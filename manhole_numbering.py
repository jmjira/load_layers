#interceptor = 'EA'
#branch = 'H'
#sub_branch = 'A'
#number_of_nodes = 5


def make_manhole_list(interceptor, branch, sub_branch, number_of_nodes):
    last_manhole = (number_of_nodes * 6)
    manhole_list = []
    manhole_number = range(5, last_manhole, 5)
    for node in manhole_number:
        manhole_list.append(interceptor + branch + \
        sub_branch + str(node).zfill(4))
    manhole_list.reverse()
    return manhole_list

manhole_list = make_manhole_list('EA','H','A',5)

import networkx as nx
G = nx.DiGraph()

node_list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
edge_list = [((1,2),(3,4)),((3,4),(5,6)),((5,6),(7,8)),((7,8),(9,10))]

G.add_nodes_from(node_list)
G.add_edges_from(edge_list)

# topoligical sort will sort through nodes and return from starting node
# to ending node ( or from upstream manhole to downstream manhole)

toplogical_node_list = nx.topological_sort(G)

manhole_number = dict(zip(toplogical_manhole_list, manhole_list))


