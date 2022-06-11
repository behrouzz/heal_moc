# Intersection between GALEX and SDSS

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import Angle, SkyCoord
from mocpy import MOC, World2ScreenMPL

sdss = MOC.from_fits('../data/P-SDSS9-r.fits')
galex = MOC.from_fits('../data/P-GALEXGR6-AIS-FUV.fits')

inter = sdss.intersection(galex)
union = sdss.union(galex)

# plotting

fig = plt.figure(111)

fov = 160 * u.deg
center = SkyCoord(ra=0, dec=0, unit='deg', frame='icrs')
rot_ang = Angle(0, u.degree)

wcs = World2ScreenMPL(fig=fig,
                      fov=fov,
                      center=center,
                      coordsys="icrs",
                      rotation=rot_ang,
                      projection="AIT").w

ax = fig.add_subplot(1, 1, 1, projection=wcs)

union.fill(ax=ax, wcs=wcs, alpha=0.5, fill=True,
           color="red", linewidth=0, label="Union")
union.border(ax=ax, wcs=wcs, alpha=1, color="red")

inter.fill(ax=ax, wcs=wcs, alpha=0.5, fill=True,
           color="green", linewidth=0, label="Intersection")
inter.border(ax=ax, wcs=wcs, alpha=1, color="green")

ax.legend()

plt.xlabel('ra')
plt.ylabel('dec')
plt.title('Logical operations between SDSS and GALEX')
plt.grid(color="black", linestyle="dotted")
plt.show()
