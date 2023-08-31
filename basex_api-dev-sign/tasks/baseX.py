# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import pydash as py_
from worker import worker
from models import NftsModel, PointModel, ReferralModel

@worker.task(name='worker.mintNft', rate_limit='1000/s')
def mintNft(event: str):
    # try:
        args = py_.get(event,'args')
        owner =args['owner']
        rank = args['rank']
        time_minted = args['time_minted']
        tokenId = args['tokenId']
        _ = NftsModel.find_one(filter={'tokenId':tokenId})
        if _:
            return "TokenId exitst"
        data_insert ={
            'owner':owner,
            'rank':rank,
            'time_minted':time_minted,
            'tokenId':tokenId,
            'created_by':'admin'
        }
        NftsModel.insert_one(data_insert)
        point = 0
        if rank == "0":
            point = 100
        elif rank == "1":
            point = 200
        elif rank == "2":
            point = 500
        else:
            point = 1000
        PointModel.insert_one({
                'user_address':owner,
                'point':point,
                'created_by':'BaseX-job'
            })    
        _ref = ReferralModel.find_one({
            'user_address':owner
        })
        if _ref:
            minted = NftsModel.find_one({
                 'owner':_ref['referral_address']
            })
            if minted:
                PointModel.insert_one({
                    'user_address':_ref['referral_address'],
                    'referral':False,
                    'point':point/10,
                    'referral':True,
                    'created_by':'BaseX-job'
                })
                return "Success mint with referral"
 
        return "Success mint"
    # except Exception as e:
    #     return "Fail"
    
  
