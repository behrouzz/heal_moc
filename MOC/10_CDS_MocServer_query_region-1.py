# https://astroquery.readthedocs.io/en/latest/cds/cds.html#getting-started

from astropy.coordinates import SkyCoord, Angle
from regions import CircleSkyRegion
from astroquery.cds import cds

# First, we need to define a cone region
# --------------------------------------
center = SkyCoord(10.8, 32.2, unit='deg')
radius = Angle(1.5, unit='deg')

cone = CircleSkyRegion(center, radius)

# Then, we call the query_region() method with the cone
# -----------------------------------------------------
a = cds.query_region(region=cone)

"""
NOTE 1:
-------
By default, query_region() returns an astropy.table.Table object storing
the data-sets as rows and their meta-datas as columns.

Data-sets might have no information for a specific meta-data. If so, the
value associated with this meta-data for this data-set is set to “-”.


NOTE 2:
-------
We can also query the MOCServer by passing a MOC object to <region> argument.

moc = ...
b = cds.query_region(region=moc)
"""
