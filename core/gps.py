from plyer import gps
from geopy.geocoders import Nominatim
from time import sleep

def obtener_ubicacion():
    gps.configure(on_location=lambda **kwargs: None, on_status=lambda stype, status: None)
    gps.start()

    sleep(3)  # tiempo de espera para obtener señal

    location = gps.get_location()
    lat = float(location['lat'])
    lon = float(location['lon'])

    try:
        geolocator = Nominatim(user_agent="bot-emergencia")
        direccion = geolocator.reverse(f"{lat}, {lon}").address
    except:
        direccion = "Dirección no disponible"

    gps.stop()
    return lat, lon, direccion
