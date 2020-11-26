from and_net import and_net
net = and_net([], [])
net.create_simple_net()
# X at [0], Y at [1], Teacher at [2]
net.connections[0].weight = 1
net.connections[1].weight = 1
net.connections[2].weight = 1
# data[0] holds X, data[1] holds Y, output calculated by data[0][i] && data[1][i]
data = []
#lines = open(input("Enter Filepath: "), "r").readlines()
lines = open("data.txt", "r").readlines()
runs = len(lines)
for i in range(runs):
    temp = []
    for j in range(2):
        if lines[i][j] == '0':
            temp.append(0)
        else:
            temp.append(1)
    data.append(temp)

# Trains the network
for r in range(runs):
    net.run_net(data[r])
    #TODO Find better formula
    for i in range(1000):
        for j in range(2):
            if net.neurons[j].output[i] == net.neurons[3].output[i] == 1:
                #increase
                net.connections[j].weight += .1
            elif net.neurons[j].output[i] == 1 and net.neurons[3].output[i] == 0:
                #decrease
                if(net.connections[j].weight != 0):
                    net.connections[j].weight -= .1
    print((data[r][0] and data[r][1]), "||", net.spikes_to_binary(net.neurons[3]), "\n")
    x_spikes = sum(net.neurons[0].output)
    y_spikes = sum(net.neurons[1].output)
    o_spikes = sum(net.neurons[3].output)
    print("X =", net.connections[0].weight, x_spikes, "\nY =", net.connections[1].weight, y_spikes, "\n", o_spikes)
    for i in range(3):
        net.neurons[i].clear