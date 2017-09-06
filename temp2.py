import numpy as np
import pylab as pl
x = [  1, 2,  3, 4, 5, 6]
y = [7.5,10,8.6, 8, 8, 8]
pl.title ('Promedio por semestre')
pl.ylabel('Promedio')
pl.xlabel('Semestre')
pl.axis([1,6,5,10])
pl.plot (x,y,'k--', linewidth = 2)
pl.savefig('temp2.png')
pl.show()
