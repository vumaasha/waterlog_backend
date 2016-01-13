from cornice import Service
from pyramid.response import Response
from pyramid.view import view_config

from .models import (
    DBSession,
    WaterLoggingInfo,
    )
from .utils import reverse_code

water_logger = Service(name='waterlog', path='/waterlog', description="record water logging information in your neighborhood")

def is_log_valid(request):
    android_id = request.params.get('android_id')
    lat = request.params.get('lat')
    long = request.params.get('long')
    level = request.params.get('level')
    area = request.params.get('area')
    sub_locality = request.params.get('sublocality')
    through_fare = request.params.get('throughfare')
    postal_code = request.params.get('postcode')
    if (android_id and lat and long and level):
        log = {
        'android_id':android_id,
        'lat':lat,
        'long':long,
        'logging_level':level
        }
        if (area):
            log['area'] = area
            log['sub_locality'] = sub_locality
            log['through_fare'] = through_fare
            log['postal_code'] = postal_code
        else:
            address_info = reverse_code(lat,long)
            log.update(address_info)
        request.validated['log'] = log
    else:
        request.errors.add(request.url,'Invalid request','Missing parameters')

@water_logger.post(validators=is_log_valid)
def store_water_logging_info(request):
    log = request.validated['log']
    water_log = WaterLoggingInfo(**log)
    DBSession.add(water_log)

@view_config(route_name='home', request_method='GET')
def home(request):
   return Response('WaterLogger is up') 


