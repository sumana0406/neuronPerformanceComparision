Benchmarking Spiking Neuron Models: LIF vs Izhikevich

This mini-project compares two widely used spiking neuron models:

Leaky Integrate-and-Fire (LIF) :  low-cost, efficient model

Izhikevich Neuron : biologically realistic and expressive

Both models were implemented and simulated using Brian2, with execution time and spike behavior analyzed on identical runs.


Objective

To evaluate the trade-off between computational efficiency and biological accuracy in single-neuron models, relevant to spiking neural networks and neuromorphic hardware design.


Results Summary

Model	                      Biological Accuracy	         Computation Time	          Notes
LIF	Basic spiking;          no bursting	                 ~0.130 seconds	            Fast and hardware-efficient
Izhikevich	                Rich dynamics: spiking       ~0.151 seconds             More realistic but slower
                                          -bursting
                                          -adaptation		

<img width="1253" height="575" alt="image" src="https://github.com/user-attachments/assets/89ceabc4-555a-4f1c-8ea7-6dd8bd3d0bde" />


Observation

LIF demonstrated ~14–16% faster simulation performance under identical stimulus conditions.


Code

The core benchmarking script is located in main.py. It performs:

- Model definition
- Simulation
- Timing measurements
- Spike data visualization


Dependencies

To reproduce results, install:

pip install brian2 numpy matplotlib


Running the Simulation

python main.py


Interpretation

- LIF is better suited for large-scale neuromorphic systems requiring minimal cost per neuron.
- Izhikevich is preferable for modeling biologically realistic dynamics and neural diversity.
- Choice depends on application: scalability vs realism.


Future Work

- Add synaptic connections and population-level dynamics
    - <img width="1250" height="573" alt="image" src="https://github.com/user-attachments/assets/8b7549a6-df89-41ff-a251-1c25ad119c91" />
    - <img width="1248" height="573" alt="image" src="https://github.com/user-attachments/assets/3741e41a-e5f3-42cb-8da0-e5d16078c308" />
    - Performance difference:
      - Execution Time (10,000 neurons):
      - LIF:        0.8012 seconds
      - Izhikevich: 1.2119 seconds
      - 1.2119 / 0.8012 ~ 1.51 -> LIF is 51% faster than Izhikevich.
      
- Extend benchmarks under varying current inputs
- Evaluate energy cost in neuromorphic hardware simulators

