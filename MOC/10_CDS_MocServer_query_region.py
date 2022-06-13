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
#a = cds.query_region(region=cone) # HUGE!!!


# Retrieve only a subset of meta-datas
# ------------------------------------
cols = ['ID', 'dataproduct_type', 'moc_sky_fraction', 'moc_access_url']
#b = cds.query_region(region=cone, fields=cols)


# Retrieving data-sets based on their meta-data values
# ----------------------------------------------------
# Let's retrieve only image data-sets that lie in the previously defined cone.

c = cds.query_region(region=cone,
                     fields=cols,
                     meta_data="dataproduct_type=image")

# Some filtering examples:
# http://alasky.unistra.fr/MocServer/example


"""
NOTE 1:
-------
By default, query_region() returns an astropy.table.Table object storing
the data-sets as rows and their meta-datas as columns.
Data-sets might have no information for a specific meta-data. If so, the
value associated with this meta-data for this data-set is set to “-”.

NOTE 2:
-------
By default, query_region() returns an astropy.table.Table.
You can get a mocpy.MOC object instead of an astropy.table.Table by setting
the parameter <return_moc> to True.
An additional argument <max_norder> allows the user to set the resolution
of the returned MOC that he wants. (Ex: next file)


NOTE 3:
-------
We can also query the MOCServer by passing a MOC object to <region> argument.
moc = ...
b = cds.query_region(region=moc)

NOTE 4:
-------
The <meta_data> parameter of query_region() allows the user to write an
algebraic expression on the meta-datas.

NOTE 5:
-------
The argument <max_rec> specifies an upper limit for the number of data-sets
to be returned.
"""
