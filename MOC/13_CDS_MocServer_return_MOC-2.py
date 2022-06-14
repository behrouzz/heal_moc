# https://astroquery.readthedocs.io/en/latest/cds/cds.html#getting-started

"""
Retrieve the MOC of a specific data-set
----------------------------------
To retrieve the MOC of a specific data-set, use <find_datasets> with the ID
of the data-set and <return_moc> parameter set to True.

Example:
We want to get the MOC of the GALEXGR6/AIS/FUV survey.
"""

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord, Angle
#from regions import CircleSkyRegion
from astroquery.cds import cds
from mocpy import MOC, World2ScreenMPL

moc = cds.find_datasets(meta_data="ID=CDS/P/GALEXGR6/AIS/FUV", return_moc=True)


# Plotting the moc
# ----------------

fig = plt.figure(111)

wcs = World2ScreenMPL(fig=fig,
                      fov=360*u.deg,
                      center=SkyCoord(0, 0, unit='deg'),
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

