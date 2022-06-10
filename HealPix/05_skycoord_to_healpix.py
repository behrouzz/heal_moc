# Get the HEALPix indexes that contains specific sky coordinates

from cdshealpix import skycoord_to_healpix
import astropy.units as u
from astropy.coordinates import SkyCoord
import numpy as np

ra = [0, 50, 25]* u.deg
dec = [6, -12, 45] * u.deg

c = SkyCoord(ra, dec, frame="icrs")

ipix = skycoord_to_healpix(skycoord=c, depth=12)
