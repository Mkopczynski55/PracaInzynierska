# Web scrapper do pobierania adresu na podstawie współrzędnych geograficznych

def get_address_from_coordinates_3417(x, y):
    
    """
    Funkcja, która przekształca współrzędne EPSG:3417 na EPSG:4326 i wykonuje geokodowanie odwrotne,
    aby znaleźć adres na podstawie współrzędnych.
    
    Parametry:
    x, y - współrzędne w systemie EPSG:3417 - takie jakie są w mojej bazie danych MySQL

    Zwraca:
    adres - Adres znaleziony na podstawie współrzędnych (lub "Nie znaleziono adresu." w razie problemów.)
    """

    try:
        # Przekształcanie współrzędnych EPSG:3417 na EPSG:4326
        transformer = Transformer.from_crs("EPSG:3417", "EPSG:4326", always_xy=True)
        lon, lat = transformer.transform(x, y)
        print(f"Przekształcone współrzędne: Longitude: {lon}, Latitude: {lat}")

        # Używamy Nominatim z geopy do geokodowania odwrotnego
        geolocator = Nominatim(user_agent="geo_locator_app")
        
        # Przerwa między zapytaniami do serwera, aby uniknąć zablokowania
        time.sleep(1)

        location = geolocator.reverse((lat, lon), exactly_one=True)

        if location:
            return location.address
        else:
            return "Nie znaleziono adresu."

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return "Nie znaleziono adresu."

# Przykład użycia
# x_3417 = 4889272.5674967505
# y_3417 = 3482741.72369067

# adres = get_address_from_coordinates_3417(x_3417, y_3417)
# print(f"Adres: {adres}")