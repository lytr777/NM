import numpy as np
import cases
import pylab as pl
import explicit_counter_flow_method
import explicit_flow_method
import leapfrog_method

# u, g, conditions = cases.get_steps()
# u, g, conditions = cases.get_flash_light()
u, g, conditions = cases.get_waves()

cs = leapfrog_method.solve(u, g, conditions)

m_x, m_y = np.mgrid[
    slice(conditions["x_min"], conditions["x_max"], conditions["dx"]),
    slice(conditions["t_min"], conditions["t_max"], conditions["dt"])]

print cs
pl.pcolormesh(m_x, m_y, cs)
pl.show()
