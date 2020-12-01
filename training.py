from and_net import and_net
#import matplotlib.pyplot as plt

net = and_net([], [])
net.create_simple_net()
# X at [0], Y at [1], Teacher at [2]
net.connections[0].weight = .6
net.connections[1].weight = .4
net.connections[2].weight = 1
# data[0] holds X, data[1] holds Y, output calculated by data[0][i] && data[1][i]
data = []
i = 0
j = 0
k = 0

"""
def raster_plot(net):
    plt.figure()
    plt.title('Raster plot for network activity')

    plt.subplot(3, 1, 1)
    plt.xlabel('Time')
    plt.ylabel('Input Neuron 1')
    for i in range(1000):
        if net.neurons[0].output[i] == 1:
            #fmt = '[|][-][k]'
            #plt.plot(fmt)
            plt.axvline(i)

    plt.subplot(3, 1, 2)
    plt.xlabel('Time')
    plt.ylabel('Input Neuron 2')
    for j in range(1000):
        if net.neurons[1].output[j] == 1:
            #fmt = '[|][-][k]'
            #plt.plot(fmt)
            plt.axvline(j)

    plt.subplot(3, 1, 3)
    plt.xlabel('Time')
    plt.ylabel('Output Neuron')
    for k in range(1000):
        if net.neurons[3].output[k] == 1:
            #fmt = '[|][-][k]'
            #plt.plot(fmt)
            plt.axvline(k)

    plt.show()
"""

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
    time = len(net.neurons[0].output)
    w_max = 1
    for i in range(int(time/100)-1):
        #Finds rate for each neuron in a time step of 100
        v_x = sum(net.neurons[0].output[100*i:100*(i+1)])
        v_y = sum(net.neurons[1].output[100*i:100*(i+1)])
        v_o = sum(net.neurons[3].output[100*i:100*(i+1)])
        #Sets a_corr value
        a_corr_x = w_max - net.connections[0].weight
        a_corr_y = w_max - net.connections[1].weight
        #If the rate is below 5, set value to 0
        if v_x <= 5:
            v_x = 0
        if v_y <= 5:
            v_y = 0
        if v_y <= 5:
            v_y = 0
        #Hebb with postsynaptic LTP/LTD threshold
        #TODO change .01 to something else?
        net.connections[0].weight += a_corr_x * v_x * (v_o - .01)
        net.connections[1].weight += a_corr_y * v_y * (v_o - .01)
    print((data[r][0] and data[r][1]), "||", net.spikes_to_binary(net.neurons[3]), "\n")
    x_spikes = sum(net.neurons[0].output)
    y_spikes = sum(net.neurons[1].output)
    o_spikes = sum(net.neurons[3].output)
    print("X =", net.connections[0].weight, x_spikes, "\nY =", net.connections[1].weight, y_spikes, "\n", o_spikes)
    for i in range(3):
        net.neurons[i].clear
#raster_plot(net)