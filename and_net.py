from lif_neuron import lif_neuron
from lif_connection import lif_connection

class and_net:

    def __init__(self, neurons, connections):
   
        self.neurons = [] # A list of lif_neuron objects
        self.connections = [] # A list of lif_connection objects

    # Function calculates current from an array of spikes from a neuron's output activity
    def spikes_to_current(self, a_spikes, conversion_factor):

        spike_count = 0
        for i in range(len(a_spikes)):
            if a_spikes[i] == 1:
                spike_count += 1
        
        spikes_per_second = spike_count / len(a_spikes)

        return spikes_per_second * conversion_factor * 100000

    # Configure the network to solve problem 3
    def create_simple_net(self):

        input_neuron_x = lif_neuron(id="input_neuron_x")
        input_neuron_y = lif_neuron(id="input_neuron_y")
        teach_neuron = lif_neuron(id="teach_neuron")
        output_neuron = lif_neuron(id="output_neuron")
        
        x_to_output = lif_connection(start=input_neuron_x, end=output_neuron, weight=1, id="x_to_output")
        y_to_output = lif_connection(start=input_neuron_y, end=output_neuron, weight=1, id="y_to_output")
        teach_to_output = lif_connection(start=teach_neuron, end=output_neuron, weight=1, id="teach_to_output")

        self.neurons = [input_neuron_x, input_neuron_y, teach_neuron, output_neuron]
        self.connections = [x_to_output, y_to_output, teach_to_output]

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
    
    # Converts a single bit into 1000 ms array of spikes
    # A value of 0 makes 5Hz spikes
    # A value of 1 makes 15Hz spikes
    def binary_to_spikes(self, val, nsteps=1000):

        a_spikes = [0] * nsteps
        nspikes = 5

        if(val == 1):
            nspikes = 15

        interval = int(nsteps / nspikes)
        for i in range(1000):
            if(i % interval == 0):
                a_spikes[i] = 1

        return a_spikes
    
    # Runs the neural net
    # Maybe include option to run without training neuron
    def run_net(self, input):
        # Initializes a current for the three input neurons
        xIn = self.spikes_to_current(self.binary_to_spikes(input[0]), self.connections[0].weight)
        yIn = self.spikes_to_current(self.binary_to_spikes(input[1]), self.connections[1].weight)
        # Change and to xor/or
        teachIn = self.spikes_to_current(self.binary_to_spikes(input[1] and input[0]), self.connections[2].weight)
        self.neurons[0].sim(xIn, 1000)
        self.neurons[1].sim(yIn, 1000)
        self.neurons[2].sim(teachIn, 1000)
        # Calculates the input current for the output by using an or function on all 3 spike outputs 
        outIn = []
        for i in range(1000):
            outIn.append(self.neurons[0].output[i] or self.neurons[1].output[i] or self.neurons[2].output[i])
        self.neurons[3].sim(self.spikes_to_current(outIn, 1), 1000)
        output = 0
        for i in range(1000):
            output = output + self.neurons[3].output[i]
        if output > 5:
            return 1
        else:
            return 0