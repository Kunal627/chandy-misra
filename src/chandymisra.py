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
from config.constants import DEFAULTPATH, DEFAULTSITE, OUTPATH
import matplotlib.pyplot as plt
import networkx as nx


class ChandyMisra:

    def __init__(self):
        self.data = 0

    def readGraph(self, path):
        self.data = pd.read_csv(path, header=None)
        return self.data.to_numpy()

    def draw_graph(self):
        graph = [(j+1, i+1) for i in range(self.data.shape[0]) for j in range(self.data.shape[1]) if self.data[i][j] == 1]
        G = nx.DiGraph()
        G.add_edges_from(graph) 
        G.add_nodes_from([node + 1 for node in range(len(self.data[1]))])
        G.number_of_nodes()
        G.number_of_edges()
        fig = plt.figure()
        nx.draw(G, ax=fig.add_subplot(111), with_labels=True, font_weight='bold',connectionstyle='arc3, rad = 0.1')
        return fig

 

def probe(data, init, k, visited):

    if k+1 in visited:
        print("Deadlock detected!! Node {} visited again!  A cycle is found.".format(k+1))
        sys.exit()

    visited.append(k+1)
    for x in range(data.shape[1]):
        if data[k][x] == 1:
            if init == x:
                print("init {}  start {}  ---->  end {}".format(init+1, k+1, x+1))
                print("Deadlock detected!! Node {} visited again! A cycle is found.".format(init+1))
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
    
    # Instantiate the Chandy Misra class and read the adjacency matrix from file
    cm = ChandyMisra()
    graph = cm.readGraph(path)
    
    # save the network graph to out location
    fig = cm.draw_graph()
    fig.savefig(OUTPATH)

    # exit if the initiating site do not belong to the network
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
        visited = []
    



if __name__ == "__main__":
    main()



