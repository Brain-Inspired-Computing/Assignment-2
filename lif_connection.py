import lif_neuron

class lif_connection:

    def __init__(self, start, end, weight, id=""):
        
        self.start = start
        self.end = end
        self.weight = weight
        self.id = id

    def set_weight(self, new_weight):
        self.weight = new_weight
        return
