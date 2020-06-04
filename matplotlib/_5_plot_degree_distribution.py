from graph_from_txt import read_graph
from matplotlib import pyplot

def degree_distribution(network):
    """Return the degree distribution as a dict."""
    degree_distribution = {}
    for node in network:
        degree = len(network[node])
        if degree in degree_distribution:
            degree_distribution[degree] += 1
        else:
            degree_distribution[degree] = 1
    n = len(network)
    for d in degree_distribution:
        degree_distribution[d] /= n
    return degree_distribution

def plot_degree_dist(network):
    """Uses pyplot to plot network's degree distribution."""
    deg_dist = degree_distribution(network)
    degree = list(deg_dist.keys())
    frequency = list(deg_dist.values())
    for d in deg_dist:
        degree.append(d)
        frequency.append(deg_dist[d])
    pyplot.scatter(degree, frequency)
##    pyplot.plot(degree, frequency)
    pyplot.xlabel('Degree')
    pyplot.ylabel('Fraction of nodes')
    pyplot.xlim(0, max(degree) + 10)
    pyplot.show()

##filename = 'clusters.txt'
filename = 'facebook_combined.txt'
network = read_graph(filename)

plot_degree_dist(network)
