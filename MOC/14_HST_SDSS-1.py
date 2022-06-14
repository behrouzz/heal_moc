# https://github.com/cds-astro/mocpy/blob/master/notebooks/WP5%20-%20astroquery.cds%20%26%20MOCPy.ipynb

"""
Let's retrieve:

- The MOC representing the footprint of all the HST combined surveys at the
  order 8 (i.e. the precision of the MOC, ~13 arcmin)
  
- The MOC representing the footprint of SDSS9: ID='CDS/P/SDSS9/color'
"""

from regions import CircleSkyRegion
from astropy.coordinates import Angle, SkyCoord
from astroquery.cds import cds

allsky = CircleSkyRegion(SkyCoord(0, 0, unit="deg"), Angle(180, unit="deg"))

# ALL HST surveys (covering ANY region of the sky)
hst_moc = cds.query_region(region=allsky,
                           return_moc=True,
                           max_norder=8,
                           meta_data="ID=*HST*")

# SDSS9
sdss_moc = cds.find_datasets(meta_data="ID=CDS/P/SDSS9/color",
                             return_moc=True)

# Compute their intersection
sdss_hst_moc = sdss_moc.intersection(hst_moc)

# If we need to convert to hdul object directly
#hdul = sdss_hst_moc.serialize(format='fits')

# If we need to save as FITS file
hst_moc.write("../data/hst_moc.fits", format="fits", overwrite=True)
sdss_moc.write("../data/sdss_moc.fits", format="fits", overwrite=True)
sdss_hst_moc.write("../data/sdss_hst_moc.fits", format="fits", overwrite=True)
