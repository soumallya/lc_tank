from __future__ import division
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy
from LC_tank_both import voltage,voltage_derivative,response

# This is the main program just for creating plots.

t = numpy.array(range(0,3000,1))
t = t/100


# Initilizing different component values for the first case. L in Henry. C in Farad. R11 (ESR of inductor) in ohm. R12 (ESR of capacitor) in ohm.
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
    Gain1.append(gain)

plt.figure(1)
plt.plot(frequency,Gain1)
plt.xlabel('Frequency in rad/sec')
plt.ylabel('Gain')
plt.savefig('Frequency_response_without_any_resistance.png')

R21 = 1    # The ESR values for the second case. L and C are smae as above.
R22 = 0

Gain2 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R21,R22,C,t)
    Gain2.append(gain)

plt.figure(2)
plt.plot(frequency,Gain2)
plt.xlabel('Frequency in rad/sec')
plt.ylabel('Gain')
plt.savefig('Frequency_response_with_only_inductor_resistance_1.png')

R31 = 0   # ESR values for the third case with same L and C value.
R32 = 1

Gain3 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R31,R32,C,t)
    Gain3.append(gain)

plt.figure(3)
plt.plot(frequency,Gain3)
plt.xlabel('Frequency in rad/sec')
plt.ylabel('Gain')
plt.savefig('Frequency_response_with_only_capacitor_resistance_1.png')

R41 = 1 # The fourth case.
R42 = 1

Gain4 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R41,R42,C,t)
    Gain4.append(gain)

plt.figure(4)
plt.plot(frequency,Gain4)
plt.xlabel('Frequency in rad/sec')
plt.ylabel('Gain')
plt.savefig('Frequency_response_with_both_resistance_1.png')

R51 = 0.5  # The fifth case
R52 = 1

Gain5 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R51,R52,C,t)
    Gain5.append(gain)

plt.figure(5)
plt.plot(frequency,Gain5)
plt.xlabel('Frequency in rad/sec')
plt.ylabel('Gain')
plt.savefig('Frequency_response_with_inductor_resistance_less_than_capacitor_resistance.png')

R61 = 1    # The sixth case.
R62 = 0.5

Gain6 = []
for w in frequency:
    i,V,t,gain = response(A,w,L,R61,R62,C,t)
    Gain6.append(gain)

plt.figure(6)
plt.plot(frequency,Gain6)
plt.xlabel('Frequency in rad/sec')
plt.ylabel('Gain')
plt.savefig('Frequency_response_with_inductor_resistance_greater_than_capacitor_resistance.png')

# This function is just for plotting voltage waveforms and corresponding current waveforms for particular LC tank circuit. A is the amplitude of the input voltage in volts. w is the angular frequency of the voltage in rad/sec. L is the inductor vaule in Henry. C is the cpacitor 
def current_vs_voltage_plot(A,w,L,R1,R2,C,t,figure_index):
    i,V,t,gain = response(A,w,L,R1,R2,C,t)
    plt.figure(figure_index)
    plt.plot(t,V,'-',linewidth = 1)
    plt.plot(t,i,'.',linewidth = 1)
    plt.xlabel('Time in seconds')
    plt.ylabel('Current in Ampere and Voltage in Volts')
    plt.legend(['Voltage','Current'])
    plt.savefig('Voltage_and_Current_vs_time_at_frequency_omega_'+str(w)+'_with_both_resistance_'+str(R1)+'.png')
    return

t = numpy.array(range(0,300,1))   # Initializing all values for showing the plots.
t = t/10
w_dash = 1
L_dash = 0.5
R1 = 0
R2 = 0
C_dash = 0.5

current_vs_voltage_plot(A,w_dash,L_dash,R1,R2,C_dash,t,7)


R1_dash = 1
R2_dash = 1

current_vs_voltage_plot(A,w_dash,L_dash,R1_dash,R2_dash,C_dash,t,8)

