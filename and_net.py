from lif_neuron import lif_neuron
from lif_connection import lif_connection

class and_net:

    def __init__(self, neurons, connections):
   
        self.neurons = [] # A list of lif_neuron objects
        self.connections = [] # A list of lif_connection objects

    # Function calculates current from neuron's output activity
    def spikes_to_current(self, neuron, conversion_factor):

        spike_count = 0
        for i in range(len(neuron.output)):
            if neuron.output[i] == 1:
                spike_count += 1
        
        spikes_per_second = spike_count / (len(neuron.output) / neuron.time_step)

        return spikes_per_second * conversion_factor

    # Configure the network to solve problem 3
    def create_simple_net(self):

        input_neuron_x = lif_neuron(id="input_neuron_x")
        input_neuron_y = lif_neuron(id="input_neuron_y")
        output_neuron = lif_neuron(id="output_neuron")
        
        x_to_output = lif_connection(start=input_neuron_x, end=output_neuron, weight=1, id="x_to_output")
        y_to_output = lif_connection(start=input_neuron_y, end=output_neuron, weight=1, id="y_to_output")

        self.neurons = [input_neuron_x, input_neuron_y, output_neuron]
        self.connections = [x_to_output, y_to_output]

        return

    # Prepare an output of 1 or 0 based on the spike frequency of the output neuron
    def spikes_to_binary(self, output_neuron, threshold=4):
        
        spike_count = 0
        for i in range(len(output_neuron.output)):
            if output_neuron.output[i] == 1:
                spike_count += 1

        spike_frequency = spike_count / len(output_neuron.output)

        if(spike_frequency > threshold):
            return 1

        return 0

    # TODO
    def learn_idk(self):
        pass