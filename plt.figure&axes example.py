from matplotlib.widgets import MultiCursor
import matplotlib.pyplot as plt
import numpy as np

#fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
t = np.arange(0.0, 2.0, 0.01)
#ax1.plot(t, np.sin(2*np.pi*t))
#ax2.plot(t, np.sin(4*np.pi*t))
#multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1, horizOn=False, vertOn=True)

fig = plt.figure(figsize=(19, 9.8))

#set the size of subplots
left = 0.14
width = 0.77
bottom = 0.11 
height = 0.5
bottom_h= bottom + height + 0.04

rect_line1=[left,bottom,width,height]
rect_line2=[left,bottom_h,width,0.3]

axbelow=plt.axes(rect_line1)
axupper=plt.axes(rect_line2)

plot1=axbelow.plot(t,np.sin(2*np.pi*t),'-ob',ms=1)
plot2=axupper.plot(t,np.sin(2*np.pi*t),'-og',ms=1)

plt.show()
