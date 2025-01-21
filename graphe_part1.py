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


g_low_20.plot3D()
g_avg_20.plot3D()
g_high_20.plot3D()

g_low_40.plot3D()
g_avg_40.plot3D()
g_high_40.plot3D()

g_low_60.plot3D()
g_avg_60.plot3D()
g_high_60.plot3D()

plt.show()