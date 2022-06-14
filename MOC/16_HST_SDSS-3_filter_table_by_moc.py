# https://github.com/cds-astro/mocpy/blob/master/notebooks/WP5%20-%20astroquery.cds%20%26%20MOCPy.ipynb

"""
Filter an astropy.Table by a MOC
--------------------------------
1) Retrieve a catalog table from Vizier (e.g. II/50). Add the columns
'_RAJ2000' and '_DEJ2000' to the outputs. MOCPy needs the positions for
filtering the table.

2) Filter the table to get only the sources that lie into intersection MOC.
"""

import astropy.units as u
from mocpy import MOC
from astroquery.vizier import Vizier

hst_moc = MOC.from_fits('../data/hst_moc.fits')
sdss_moc = MOC.from_fits('../data/sdss_moc.fits')
both_moc = MOC.from_fits('../data/sdss_hst_moc.fits')

viz = Vizier(columns=['*', '_RAJ2000', '_DEJ2000'])
viz.ROW_LIMIT = -1

# Photometric standard stars (tables II and IV of paper)
tables = viz.get_catalogs('II/50')

table = tables[0]


idx_inside = both_moc.contains(ra=table['_RAJ2000'].T * u.deg,
                               dec=table['_DEJ2000'].T * u.deg)

sources_inside = table[idx_inside]
