# https://cds-astro.github.io/cds-healpix-python/examples/examples.html

from cdshealpix import cone_search
import astropy.units as u
from astropy.coordinates import Longitude, Latitude, SkyCoord, Angle
from mocpy import MOC, World2ScreenMPL
import matplotlib.pyplot as plt

lon = Longitude(0, u.deg)
lat = Latitude(0, u.deg)
r = 10 * u.deg

depth = 10

ipix, depth, fully_covered = cone_search(lon=lon,
                                         lat=lat, 
                                         radius=r,
                                         depth=depth)

# Create a MOC from a set of HEALPix cells at a given depth
moc = MOC.from_healpix_cells(ipix=ipix,
                             depth=depth,
                             fully_covered=fully_covered)


fig = plt.figure(111)#, figsize=(10, 10))

center = SkyCoord(0, 0, unit='deg', frame='icrs')
fov = 30 * u.deg
rot_ang = Angle(0, u.degree)

# Define an astropy WCS from the mocpy.WCS class

wcs = World2ScreenMPL(fig=fig,
                      fov=fov,
                      center=center,
                      coordsys="icrs",
                      rotation=rot_ang,
                      projection="AIT").w #kh

ax = fig.add_subplot(1, 1, 1, projection=wcs)
moc.fill(ax=ax, wcs=wcs, alpha=0.5, fill=True, color="green")
moc.border(ax=ax, wcs=wcs, alpha=0.5, color="black") # perimeter of MOC

plt.xlabel('ra')
plt.ylabel('dec')
plt.title('Cone search')
plt.grid(color="black", linestyle="dotted")
plt.show()

