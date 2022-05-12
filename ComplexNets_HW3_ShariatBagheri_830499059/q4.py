import os
import snap


graph = snap.LoadEdgeList(snap.TNGraph, "Wiki-Vote.txt", 0, 1)
# A:
print('#Nodes: {NODES}\n#Edges: {EDGES}'.format(NODES=graph.GetNodes(), EDGES=graph.GetEdges()))

# B:
print('#Directed Edges: {}'.format(graph.CntUniqDirEdges()))
print('#UnDirected Edges: {}'.format(graph.CntUniqUndirEdges()))

# C:
print('#In-Degree Nodes: {}'.format(graph.CntInDegNodes(0)))
print('#Out-Degree Nodes: {}'.format(graph.CntOutDegNodes(0)))

# D:
print('#Cluster Coefficient: {:.5f}'.format(graph.GetClustCf()))

# E:
print('Diameter of Network: {}'.format(graph.GetBfsFullDiam(100)))

# F:
print('#Triads: {}'.format(graph.GetTriads()))

# G:
ComponentDist = graph.GetWccs()
print('#Weak Connected Components: {}'.format(len(ComponentDist)))
# for comp in ComponentDist:
#     print('Size: {}'.format(comp.Len()))

# H:
MxScc = graph.GetMxScc()
counter = 0
for node in MxScc.Nodes():
    counter += 1
print('#Nodes in MxScc: {}'.format(counter))

# I:
if os.path.exists("InDegreeDistribution.plt"):
	os.remove('InDegreeDistribution*')
if os.path.exists("OutDegreeDistribution.plt"):
	os.remove('OutDegreeDistribution*')
graph.PlotInDegDistr('InDegreeDistribution', 'Undirected graph - in-degree Distribution')
graph.PlotOutDegDistr('OutDegreeDistribution', 'Undirected graph - out-degree Distribution')
