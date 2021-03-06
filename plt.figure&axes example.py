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
left = 0.03
width = 0.95
bottom = 0.04
height = 0.25
bottom_h = bottom + height + 0.04 #  0.11+0.5+0.04=0.65
print(bottom_h)

rect_line1 = [left,bottom,width,0.25] #  below parameter
rect_line2 = [left,bottom_h,width,0.65]#  upper parameter

axbelow = plt.axes(rect_line1) #  below ax
axupper = plt.axes(rect_line2) #  upper ax

plot1 = axbelow.plot(t,np.sin(2*np.pi*t),'-ob',ms=1)
plot2 = axupper.plot(t,np.sin(2*np.pi*t),'-og',ms=1)

plt.show()
