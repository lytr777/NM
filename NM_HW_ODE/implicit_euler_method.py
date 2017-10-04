import numpy as np


def solve(system, conditions):
    dt = system["dt"]
    t = 0
    x, y, z = conditions
    xs, ys, zs, ts = [x], [y], [z], [t]

    for _ in range(1000):
        F = [
            lambda x1, y1, z1: (system["delta"] * y1 + x) / (1 + system["delta"] * system["dt"]),
            lambda x1, y1, z1: (y + system["r"] * x1 * system["dt"] - x1 * z1 * system["dt"]) / (1 + system["dt"]),
            lambda x1, y1, z1: (z + x1 * y1 * system["b"] * system["dt"]) / (1 + system["b"] * system["dt"])
        ]
        F_N = [
            lambda x1, y1, z1: x - (system["delta"] * y1 + x) / (1 + system["delta"] * system["dt"]),
            lambda x1, y1, z1: y - (y + system["r"] * x1 * system["dt"] - x1 * z1 * system["dt"]) / (1 + system["dt"]),
            lambda x1, y1, z1: z - (z + x1 * y1 * system["b"] * system["dt"]) / (1 + system["b"] * system["dt"])
        ]

        FM_N = [
            [
                lambda x1, y1, z1: 1,
                lambda x1, y1, z1: -(system["delta"] * system["dt"]) / (1 + system["delta"] * system["dt"]),
                lambda x1, y1, z1: 0],
            [
                lambda x1, y1, z1: -(system["r"] - z1) * system["dt"]/(1 + system["dt"]),
                lambda x1, y1, z1: 1,
                lambda x1, y1, z1: x1 * system["dt"] / (1 + system["dt"])
            ],
            [
                lambda x1, y1, z1: -y1 * system["b"] * system["dt"] / (1 + system["b"] * system["dt"]),
                lambda x1, y1, z1: -x1 * system["b"] * system["dt"] / (1 + system["b"] * system["dt"]),
                lambda x1, y1, z1: 1
            ]
        ]

        # x, y, z = __newton_method(F, FM, [x, y, z], 0.8)
        v, converge = __simple_iterations(F, [x, y, z], 0.01)
        # if not converge:
        #     print "Not converge"
        #     print v
        # v, converge = __newton_method(F_N, FM_N, [x, y, z], 0.01)
        x, y, z = v
        # print [x, y, z]
        t = t + dt

        xs.append(x)
        ys.append(y)
        zs.append(z)
        ts.append(t)


    return xs, ys, zs, ts


def __seidel(F, x0, eps):
    x = x0[:]

    dist = 1
    iterations = 10000
    it = 1

    while dist > eps and it < iterations:
        x1 = np.array(x[:])
        for i in range(len(x)):
            f_v = np.vectorize(lambda f: f(x[0], x[1], x[2]))
            x2 = f_v(F)
            x1[i] = x2[i]
        dist = np.linalg.norm(x1 - x)
        x = x1
        it += 1

    return x


# mb
def __simple_iterations(F, x0, eps):
    x = x0[:]

    dist = 1
    iterations = 10000
    it = 1
    while dist > eps and it < iterations:
        f_v = np.vectorize(lambda f: f(x[0], x[1], x[2]))
        x1 = f_v(F)

        dist = np.linalg.norm(x1 - x)
        # if any(math.isnan(t) or math.isinf(t) for t in x1):
        #     break
        x = x1
        it += 1

    return x, it < iterations


def __newton_method(F, FM, x0, eps):
    x = x0[:]

    # x = x -
    print "x:"
    print x

    dist = 1
    iterations = 10000
    it = 1
    while dist > eps and it < iterations:
        f_v = np.vectorize(lambda f: f(x[0], x[1], x[2]))
        W = f_v(FM)
        F1 = f_v(F)

        x1 = x - np.linalg.inv(W).dot(F1)

        dist = np.linalg.norm(x1 - x)
        x = x1
        it += 1

    return x, it < iterations
