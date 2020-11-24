from and_net import and_net
net = and_net([], [])
net.create_simple_net()
# X at [0], Y at [1], Teacher at [2]
net.connections[0].weight = 1
net.connections[1].weight = 1
net.connections[2].weight = 1
# data[0] holds X, data[1] holds Y, output calculated by data[0][i] && data[1][i]
data = [[]]
lines = open(input("Enter Filepath: "), "r").readlines()
runs = len(lines)
for i in range(runs):
    for j in range(2):
        if lines[i][j] == '0':
            data[j][i] = 0
        else:
            data[j][i] = 1
# Trains the network
for i in range(runs):
    #out = net.run_net([data[0][i], data[1][i], data[0][i] and data[1][i]])
    #TODO Find better formula
    for i in range(1000):
        for j in range(2):
            if net.neurons[j].output[i] == net.neurons[3].output[i] == 1:
                #increase
                net.connections[j].weight += .1
            elif net.neurons[j].output[i] == 1 and net.neurons[3].output[i] == 0:
                #decrease
                net.connections[j].weight -= .1
    for i in range(3):
        net.neurons[i].clear