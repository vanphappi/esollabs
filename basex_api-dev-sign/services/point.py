import datetime
import traceback
import pydash as py_
import bson
from bson import ObjectId
from pymongo import MongoClient

# from lib import dt_utcnow
from lib.utils import util_web3, dt_utcnow
from datetime import datetime, timedelta
from connect import redis_cluster
from worker import worker
from models import NftsModel,PointModel,ReferralModel
from helper import WalletHelper
from exceptions.referral import InvalidNonce,InvalidSignature
class PointServices:
    def get_point(params):
        _user_address = py_.get(params, 'user_address')
        
        pipeline = [
            {"$match": {"$and": [{"user_address": _user_address}, {"referral": True}]}},
            {        
                "$group": {
                    "_id": "$user_address",
                    "total_referral": {"$sum": 1}
                }
            },
            {"$project": {
                "_id": 0, 
                "user_address": "$_id",
                "total_referral": 1
            }}
        ]
        
        user = list(PointModel.col.aggregate(pipeline))
        if not user:
            user = {
                "user_address":_user_address,
                "total_referral":0,
            }
        else:
            user = user[0]    
        pipeline = [
            {"$match": {"user_address": _user_address}},
            {        
                "$group": {
                    "_id": "$user_address",
                    "total_point": {"$sum": "$point"}
                }
            },
            {"$project": {
                "_id": 0, 
                "total_point": 1
            }}
        ]
        
        add = list(PointModel.col.aggregate(pipeline))
        if not add:
            add = {
                "total_point":0
            }
        else:
            add = add[0]    
        user.update(add)
        return user

    @classmethod
    def get_top_point(cls,params):
        _top = py_.get(params,'top')
        pipeline = [
            {
                "$group": {
                    "_id": "$user_address",
                    "total_point": {"$sum": "$point"}
                }
            },
            {"$sort": {"total_point": -1}},
            {"$limit": _top},
            {"$project": {
                "_id": 0, 
                "user_address": "$_id",
                "total_point":1
            }}
        ]
        _ = PointModel.col.aggregate(pipeline)
        user= {"user":_}  
        return user
    
    @classmethod
    def get_top_referral(cls,params):
        _top = py_.get(params,'top')
        pipeline = [
            {"$match": {"referral": True}},
            {
                "$group": {
                    "_id": "$user_address",
                    "total_referral": {"$sum": 1}
                }
            },
            {"$sort": {"total_referral": -1}},
            {"$limit": _top},
            {"$project": {
                "_id": 0, 
                "user_address": "$_id",
                "total_referral":1
            }}
        ]
        _ = PointModel.col.aggregate(pipeline)
        user= {"user":_}
        return user
    
    @staticmethod
    def validate_nonce(_nonce):
        _dt = dt_utcnow().timestamp() - _nonce
        print(_dt)
        if 360 >= _dt >= 0:
            return True

        return False
    @classmethod
    def referral(cls,form_data):

        user_address = py_.get(form_data,'user_address')
        _nonce = py_.get(form_data,'nonce')
        if not cls.validate_nonce(_nonce): 
            raise InvalidNonce('nonce invalid')
        signature = py_.get(form_data,'signature')
        _message = WalletHelper._get_sign_msg(user_address, _nonce)
        if len(signature)!= 65:
            raise InvalidSignature('signature invalid')
        _signer = WalletHelper.get_address_of(signature,_message)
        if _signer == user_address:
            referral_address = py_.get(form_data,'referral_address')
            if len(referral_address)!=42:
                referral_address= 'wrong'
            print(user_address)
            print(referral_address)
            if user_address != referral_address:
                ReferralModel.update_one({
                    'user_address':user_address
                },
                {
                    'referral_address':referral_address,        
                    'created_by':'admin',
                    'updated_by':'admin',

                },upsert=True
                )
            return{}
        raise InvalidSignature('signature invalid')
    @staticmethod
    def get_sign_message(cls,params):
        _address = py_.get(params,'user_address')
        if not _address:
            return
        _message,_nonce = WalletHelper.get_sign_msg(_address)
        return {"message":_message,
                "address": _address,
                "nonce":_nonce}
