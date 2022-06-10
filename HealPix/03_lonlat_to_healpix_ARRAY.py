# Get the HEALPix indexes that contains specific sky coordinates

from cdshealpix import lonlat_to_healpix
from astropy.coordinates import Longitude, Latitude
import astropy.units as u
import numpy as np

lon = Longitude([0, 50, 25], u.deg)
lat = Latitude([6, -12, 45], u.deg)

depth = np.array([5, 6])
ipix = lonlat_to_healpix(lon[:, np.newaxis],
                         lat[:, np.newaxis],
                         depth[np.newaxis, :])
