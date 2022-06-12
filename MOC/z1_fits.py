from astropy.io import fits

hdul = fits.open('../data/P-GALEXGR6-AIS-FUV.fits')
hdul.info()

# header
hdr = hdul[0].header
hdr_1 = hdul[1].header

# FITS_rec object
data = hdul[1].data

# to get column names
cols = data.columns

# To get the first column
a = data.field(0) # by index
b = data['UNIQ']    # by column name

hdul.close()
