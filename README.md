# Assignment-2

## Structure

### training.py

Structure:

This file trains the network.

To change the logical funtion that the network trains, change lines 10-12 based on the values on lines 7-9.
In and_net, the values on lines 84 and 92 must also be changed based on the values on lines 83 and 89-91 respectively.

This file reads in a series of two bit lines from data.txt as input data and runs the network for every line of bits
based on inital weights. Based on the spiking results of the network the weights will be changed as more data is
processed.

### and_net.py

Structure:

This network is a graph of neurons, with weights between the edges.

- self.neurons: A list of lif_neuron objects
- self.connections: A list of lif_connection objects

Important functions:

- and_net.create_simple_net(): sets the network to have the three-node setup described in problem 3
- and_net.spikes_to_current(neuron, conversion_factor): calculates an average output current based on the frequency of
output spikes from a given neuron. Conversion factor is multiplied by spike frequency for current output.
- and_net.spikes_to_binary(neuron, threshold): checks if the given neuron is spiking at or above the threshold
frequency. If so, return 1, else return 0.
- and_net.binary_to_spikes(self, val, nsteps=run_time): returns an array, the same length as the run time, of spikes
based on whether the input bit is a 1 or a 0. For a 1, the array will have more spikes, for a 0 the array will have less.
- and_net.run_net(self, input, time = run_time): Runs the nueral net on a pair of given bits and fills the output arrays
of the neurons. The function combines the spiking outputs of the input nuerons using a logical operator, converts those
spikes into a current using spikes_to_current, and feeds it to the output neuron.

### lif_connection.py

Structure:

- self.start: the first neuron in the connection
- self.end: the second neuron in the connection
- self.weight: the weight of the connection
- self.id: a string to identify the connection

### lif_neuron.py

Structure:

There are three arrays, with the index corresponding to time. For example, self.potential[1500] will get the neuron's
potential at 1.5 seconds.

- self.input: a current coming into the neuron
- self.potential: the current potential of the neuron
- self.output: 1 if there's a spike, 0 otherwise

Also has:

- self.id: a string to identify the neuron (optional)

Important functions:

- lif_neuron.sim(current, time): appends to the three arrays [time] times, calculating potential and output with a
constant input equal to to [current].
- lif_neuron.clear(): deletes the contents of the three arrays.