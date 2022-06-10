from cdshealpix import cone_search
from astropy.coordinates import Longitude, Latitude
import astropy.units as u


lon = Longitude(180, u.deg)
lat = Latitude(0, u.deg)
r = 10 * u.deg

# Get the HEALPix cells contained in a cone at a given depth
# kh: ehtemalan default nested ast
# https://cds-astro.github.io/cds-healpix-python/api.html
ipix, depth, fully_covered = cone_search(lon=lon,
                                         lat=lat, 
                                         radius=r,
                                         depth=1)



