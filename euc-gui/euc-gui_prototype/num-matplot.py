#!/usr/bin/python
import numpy
from matplotlib import pyplot
x = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(x)
pyplot.plot(x, y)
pyplot.show()
