# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import pydash as py_
from worker import worker
from models import NftsModel, PointModel, ReferralModel


@worker.task(name='worker.transfer', rate_limit='1000/s')
def transfer(event: str):
    print(event)
    args = py_.get(event,'args')
    owner = args['fromadd']
    new_owner = args['toadd']
    tokenId = args['tokenId']
    transfered = NftsModel.find_one({
        'tokenId':tokenId,
        'owner':new_owner
    })
    if transfered:
        return "Transfered"
    nft = NftsModel.find_one({
        'tokenId':tokenId,
    })
    rank = nft['rank']
    point = 0
    if rank == "0":
        point = 100
    elif rank == "1":
        point = 200
    elif rank == "2":
        point = 500
    else:
        point = 1000
    PointModel.update_one({
        'user_address':owner,
        'point':point
    },
    {
        'user_address':new_owner,
        'updated_by':'transfer-job'
    })
    NftsModel.update_one({
        'tokenId':tokenId
    },
    {
        'owner':new_owner,
        'updated_by':'transfer-job'
    })
    return "Complete transfer"