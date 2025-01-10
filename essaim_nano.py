import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance(x,y):
    return np.sqrt((x[1]-y[1])**2 + (x[2]-y[2])**2 + (x[3]-y[3])**2)

def plot_3d_graph(G, title):
  pos = nx.get_node_attributes(G,'pos') #Récupération des positions

  node_xyz = np.array([pos[v] for v in sorted(G)])
  edge_xyz = np.array([(pos[u], pos[v]) for u, v in G.edges()])

  fig = plt.figure()
  ax = fig.add_subplot(111, projection="3d")

  ax.scatter(*node_xyz.T, s=100, ec="w")

  for vizedge in edge_xyz:
      ax.plot(*vizedge.T, color="tab:gray")

  for node, (x, y, z) in pos.items():
      ax.text(x, y, z, str(node), color='black', fontsize=8)

  ax.grid(False) # Turn gridlines off
  # Suppress tick labels
  for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
      dim.set_ticks([])
  # Set axes labels
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.set_zlabel("z")
  ax.set_title(title)
  fig.tight_layout()
  plt.show()

class graph_essaim:

    def __init__(self, title, path , detection):
        self.title = title
        self.path = path
        self.detection = detection
        self.import_graph()

    def import_graph(self):
        self.graph = nx.Graph()
        matrice = pd.read_csv(self.path).to_numpy()

        for i in range(len(matrice)):
            self.graph.add_node(int(matrice[i][0]),pos=(matrice[i][1],matrice[i][2],matrice[i][3]))

        for i in range(len(matrice)):
            for  j in range(len(matrice)):
                if i != j:
                    d = distance(matrice[i],matrice[j])
                    if d < self.detection:
                        self.graph.add_edge(int(matrice[i][0]),int(matrice[j][0]))
    
    def plot3D(self):
        plot_3d_graph(self.graph, self.title)

    def get_avg_degree(self):
        return sum(dict(self.graph.degree()).values()) / len(self.graph.nodes)
    
    def plot_degree_distribution(self):
        degree_sequence = [d for n, d in self.graph.degree()]

        plt.figure()
        plt.hist(degree_sequence, bins=range(min(degree_sequence), max(degree_sequence) + 2), color='tab:blue', edgecolor='black')

        # Titres et labels
        plt.title("Distribution du Degré", fontsize=16)
        plt.xlabel("Degré", fontsize=12)
        plt.ylabel("Nombre de nœuds", fontsize=12)

        # Affichage de l'histogramme
        plt.grid(True)
        plt.show()

    def get_avg_clustering(self):
        return sum(nx.clustering(self.graph).values()) / len(self.graph.nodes)

    def plot_clustering_distribution(self):
        clustering_sequence = list(nx.clustering(self.graph).values())

        plt.figure()
        plt.hist(clustering_sequence,bins = np.arange(0,1,0.1), color='tab:blue', edgecolor='black')

        # Titres et labels
        plt.title("Distribution du degré de clustering", fontsize=16)
        plt.xlabel("Degré de clustering", fontsize=12)
        plt.ylabel("Nombre de nœuds", fontsize=12)

        # Affichage de l'histogramme
        plt.grid(True)
        plt.show()

    def get_nb_cliques(self):
        return len(list(nx.enumerate_all_cliques(self.graph)))
    
    def get_orders_cliques_distribution(self):
        listCliques =  list(nx.enumerate_all_cliques(self.graph))
        orders = [len(l) for l in listCliques]
        plt.figure()
        plt.hist(orders, color='tab:blue', edgecolor='black')

        # Titres et labels
        plt.title("Distribution de l'ordre des cliques", fontsize=16)
        plt.xlabel("Ordre des cliques", fontsize=12)
        plt.ylabel("Nombre de nœuds", fontsize=12)

        # Affichage de l'histogramme
        plt.grid(True)
        plt.show()

    def get_nb_connected_components(self):
        return nx.number_connected_components(self.graph)
    
    def plot_orders_connected_components(self):
        listCliques =  list(nx.connected_components(self.graph))
        orders = [len(l) for l in listCliques]
        plt.figure()
        plt.hist(orders, color='tab:blue', edgecolor='black')

        # Titres et labels
        plt.title("Distribution de l'ordre des composantes connexes", fontsize=16)
        plt.xlabel("Ordre des composantes connexes", fontsize=12)
        plt.ylabel("Nombre de nœuds", fontsize=12)

        # Affichage de l'histogramme
        plt.grid(True)
        plt.show() 
    
    def get_list_PCC(self,point):
        listRest = []
        for i in range(1,100):
            try :
                if i !=point:
                    listRest.append(nx.shortest_path_length(self.graph,point,i))
            except :
                None
        return listRest

    def plot_PPC_distribution(self,point):
        listCliques = self.get_list_PCC(point)
        plt.figure()
        plt.hist(listCliques, color='tab:blue', edgecolor='black')

        # Titres et labels
        plt.title("Distribution des plus chemin du point "+str(point), fontsize=16)
        plt.xlabel("Nombre de chemins", fontsize=12)
        plt.ylabel("Nombre de nœuds", fontsize=12)

        # Affichage de l'histogramme
        plt.grid(True)
        plt.show() 