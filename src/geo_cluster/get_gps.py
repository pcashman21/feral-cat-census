import exifread

def get_gps(file):
    """
    Get the GPS coordinates from the EXIF data of an image.

    file: The image file to read.
    :return: The latitude and longitude, if available.

    """

    file = open(file, 'rb')
    tags = exifread.process_file(file)
    try:
        gps_latitude = tags['GPS GPSLatitude'].values
        gps_longitude = tags['GPS GPSLongitude'].values
    except KeyError:
        return None, None
    gps_latitude = float(gps_latitude[0]) + float(gps_latitude[1]/60) + float(gps_latitude[2]/3600)
    gps_longitude = float(gps_longitude[0]) + float(gps_longitude[1]/60) + float(gps_longitude[2]/3600)
    return gps_latitude, gps_longitude
        