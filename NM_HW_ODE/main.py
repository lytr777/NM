# coding=utf-8
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as py
import explicit_euler_method
import implicit_euler_method

delta = 10.
b = 8. / 3
dt = 0.01

fig = py.figure()
ax = fig.add_subplot(111, projection='3d')

f, ppt = py.subplots()

for r in np.arange(0.0, 30.0, 5.):
    print "r = %f" % r
    system = {
        "x": lambda x, y, z: -delta * x + delta * y,
        "y": lambda x, y, z: -x * z + r * x - y,
        "z": lambda x, y, z: x * y - b * z,
        "r": r,
        "delta": delta,
        "b": b,
        "dt": dt
    }

    # начальные условия (x, y, z)
    conditions = (0.1, 0.1, 0.1)

    xs, ys, zs, ts = implicit_euler_method.solve(system, conditions)
#     ax.plot(xs, ys, zs, label="r = %f" % r)
#
#     ppt.plot(ts, xs, label="x(t), r=%f" % r)
#     ppt.plot(ts, ys, label="y(t), r=%f" % r)
#     ppt.plot(ts, zs, label="z(t), r=%f" % r)
#
# ax.legend()
# ppt.legend()
# py.show()
