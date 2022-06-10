# Get the sky coordinates of the center of some HEALPix cells at a given depth

from cdshealpix import healpix_to_skycoord
import numpy as np

ipix = np.array([42, 6, 10])

c = healpix_to_skycoord(ipix=ipix,
                        depth=12)
