from pylab import *
xvalues, yvalues = meshgrid(arange(-3, 3, 0.1), arange(-3, 3, 0.1))
xdot =yvalues
w = 2
k = w * 0.5


ydot =k - w*xvalues
streamplot(xvalues, yvalues, xdot, ydot)
show()
