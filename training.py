from and_net import and_net
net = and_net([], [])
net.create_simple_net()
# X at [0], Y at [1], Teacher at [2]
net.connections[0].weight = .7
net.connections[1].weight = .3
net.connections[2].weight = .5
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
#TODO does training and results and_net with proper weights
for i in range(runs):
    pass