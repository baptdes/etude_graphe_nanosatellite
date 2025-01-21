from essaim_nano import *
import matplotlib.pyplot as plt

# Chemin des CSVs
csv_path_avg = 'Topologies-20250107/topology_avg.csv'
csv_path_high = 'Topologies-20250107/topology_high.csv'
csv_path_low = 'Topologies-20250107/topology_low.csv'

#creation des graphes
g_low_60 = graph_essaim("topology_low_20",csv_path_low,20000,True)
g_avg_60 = graph_essaim("topology_avg_20",csv_path_avg,20000,True)
g_high_60 =  graph_essaim("topology_high_20",csv_path_high,20000,True)

g_low_60.plot_PPC_distribution(55)
g_avg_60.plot_PPC_distribution(55)
g_high_60.plot_PPC_distribution(55)
