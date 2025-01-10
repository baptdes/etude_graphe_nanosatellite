from essaim_nano import *

# Chemin des CSVs
csv_path_avg = 'Topologies-20250107/topology_avg.csv'
csv_path_high = 'Topologies-20250107/topology_high.csv'
csv_path_low = 'Topologies-20250107/topology_low.csv'

g = graph_essaim("topology_low_20",csv_path_low,20000)
#g.plot3D()
print("Degré moyen : ", g.get_avg_degree())
#g.plot_degree_distribution()
print("Average clustering : ", g.get_avg_clustering())
#g.plot_clustering_distribution()
print("nombre de cliques : ", g.get_nb_cliques())
#g.plot_orders_cliques_distribution()
print("Nombre de composantes connexes : ", g.get_nb_connected_components())
#g.get_orders_connected_components()
#55
g.plot_PPC_distribution(55)