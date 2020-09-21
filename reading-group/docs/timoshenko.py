import numpy
from matplotlib import pyplot

Hi = 2
hi = 4
H = 1/Hi
h = 1/hi

x_H = numpy.linspace(0, 1, num=(Hi + 1))
x_h = numpy.linspace(0, 1, num=(hi + 1))


def diff(w, h):
    return (w[1:] - w[:-1])/h


def avg(b):
    return (b[1:] + b[:-1])/2


def R0(w):
    a = numpy.asarray([[1, 0],
                       [1/2, 1/2],
                       [0, 1]], dtype=float)
    first, *parts = [numpy.dot(a, w[i:i+2])
                     for i in range(len(w)-1)]
    return numpy.hstack((first, *(p[1:] for p in parts)))


def R(w, b, h):
    w_ = R0(w)
    # These are the only ones we can modify.
    w_[1::2] -= h*(diff(w_, h) - avg(b))[::2]
    return w_


w_H = numpy.asarray([0.5, 0, 0.5], dtype=float)

b_H = numpy.asarray([-2, 0, 2], dtype=float)

ker_H = diff(w_H, H) - avg(b_H)

fig, axes = pyplot.subplots()

axes.plot(x_H, w_H, "o-", label=r"$w_H$")
axes.plot(x_H, b_H, "s-", label=r"$\beta_H$")
axes.plot(avg(x_H), ker_H, "^-", label=r"$\overline{(w^\prime_H - \beta_H)}^H$")

axes.legend()

fig.savefig("timoshenko-coarse-grid.png", dpi=300)
               
w_h = R0(w_H)
b_h = R0(b_H)
ker_h = diff(w_h, h) - avg(b_h)
w_mod_h = R(w_H, b_h, h)
ker_mod_h = diff(w_mod_h, h) - avg(b_h)

fig, axes = pyplot.subplots()

axes.plot(x_h, w_h, "o-", label=r"$w_h = R^{V,0}_H w_H$")
axes.plot(x_h, b_h, "s-", label=r"$\beta_h = R^{V,0}_H \beta_h$")
axes.plot(x_h, w_mod_h, "v-", label=r"$\tilde{w}_h = R^V_H w_H$")
axes.plot(avg(x_h), ker_h, "^-", label=r"$\overline{(w^\prime_h - \beta_h)}^h$")
axes.plot(avg(x_h), ker_mod_h, "-", label=r"$\overline{(\tilde{w}^\prime_h - \beta_h)}^h$")
axes.legend()

fig.savefig("timoshenko-fine-grid.png", dpi=300)
