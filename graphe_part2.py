from essaim_nano import *
import matplotlib.pyplot as plt

# Chemin des CSVs
csv_path_avg = 'Topologies-20250107/topology_avg.csv'
csv_path_high = 'Topologies-20250107/topology_high.csv'
csv_path_low = 'Topologies-20250107/topology_low.csv'

#creation des graphes
g_low_20 = graph_essaim("topology_low_20",csv_path_low,20000,False)
g_avg_20 = graph_essaim("topology_avg_20",csv_path_avg,20000,False)
g_high_20 =  graph_essaim("topology_high_20",csv_path_high,20000,False)

g_low_40 = graph_essaim("topology_low_40",csv_path_low,40000,False)
g_avg_40 = graph_essaim("topology_avg_40",csv_path_avg,40000,False)
g_high_40 =  graph_essaim("topology_high_40",csv_path_high,40000,False)

g_low_60 = graph_essaim("topology_low_60",csv_path_low,60000,False)
g_avg_60 = graph_essaim("topology_avg_60",csv_path_avg,60000,False)
g_high_60 =  graph_essaim("topology_high_60",csv_path_high,60000,False)


# affichage des degré moyen et de la distribution des degrés
"""
print("Degré moyen : ", g_low_20.get_avg_degree())
g_low_20.plot_degree_distribution()
print("Degré moyen : ", g_avg_20.get_avg_degree())
g_avg_20.plot_degree_distribution()
print("Degré moyen : ", g_high_20.get_avg_degree())
g_high_20.plot_degree_distribution()
print("Degré moyen : ", g_low_40.get_avg_degree())
g_low_40.plot_degree_distribution()
print("Degré moyen : ", g_avg_40.get_avg_degree())
g_avg_40.plot_degree_distribution()
print("Degré moyen : ", g_high_40.get_avg_degree())
g_high_40.plot_degree_distribution()
print("Degré moyen : ", g_low_60.get_avg_degree())
g_low_60.plot_degree_distribution()
print("Degré moyen : ", g_avg_60.get_avg_degree())
g_avg_60.plot_degree_distribution()
print("Degré moyen : ", g_high_60.get_avg_degree())
g_high_60.plot_degree_distribution()
"""



#affichage des cliques et odres
"""
print("nombre de cliques : ", g_low_20.get_nb_cliques())
g_low_20.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_avg_20.get_nb_cliques())
g_avg_20.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_high_20.get_nb_cliques())
g_high_20.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_low_40.get_nb_cliques())
g_low_40.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_avg_40.get_nb_cliques())
g_avg_40.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_high_40.get_nb_cliques())
g_high_40.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_low_60.get_nb_cliques())
g_low_60.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_avg_60.get_nb_cliques())
g_avg_60.plot_orders_cliques_distribution()
print("nombre de cliques : ", g_high_60.get_nb_cliques())
g_high_60.plot_orders_cliques_distribution()
"""


#affichage des composantes connexes et ordres
"""
print("Nombre de composantes connexes : ", g_low_20.get_nb_connected_components())
g_low_20.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_avg_20.get_nb_connected_components())
g_avg_20.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_high_20.get_nb_connected_components())
g_high_20.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_low_40.get_nb_connected_components())
g_low_40.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_avg_40.get_nb_connected_components())
g_avg_40.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_high_40.get_nb_connected_components())
g_high_40.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_low_60.get_nb_connected_components())
g_low_60.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_avg_60.get_nb_connected_components())
g_avg_60.plot_orders_connected_components()
print("Nombre de composantes connexes : ", g_high_60.get_nb_connected_components())
g_high_60.plot_orders_connected_components()
"""

#affichage clustering moyen et distribution
"""
print("Average clustering : ", g_low_20.get_avg_clustering())
g_low_20.plot_clustering_distribution()
print("Average clustering : ", g_avg_20.get_avg_clustering())
g_avg_20.plot_clustering_distribution()
print("Average clustering : ", g_high_20.get_avg_clustering())
g_high_20.plot_clustering_distribution()
print("Average clustering : ", g_low_40.get_avg_clustering())
g_low_40.plot_clustering_distribution()
print("Average clustering : ", g_avg_40.get_avg_clustering())
g_avg_40.plot_clustering_distribution()
print("Average clustering : ", g_high_40.get_avg_clustering())
g_high_40.plot_clustering_distribution()
print("Average clustering : ", g_low_60.get_avg_clustering())
g_low_60.plot_clustering_distribution()
print("Average clustering : ", g_avg_60.get_avg_clustering())
g_avg_60.plot_clustering_distribution()
print("Average clustering : ", g_high_60.get_avg_clustering())
g_high_60.plot_clustering_distribution()
"""

#chemin les plus courts à partir du point non centrale ou sur les bords 55
g_low_20.plot_PPC_distribution(55)
g_avg_20.plot_PPC_distribution(55)
g_high_20.plot_PPC_distribution(55)
g_low_40.plot_PPC_distribution(55)
g_avg_40.plot_PPC_distribution(55)
g_high_40.plot_PPC_distribution(55)
g_low_60.plot_PPC_distribution(55)
g_avg_60.plot_PPC_distribution(55)
g_high_60.plot_PPC_distribution(55)