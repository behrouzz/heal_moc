# Get the HEALPix indexes that contains specific sky coordinates

from cdshealpix import lonlat_to_healpix
from astropy.coordinates import Longitude, Latitude
import astropy.units as u
import numpy as np

lon = Longitude(0.001 *u.deg)
lat = Latitude(0 *u.deg)

ipix = lonlat_to_healpix(lon=lon,
                         lat=lat,
                         depth=1)
