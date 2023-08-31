# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import json
import traceback

import sentry_sdk
from eth_account.messages import defunct_hash_message, encode_defunct
from pydash import get
from web3 import Web3
from web3.exceptions import TransactionNotFound

from blockchain.abi import erc20_abi


class Blockchain(Web3):
    def __init__(self, at_chain, *args, **kwargs):
        print(*args, **kwargs)
        super(Blockchain, self).__init__(*args, **kwargs)
        self.chain = at_chain
        self.decimals = {}

    def get_tx_status(self, tx_hash):
        _tx = self.eth.get_transaction_receipt(tx_hash)
        return get(_tx, 'status')

    def recover_address_from_msg_sign(self, msg, signature):

        _msg_hash = defunct_hash_message(text=msg)

        _address = self.eth.account._recover_hash(
            _msg_hash,
            signature=signature
        )

        return _address

    def sign_message(self, msg, private_key):
        _message = encode_defunct(text=msg)
        _signed_message = self.eth.account.sign_message(_message, private_key=private_key)
        return _signed_message.signature.hex()

    def get_transfer_info(self, token, tx_hash):
        try:
            _smc = getattr(self, f'{token.lower()}_smc')
            if not _smc:
                return None, None
            _tx = self.eth.wait_for_transaction_receipt(tx_hash)
            # _tx = _smc.eth.get_transaction_receipt(tx_hash)
            _log_smc = _smc.events.Transfer().processReceipt(_tx)
            if _log_smc:
                _tx_info = json.loads(Web3.toJSON(_log_smc))
                if isinstance(_tx_info, list) and _tx_info:
                    return _tx_info[0], _tx
        except TransactionNotFound as e:
            return str(e), None
        except Exception as e:
            sentry_sdk.capture_exception()
            traceback.print_exc()
            return -1, str(e)

    def to_wei(self, amount, decimal):
        decimals = {
            '0': 'wei',
            '3': 'kwei',
            '6': 'mwei',
            '9': 'gwei',
            '12': 'szabo',
            '15': 'finney',
            '18': 'ether'
        }
        return self.to_wei(amount, get(decimals, str(decimal), 'ether'))
