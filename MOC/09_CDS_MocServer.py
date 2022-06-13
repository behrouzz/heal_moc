# https://github.com/cds-astro/mocpy/blob/master/notebooks/WP5%20-%20astroquery.cds%20%26%20MOCPy.ipynb
# I arrived here from the link above.

"""
===============
CDS MOC Service
===============

astroquery.cds offers a Python access API to the MOCServer that stores
~20000 metadata and MOCs of Vizier catalogues and ~500 metadata and MOCs
of HiPS image surveys.
Ref: https://astroquery.readthedocs.io/en/latest/cds/cds.html#getting-started

CDS has set up a server known as the MOCServer storing data-set names each
associated with a MOC spatial coverage and some meta-datas giving a more
detailed explanation of the data-set.

The MOCServer aims at returning the data-sets having at least one source
lying in a specific sky region defined by the user

Internally, the MOCServer performs the intersection between the given sky
region and the MOCs associated with each data-sets.

Example 1:
----------
We have queried the MOCServer with a cone region of center
ra, dec = (10.8, 32.2) deg and radius = 1.5 deg.
In return, the MOCServer gives a list of data-sets each tagged with an
unique ID along with some other meta-datas too e.g. obs_title,
obs_description, moc_access_url (url for accessing the MOC associated with
the data-set. Usually a FITS file storing a list of HEALPix cells).

http://alasky.unistra.fr/MocServer/query?RA=10.8&DEC=32.2&SR=1.5&intersect=overlaps&get=record&fmt=html

It is also possible to ask the MOCServer for retrieving data-sets based on
their meta-data values.

Example 2:
----------
Here we have queried the MOCServer for only the image data-sets being in
the cone defined above (dataproduct_type meta-data equals to "image").

http://alasky.unistra.fr/MocServer/query?RA=10.8&DEC=32.2&SR=1.5&intersect=overlaps&get=record&fmt=html&expr=(dataproduct_type=image)


This package (astroquery.cds) implements two methods:
-----------------------------------------------------
1) query_region(): retrieving data-sets (their associated MOCs and meta-datas)
                   having sources in a given region.

2) find_datasets(): retrieving data-sets (their associated MOCs and meta-datas)
                    based on the values of their meta-datas.

"""
