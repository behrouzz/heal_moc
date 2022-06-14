# https://github.com/cds-astro/mocpy/blob/master/notebooks/WP5%20-%20astroquery.cds%20%26%20MOCPy.ipynb

# Let's read the files that we have created

from mocpy import MOC, World2ScreenMPL

hst_moc = MOC.from_fits('../data/hst_moc.fits')
sdss_moc = MOC.from_fits('../data/sdss_moc.fits')
both_moc = MOC.from_fits('../data/sdss_hst_moc.fits')

# Plotting

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord, Angle

fig = plt.figure()

wcs = World2ScreenMPL(
    fig=fig,
    fov=220*u.deg,
    center=SkyCoord(ra=0, dec=0, unit='deg', frame='icrs'),
    coordsys="icrs",
    rotation=Angle(0, u.deg),
    projection="AIT").w

ax = fig.add_subplot(1, 1, 1, projection=wcs)

# sdss
sdss_moc.fill(ax=ax, wcs=wcs, edgecolor='r', facecolor='r',
              linewidth=0, alpha=0.7, fill=True, label='SDSS9')
sdss_moc.border(ax=ax, wcs=wcs, alpha=0.5, color="black")

# hst
hst_moc.fill(ax=ax, wcs=wcs, edgecolor='g', facecolor='g',
             linewidth=0, alpha=0.7, fill=True, label='HST all surveys')
hst_moc.border(ax=ax, wcs=wcs, alpha=0.5, color="black")

# both
both_moc.fill(ax=ax, wcs=wcs, edgecolor='b', facecolor='b',
              linewidth=0, alpha=0.7, fill=True, label='intersection')
both_moc.border(ax=ax, wcs=wcs, alpha=0.5, color="black")

plt.xlabel('ra')
plt.ylabel('dec')
plt.grid(color="black", linestyle="dotted")
plt.legend()
plt.show()
