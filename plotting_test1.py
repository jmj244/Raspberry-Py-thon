from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y1 = sin(2*pi*t)
y2 = cos(2*pi*t)

figure(1)
clf()
plot(t,y1,'r:')
plot(t,y2)
plot(t,y1+y2)

xlabel('Time (sec.)')
ylabel('$y^2(t)$')
legend(['signal1','signal2','addition'],loc=3)

show()
