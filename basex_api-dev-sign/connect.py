# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import asyncio
import motor
from flask_pymongo import PyMongo
import motor.motor_asyncio
from rediscluster import RedisCluster
from web3 import Web3
from blockchain import Blockchain
from config import Config
from redlock import Redlock
from socket_io_emitter import Emitter


class InterfaceAsync:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_URI)
        self.client.get_io_loop = asyncio.get_event_loop
        self.db = self.client.core


connect_db = PyMongo()

redis_cluster = None
# RedisCluster(
#     startup_nodes=Config.REDIS_CLUSTER,
#     decode_responses=True,
#     skip_full_coverage_check=True
# )

# dlm = Redlock(Config.REDLOCK_REDIS, retry_count=2)

# web3_providers = {
#     "97": Blockchain('BSC', Web3.HTTPProvider(Config.BSC_RPC_URI, request_kwargs={'timeout': 60})),
# }
# socket_io = Emitter(Config.REDIS_CLUSTER[0])

from lib import HTTPSecurity

security = HTTPSecurity(redis=redis_cluster)

