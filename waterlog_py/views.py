from pyramid.response import Response
from pyramid.view import view_config
from cornice import Service

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    WaterLoggingInfo,
    )

water_logger = Service(name='waterlog', path='/waterlog', description="record water logging information in your neighborhood")

def is_log_valid(request):
    android_id = request.params.get('android_id')
    lat = request.params.get('lat')
    long = request.params.get('long')
    level = request.params.get('level')
    if (android_id and lat and long and level):
        log = {
        'android_id':android_id,
        'lat':lat,
        'long':long,
        'logging_level':level
        }
        request.validated['log'] = log
    else:
        request.errors.add(request.url,'Invalid request','Missing parameters')

@water_logger.post(validators=is_log_valid)
def store_water_logging_info(request):
    log = request.validated['log']
    water_log = WaterLoggingInfo(**log)
    DBSession.add(water_log)


