from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_

from schemas.schemas import MintingTimeSchema
from services.minting_time import MintingTimeServices
class MintingTimeResouce(Resource):
    @security.http(
        login_required=False,
        response=MintingTimeSchema(),
    )
    def get(self):
        _time = MintingTimeServices.get_minting_time()
        return _time