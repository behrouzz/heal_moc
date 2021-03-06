import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import Angle, SkyCoord
from mocpy import MOC, World2ScreenMPL


# The set of points delimiting the polygon in deg
vertices = np.array([[18.36490956,  5.        ],
                    [15.7446692 ,  6.97214743],
                    [16.80755056, 10.29852928],
                    [13.36215502, 10.14616136],
                    [12.05298691, 13.10706197],
                    [ 9.54793022, 10.4556709 ],
                    [ 8.7677627 ,  7.80921809],
                    [ 9.71595962,  5.30855011],
                    [ 7.32238541,  6.44905255],
                    [ 0.807265  ,  6.53399616],
                    [ 1.08855146,  3.51294225],
                    [ 2.07615384,  0.7118289 ],
                    [ 3.90690158, -1.61886929],
                    [ 9.03727956,  2.80521847],
                    [ 9.22274427, -4.38008174],
                    [10.23563378,  4.06950324],
                    [10.79931601,  3.77655576],
                    [14.16533992,  1.7579858 ],
                    [19.36243491,  1.78587203],
                    [15.31732084,  5.        ]])

c = SkyCoord(vertices, unit="deg", frame="icrs")

# A point that we say it belongs to the inside of the MOC
inside = SkyCoord(ra=10, dec=5, unit="deg", frame="icrs")

moc = MOC.from_polygon_skycoord(c, max_depth=9)

fig = plt.figure(111)

wcs = World2ScreenMPL(fig=fig,
                      fov=20 * u.deg,
                      center=inside,
                      coordsys="icrs",
                      rotation=Angle(0, u.degree),
                      projection="TAN").w

ax = fig.add_subplot(1, 1, 1, projection=wcs)
moc.fill(ax=ax, wcs=wcs, alpha=0.5, fill=True, color="red", linewidth=1)
moc.border(ax=ax, wcs=wcs, alpha=1, color="red")

plt.xlabel('ra')
plt.ylabel('dec')
plt.title('MOC from a polygon')
plt.grid(color="black", linestyle="dotted")
plt.show()

# NOTE
# The gnomonic projection transforms great circles into straight lines. 
