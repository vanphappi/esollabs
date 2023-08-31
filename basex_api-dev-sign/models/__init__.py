# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""

from config import Config
from connect import connect_db, redis_cluster
from lib import DaoModel

# __models__ = ['UsersModel', 'SessionsModel']
PointModel = DaoModel(col=connect_db.db.point, redis=redis_cluster, project=Config.PROJECT, broker=Config.BROKER_URL)
NftsModel = DaoModel(col=connect_db.db.nft_mint, redis=redis_cluster, project=Config.PROJECT, broker=Config.BROKER_URL)
ReferralModel = DaoModel(col=connect_db.db.referral, redis=redis_cluster, project=Config.PROJECT, broker=Config.BROKER_URL)
MintingTimeModel = DaoModel(col=connect_db.db.minting_time, redis=redis_cluster, project=Config.PROJECT, broker=Config.BROKER_URL)


