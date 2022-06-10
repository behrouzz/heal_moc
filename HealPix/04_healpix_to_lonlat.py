# Get the longitudes and latitudes of the center of some HEALPix cells
# at a given depth.

from cdshealpix import healpix_to_lonlat
import numpy as np

# only 1 cell
lon, lat = healpix_to_lonlat(ipix=17, depth=1)
print('lon:',lon)
print('lat:',lat)

# array of cells at different depths
ipix = np.array([42, 6, 10])
depth = np.array([12, 20])

lon, lat = healpix_to_lonlat(ipix=ipix[:, np.newaxis],
                             depth=depth[np.newaxis, :])

print('-'*70)
print(lon, '\n')
print(lat)
