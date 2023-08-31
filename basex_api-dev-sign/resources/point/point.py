from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_

from services.point import PointServices
from schemas.schemas import GetPointSchema,ResponsePointSchema
class PointServiceResource(Resource):

    @security.http(
        params=GetPointSchema(),
        login_required=False,
        response=ResponsePointSchema(),
    )
    def get(self,params):
        _point = PointServices.get_point(params=params)
        return _point