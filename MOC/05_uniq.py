# very useful functions:
# https://github.com/astropy/astropy-healpix/blob/main/astropy_healpix/core.py

"""
UNIQ
====
A uniq number is a 64 bits integer equaling to : ipix + 4*(4**level).
Ref: http://ivoa.net/documents/MOC/20140602/REC-MOC-1.0-20140602.pdf

uniq_to_level_ipix(uniq)
------------------------
Convert a HEALPix cell uniq number to its (level, ipix) equivalent.

level_ipix_to_uniq(level, ipix)
-------------------------------
inverse of 'uniq_to_level_ipix'
"""

import astropy.units as u
from astropy.io import fits
import astropy_healpix as ah
import math
import numpy as np

adr = 'https://github.com/cds-astro/mocpy/raw/master/resources/bayestar.multiorder.fits'

with fits.open(adr) as hdul:
    hdul.info()
    cols = hdul[1].columns
    data = hdul[1].data

uniq = data['UNIQ']
probdensity = data['PROBDENSITY']

# find the resolution level and ...
level, ipix = ah.uniq_to_level_ipix(uniq)

# number of pixels on the side of one of the 12 'top-level' HEALPix tiles
nside = 2 ** level

npix = 12 * nside * nside
pixel_area = 4 * math.pi / npix * u.sr
area = pixel_area.to_value(u.steradian)

prob = probdensity * area
