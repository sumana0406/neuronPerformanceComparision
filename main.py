from brian2 import *
import time

prefs.codegen.target = 'numpy'

duration = 500*ms

########################
# LIF MODEL
########################
start_lif = time.time()

tau = 10*ms
Vt = -50*mV
Vr = -65*mV

eqs_lif = '''
dV/dt = (-V)/tau : volt
'''

lif = NeuronGroup(1, eqs_lif, threshold='V>Vt', reset='V=Vr', method='euler')
lif.V = Vr
Mlif = StateMonitor(lif, 'V', record=True)
Slif = SpikeMonitor(lif)

net_lif = Network(lif, Mlif, Slif)
net_lif.run(duration)
lif_time = time.time() - start_lif

# IZHIKEVICH MODEL

start_izh = time.time()

eqs_izh = '''
dv/dt = (0.04*v**2 + 5*v + 140 - u)/ms : 1
du/dt = (0.02*(0.2*v - u))/ms : 1
'''

izh = NeuronGroup(1, eqs_izh, threshold='v>30', reset='v=-65; u+=8', method='euler')
izh.v = -70
izh.u = 0
Mizh = StateMonitor(izh, 'v', record=True)
Sizh = SpikeMonitor(izh)

net_izh = Network(izh, Mizh, Sizh)
net_izh.run(duration)
izh_time = time.time() - start_izh

# PRINT TIMES
print("\nExecution Time:")
print(f"LIF: {lif_time:.6f} seconds")
print(f"Izhikevich: {izh_time:.6f} seconds\n")

# PLOT RESULTS

figure(figsize=(10,4))
plot(Mlif.t/ms, Mlif.V[0]/mV)
title("LIF Membrane Potential")
xlabel("Time (ms)")
ylabel("Voltage (mV)")
show()

figure(figsize=(10,4))
plot(Mizh.t/ms, Mizh.v[0])
title("Izhikevich Membrane Potential")
xlabel("Time (ms)")
ylabel("Voltage (arbitrary units)")
show()
