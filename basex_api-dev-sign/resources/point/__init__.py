from services.point import PointServices
from resources.point.point import PointServiceResource
from resources.point.top_point import TopPointServiceResource
from resources.point.top_referral import TopReferralServiceResource
from resources.point.referral import ReferralServiceResource
point_resources = {
    "/total_point":PointServiceResource,
    "/top_point":TopPointServiceResource,
    "/top_referral":TopReferralServiceResource,
    "/referral":ReferralServiceResource
}