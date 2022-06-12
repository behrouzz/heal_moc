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


from_valued_healpix_cells
-------------------------
Creates a MOC from a list of uniq associated with values.
"""

import astropy.units as u
from astropy.io import fits
import astropy_healpix as ah
import numpy as np

adr = 'https://github.com/cds-astro/mocpy/raw/master/resources/bayestar.multiorder.fits'

with fits.open(adr) as hdul:
    cols = hdul[1].columns
    data = hdul[1].data

uniq = data['UNIQ']
probdensity = data['PROBDENSITY']

level, ipix = ah.uniq_to_level_ipix(uniq)

nside = 2 ** level
npix = 12 * nside * nside
area = 4 * np.pi / npix
prob = probdensity * area

#==================================================

from mocpy import MOC

cumul_to = [0.9, 0.8, 0.7, 0.6, 0.5]
colors = ['blue', 'green', 'yellow', 'orange', 'red']
mocs = [MOC.from_valued_healpix_cells(uniq, prob, cumul_to=c) for c in cumul_to]

#===================================================

from mocpy import World2ScreenMPL
from astropy.coordinates import Angle, SkyCoord
import matplotlib.pyplot as plt

fig = plt.figure()


with World2ScreenMPL(fig, 
        fov=50 * u.deg,
        center=SkyCoord(315, 15, unit='deg', frame='icrs'),
        coordsys="icrs",
        rotation=Angle(0, u.degree),
        projection="AIT") as wcs:
    ax = fig.add_subplot(1, 1, 1, projection=wcs)
    # Call fill with a matplotlib axe and the `~astropy.wcs.WCS` wcs object.
    for (moc, c, col) in zip(mocs, cumul_to, colors):
        moc.fill(ax=ax, wcs=wcs, alpha=0.5, linewidth=0, fill=True, color=col, label='confidence probability ' + str(round(c*100)) + '%')
        moc.border(ax=ax, wcs=wcs, alpha=0.5, color=col)

    ax.legend()

plt.xlabel('ra')
plt.ylabel('dec')
plt.title('Bayestar')
plt.grid(color="black", linestyle="dotted")
plt.show()
