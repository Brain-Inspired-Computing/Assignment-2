# Assignment-2

## Structure

### and_net.py

Structure:

This network is a graph of neurons, with weights between the edges.

- self.neurons: A list of lif_neuron objects
- self.connections: A list of lif_connection objects

Important functions:

- and_net.create_simple_net(): sets the network to have the three-node setup described in problem 3
- and_net.spikes_to_current(neuron, conversion_factor): calculates an average output current based on the frequency of output spikes from a given neuron. Conversion factor is multiplied by spike frequency for current output.
- and_net.spikes_to_binary(neuron, threshold): checks if the given neuron is spiking at or above the threshold frequency. If so, return 1, else return 0.

### lif_connection.py

Structure:

- self.start: the first neuron in the connection
- self.end: the second neuron in the connection
- self.weight: the weight of the connection
- self.id: a string to identify the connection

### lif_neuron.py

Structure:

There are three arrays, with the index corresponding to time. For example, self.potential[1500] will get the neuron's potential at 1.5 seconds.

- self.input: a current coming into the neuron
- self.potential: the current potential of the neuron
- self.output: 1 if there's a spike, 0 otherwise

Also has:

- self.id: a string to identify the neuron (optional)

Important functions:

- lif_neuron.sim(current, time): appends to the three arrays [time] times, calculating potential and output with a constant input equal to to [current].
- lif_neuron.clear(): deletes the contents of the three arrays.