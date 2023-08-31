from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_

from services.point import PointServices
from schemas.schemas import GetTopSchema,ResponsePointSchema,ResponseTopPointSchema,ReferralSchema
class ReferralServiceResource(Resource):
    @security.http(
            params=ReferralSchema(),
            login_required=False,
        )
    def get(self,params):
        message = PointServices.get_sign_message(self,params=params)
        return message

    @security.http(
        form_data=ReferralSchema(),
        login_required=False,
    )
    def put(self,form_data):
        _point = PointServices.referral(form_data=form_data)
        return _point