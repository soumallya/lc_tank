from __future__ import division
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from matplotlib import animation
from IPython.display import HTML
import numpy
from LC_tank_both import voltage,voltage_derivative,response

# This program is just for creating animation. This code will create the animations as .mp4 files for all the corresponding plots of main.py

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
plt.title('Voltage and current vs time Roll: 153070018')
plt.xlabel('Time in seconds')
plt.ylabel('Current in Ampere and Voltage in Volts')
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,5), ylim=(-5, 5))
line, = ax.plot([], [],'-', lw=2,label = 'Voltage')
line2, = ax.plot([], [],'.', lw=2,label = 'Current')
plt.legend(handles=[line, line2])

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    return line, line2,

A = 1
w_dash = 1
L_dash = 0.5
R1 = 0
R2 = 0
C_dash = 0.5

t = numpy.array(range(0,300,1))
t = t/10
i1,V,t,gain = response(A,w_dash,L_dash,R1,R2,C_dash,t)
# animation function.  This is called sequentially
def animate(i):
    line.set_data(t-0.1*i,V)
    line2.set_data(t-0.1*i,i1)
    return line,line2

# call the animator.  blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit= False)

ani.save('movie1.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

A = 1
w_dash = 1
L_dash = 0.5
R1 = 1
R2 = 1
C_dash = 0.5

t = numpy.array(range(0,300,1))
t = t/10
i1,V,t,gain = response(A,w_dash,L_dash,R1,R2,C_dash,t)
# animation function.  This is called sequentially
def animate(i):
    line.set_data(t-0.1*i,V)
    line2.set_data(t-0.1*i,i1)
    return line,line2

# call the animator.  blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit= False)

ani.save('movie2.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

#Gain vs frequency response when both inductor resistance and capacitor resistance are zero
t = numpy.array(range(0,30000,1))
t = t/1000

L = 0.5
R11 = 0
R12 = 0
C = 0.5
A = 1

frequency = numpy.array(range(1,100))
frequency = frequency/10
Gain1 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R11,R12,C,t)
    #print "Frequency = {},Gain = {}".format(w,gain)
    Gain1.append(gain)
    
fig1 = plt.figure()
plt.title('Gain vs frequency Roll: 153070018')
plt.ylabel('Gain')
plt.xlabel('Frequency in rad/sec')
ax = fig1.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0, 20))
ax.grid()
line, = ax.plot([], [], '-', lw=2)

def init():
    line.set_data([], [])
    return line,

thisx = []
thisy = []
def animate(i):
    thisx.append(frequency[i])
    thisy.append(Gain1[i])

    line.set_data(thisx, thisy)
    return line,

ani1 = animation.FuncAnimation(fig1, animate, numpy.arange(1, len(frequency)),
                              interval=25, blit=False, init_func=init)
ani1.save('movie3.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

# Gain vs frequency curve when inductor resistance is 1 ohm and capacitor resistance is zero

R21 = 1
R22 = 0

frequency = numpy.array(range(1,100))
frequency = frequency/10
Gain2 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R21,R22,C,t)
    #print "Frequency = {},Gain = {}".format(w,gain)
    Gain2.append(gain)
    
fig2 = plt.figure()
plt.title('Gain vs frequency Roll: 153070018')
plt.ylabel('Gain')
plt.xlabel('Frequency in rad/sec ')
ax = fig2.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0, 6))
ax.grid()
line, = ax.plot([], [], '-', lw=2)

def init():
    line.set_data([], [])
    return line,

thisx = []
thisy = []
def animate(i):
    thisx.append(frequency[i])
    thisy.append(Gain2[i])

    line.set_data(thisx, thisy)
    return line,

ani2 = animation.FuncAnimation(fig2, animate, numpy.arange(1, len(frequency)),
                              interval=25, blit=False, init_func=init)
ani2.save('movie4.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

# Gain vs frequency curve when the capacitor resistance is 1 ohm and inductor resistance is zero

R31 = 0
R32 = 1


Gain3 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R31,R32,C,t)
    #print "Frequency = {},Gain = {}".format(w,gain)
    Gain3.append(gain)
    
fig3 = plt.figure()
plt.title('Gain vs frequency Roll: 153070018')
plt.ylabel('Gain')
plt.xlabel('Frequency in rad/sec')
ax = fig3.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0, 10))
ax.grid()
line, = ax.plot([], [], '-', lw=2)

def init():
    line.set_data([], [])
    return line,

thisx = []
thisy = []
def animate(i):
    thisx.append(frequency[i])
    thisy.append(Gain3[i])

    line.set_data(thisx, thisy)
    return line,

ani3 = animation.FuncAnimation(fig3, animate, numpy.arange(1, len(frequency)),
                              interval=25, blit=False, init_func=init)
ani3.save('movie5.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

#Gain vs frequency curve when both of the resistances value are 1 ohm

R41 = 1
R42 = 1


Gain4 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R41,R42,C,t)
    #print "Frequency = {},Gain = {}".format(w,gain)
    Gain4.append(gain)
    
fig4 = plt.figure()
plt.title('Gain vs frequency Roll: 153070018')
plt.ylabel('Gain')
plt.xlabel('Frequency in rad/sec')
ax = fig4.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0, 2))
ax.grid()
line, = ax.plot([], [], '-', lw=2)

def init():
    line.set_data([], [])
    return line,

thisx = []
thisy = []
def animate(i):
    thisx.append(frequency[i])
    thisy.append(Gain4[i])

    line.set_data(thisx, thisy)
    return line,

ani4 = animation.FuncAnimation(fig4, animate, numpy.arange(1, len(frequency)),
                              interval=25, blit=False, init_func=init)
ani4.save('movie6.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

# Gain vs frequency curve when the inductor resistance is 1 ohm and capacitor resistance is 0.5 ohm

R51 = 1
R52 = 0.5


Gain5 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R51,R52,C,t)
    #print "Frequency = {},Gain = {}".format(w,gain)
    Gain5.append(gain)
    
fig5 = plt.figure()
plt.title('Gain vs frequency Roll: 153070018')
plt.ylabel('Gain')
plt.xlabel('Frequency in rad/sec')
ax = fig5.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0, 2))
ax.grid()
line, = ax.plot([], [], '-', lw=2)

def init():
    line.set_data([], [])
    return line,

thisx = []
thisy = []
def animate(i):
    thisx.append(frequency[i])
    thisy.append(Gain5[i])

    line.set_data(thisx, thisy)
    return line,

ani5 = animation.FuncAnimation(fig5, animate, numpy.arange(1, len(frequency)),
                              interval=25, blit=False, init_func=init)
ani5.save('movie7.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

# Gain vs frequency curve when the inductor resistance is 0.5 ohm and capacitor resistance is 1 ohm

R61 = 0.5
R62 = 1


Gain6 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R61,R62,C,t)
    #print "Frequency = {},Gain = {}".format(w,gain)
    Gain6.append(gain)
    
fig6 = plt.figure()
plt.title('Gain vs frequency Roll: 153070018')
plt.ylabel('Gain')
plt.xlabel('Frequency in rad/sec')
ax = fig6.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0, 2))
ax.grid()
line, = ax.plot([], [], '-', lw=2)

def init():
    line.set_data([], [])
    return line,

thisx = []
thisy = []
def animate(i):
    thisx.append(frequency[i])
    thisy.append(Gain6[i])

    line.set_data(thisx, thisy)
    return line,

ani6 = animation.FuncAnimation(fig6, animate, numpy.arange(1, len(frequency)),
                              interval=25, blit=False, init_func=init)
ani6.save('movie8.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
