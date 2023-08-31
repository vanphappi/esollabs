# from resources.health_check import HealthCheck
# from resources.hello import HelloWorld
from resources.point import PointServices
from resources.point import point_resources
from resources.mingting_time import MintingTimeResouce
# from resources.iapi import iapi_resources
api_resources = {
    # '/hello': HelloWorld,
    # '/common/health_check': HealthCheck,
    # **{f'/iapi{k}': val for k, val in iapi_resources.items()},
    **{f'/point{k}': val for k, val in point_resources.items()},
    '/minting_time':MintingTimeResouce
}

