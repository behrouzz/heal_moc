import matplotlib.pyplot as plt
from astropy.coordinates import Angle, SkyCoord
import astropy.units as u
from mocpy import MOC, World2ScreenMPL

# https://github.com/cds-astro/mocpy/blob/master/resources/P-GALEXGR6-AIS-FUV.fits
moc = MOC.from_fits('../data/P-GALEXGR6-AIS-FUV.fits')

fig = plt.figure(111)

fov = 90 * u.deg
center = SkyCoord(ra=0, dec=0, unit='deg', frame='icrs')
rot_ang = Angle(0, u.degree)

wcs = World2ScreenMPL(fig=fig,
                      fov=fov,
                      center=center,
                      coordsys="icrs",
                      rotation=rot_ang,
                      projection="AIT").w

ax = fig.add_subplot(1, 1, 1, projection=wcs)

moc.fill(ax=ax, wcs=wcs, alpha=0.5, fill=True, color="green")

moc.border(ax=ax, wcs=wcs, alpha=0.5, color="black")

plt.xlabel('ra')
plt.ylabel('dec')
plt.grid(color="black", linestyle="dotted")
plt.show()
