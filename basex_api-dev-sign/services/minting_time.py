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
from models import MintingTimeModel

class MintingTimeServices:
    @classmethod
    def get_minting_time(cls):
        time = MintingTimeModel.find_one({})
        return time
