from geopy.geocoders import Nominatim
geolocator = Nominatim()

def reverse_code(lat,long):
    def get_address_attr(address,attr):
        if (address):
            return address.get(attr)

    location = geolocator.reverse("{},{}".format(lat,long))
    address_info = {}
    address_ = location.raw['address']
    district_ = get_address_attr(address_,'state_district')
    if district_:
        district_ = district_.replace('district','').rstrip()
    address_info['area'] = district_
    address_info['sub_locality'] = get_address_attr(address_,'suburb')
    address_info['through_fare'] = get_address_attr(address_,'road')
    address_info['postal_code'] = get_address_attr(address_,'postcode')
    return address_info

