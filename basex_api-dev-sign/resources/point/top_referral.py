from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_

from services.point import PointServices
from schemas.schemas import GetTopSchema,ResponsePointSchema,ResponseTopPointSchema
class TopReferralServiceResource(Resource):

    @security.http(
        params=GetTopSchema(),
        login_required=False,
        response=ResponseTopPointSchema(),
    )
    def get(self,params):
        user= PointServices.get_top_referral(params=params)
        return user