from marshmallow import Schema, EXCLUDE, fields
from lib import ObjectIdField

class GetPointSchema(Schema):
    class Meta:
        unknown=EXCLUDE
        ordered=True    
    user_address = fields.String(required=True)

class ResponsePointSchema(Schema):
    class Meta:
        unknown=EXCLUDE
        ordered=True
    user_address = fields.String(required=True)
    total_referral=fields.Int()
    total_point=fields.Int()

class GetTopSchema(Schema):
    class Meta:
        unknown=EXCLUDE
        ordered=True
    top = fields.Int(require=True)

class ResponseTopPointSchema(Schema):
    class Meta:
        unknown=EXCLUDE
        ordered=True
    
    user = fields.List(fields.Nested(ResponsePointSchema), default=[], missing=[])


class ReferralSchema(Schema):
    class Meta:
        unknown =EXCLUDE
        ordered=True
    user_address = fields.String(required=True)
    referral_address = fields.String()
    signature = fields.String(default='', missing='')
    nonce = fields.Int()    

class MintingTimeSchema(Schema):
    class Meta:
        unknown =EXCLUDE
        ordered=True
    time = fields.Int()
    stage = fields.Int()
