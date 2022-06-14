# https://astroquery.readthedocs.io/en/latest/cds/cds.html#getting-started

"""
Returning a MOC object as a result
----------------------------------
Example:
We want to obtain the union of the spatial coverage of all the Hubble surveys.
We want a mocpy object instead of an astropy table.
The order of the MOC we need is 7.
"""

from astropy.coordinates import SkyCoord, Angle
from regions import CircleSkyRegion
from astroquery.cds import cds
from mocpy import MOC


center = SkyCoord(0, 0, unit='deg')
radius = Angle(180, unit='deg')
allsky = CircleSkyRegion(center, radius)

moc = cds.query_region(region=allsky,
                       return_moc=True,
                       max_norder=7,
                       meta_data="ID=*HST*")

#moc.plot(title="Union of the spatial coverage of all the Hubble surveys.")
# KHATE BALA IRAD DARE
# bejash payino neveshtam:


# kh:
import matplotlib.pyplot as plt
import astropy.units as u
from mocpy import MOC, World2ScreenMPL

fig = plt.figure(111)

wcs = World2ScreenMPL(fig=fig,
                      fov=360*u.deg,
                      center=center,
                      coordsys="icrs",
                      rotation=Angle(0, u.deg),
                      projection="MOL" #AIT
                      ).w

ax = fig.add_subplot(1, 1, 1, projection=wcs)

moc.fill(ax=ax, wcs=wcs, alpha=0.5, fill=True, color="red")
#moc.border(ax=ax, wcs=wcs, alpha=0.5, color="black")

plt.xlabel('ra')
plt.ylabel('dec')
plt.grid(color="black", linestyle="dotted")
plt.show()

