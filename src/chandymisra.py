import pytest, sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


import json
import os
import numpy as np
import pandas as pd
import argparse
from config.constants import DEFAULTPATH, DEFAULTSITE
import matplotlib.pyplot as plt
import networkx as nx


class ChandyMisra:

    def __init__(self):
        self.data = 0

    def readGraph(self, path):
        self.data = pd.read_csv(path, header=None)
        return self.data.to_numpy()

    def showgraph(self):
        G = nx.from_pandas_adjacency(self.data)
        G.name = "Network"
        print(nx.info(G))
        nx.draw(G)

    def show_graph_with_labels(self, mylabels):
        adjacency_matrix = self.data.to_numpy()
        mylabels = self.data.columns
        
        rows, cols = np.where(adjacency_matrix == 1)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        gr.add_edges_from(edges)
        nx.draw(gr, node_size=500, labels=None, with_labels=False)
        plt.show()
 

def probe(data, init, k, visited):

    if k+1 in visited:
        print("Deadlock detected!! Node {} visited again!".format(k+1))
        sys.exit()

    visited.append(k+1)
    for x in range(data.shape[1]):
        if data[k][x] == 1:
            if init == x:
                print("init {}  start {}  ---->  end {}".format(init+1, k+1, x+1))
                print("Deadlock detected!! Node {} visited again!".format(init+1))
                sys.exit()
            print("init {}  start {}  ---->  end {}".format(init+1, k+1, x+1))
            return probe(data, init, x,visited)
    print("There is No Deadlock detected!!")

# This function parses command line arguments
def parseargs():
    parser = argparse.ArgumentParser(description='Parse inp parameters.')
    parser.add_argument('-path', action="store", dest='path')
    parser.add_argument('-initsite', action="store", dest='initsite')
    return parser.parse_args()


# Validate the command line arguments
def validateargs(parseargs):

#   validate input site file path    
    if os.path.exists(parseargs.path) == True:
        path = parseargs.path
    else:
        print("Not a valid input path, reading from default location {}".format(DEFAULTPATH))
        path = DEFAULTPATH

    if parseargs.initsite == None:
        with open('path_to_file/person.json') as f:
            data = json.load(DEFAULTSITE)
        initsite = data['init']
    else:
        initsite = parseargs.initsite

    return path, int(initsite)
     
def main():
    args = parseargs()
    path, init = validateargs(args)

    cm = ChandyMisra()
    graph = cm.readGraph(path)

    if init > graph.shape[0]:
        print("Initiator node s{} not in the network".format(str(init)))
        print("Provide a valid initiator. Exiting!!!")
        sys.exit()


    j = init - 1
    visited = []
    visited.append(init)
    for k in range(graph.shape[1]):
        if graph[j][k] == 1:
            print("init {}  start {}  ---->  end {}".format(init, j+1, k+1))
            #probe(graph, k, k)
            probe(graph, j, k, visited)



if __name__ == "__main__":
    main()



