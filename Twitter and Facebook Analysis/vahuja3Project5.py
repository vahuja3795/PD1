#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:51:53 2018

@author: varunahuja
"""

import matplotlib.pyplot as plt
import pandas
import networkx as nx
import numpy

'''Network/data analysis of a csv file containing data obtained from Twitter.'''
fileref = open('twitter_cleaned.csv',encoding='ISO-8859-1')

edge_data_0 = pandas.read_csv(fileref)
edge = edge_data_0.head()
file=open('vahuja3Project4.txt','a')
file.write(edge.to_string())
file.write('\n')

g = nx.Graph()
g.add_edges_from(edge_data_0.values)

file.write(str(g.number_of_edges()))
file.write('\n')
file.write(str(g.number_of_nodes()))

degree_data = pandas.Series(dict(nx.degree(g)))

plt.figure(1)
degree_data.plot(kind = 'hist')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title('Degree Distribution (no scaling)')

edge2 = degree_data.sort_values(ascending=False).head(10)

file.write('\n')
file.write(edge2.to_string())
file.write('\n')

plt.figure(2)
log_degree = numpy.log10(degree_data)
log_degree.plot(kind='hist', log=True)
plt.title("Distribution of log base 10 of degrees")
plt.xlabel("Log base 10 of degree")
plt.ylabel("Count")

cent = nx.degree_centrality(g)

cent2 = sorted(cent.items(), reverse=True,key=lambda x: x[1])[:10]

file.write('\n')
file.write(str(cent2))
file.write('\n')

plt.figure(3)
g_cored = nx.k_core(g, 3)
g_data = pandas.Series(dict(nx.degree(g_cored)))
g_data.plot(kind = 'hist')
plt.title('3-cored graph degree distribution')
plt.xlabel('Degree')
plt.ylabel('Count')

file.write(str(g_cored.number_of_edges()))
file.write('\n')
file.write(str(g_cored.number_of_nodes()))
file.write('\n')

labels_dict = {}
for i in g_cored.nodes():
    if type(i) == str and len(i) >= 15:
        labels_dict[i] = i[0:13] + '.'
    elif type(i) == str and len(i) < 15:
        labels_dict[i] = i[0:14]
pos = nx.circular_layout(g_cored)

plt.figure(4)
nx.draw(g_cored, with_labels = True, labels = labels_dict, font_size = 8, pos = pos)

'''Network/data analysis of a csv file containing data obtained from Facebook.'''
fileref2 = open('facebook_combined.csv',encoding='ISO-8859-1')

edge_data_1 = pandas.read_csv(fileref2)
edge = edge_data_1.head()

g2 = nx.Graph()
g2.add_edges_from(edge_data_1.values)

file.write(str(g2.number_of_edges()))
file.write('\n')
file.write(str(g2.number_of_nodes()))

degree_data = pandas.Series(dict(nx.degree(g2)))

edge2 = degree_data.sort_values(ascending=False).head(10)

file.write('\n')
file.write(edge2.to_string())
file.write('\n')

cent = nx.degree_centrality(g2)

cent2 = sorted(cent.items(), reverse=True,key=lambda x: x[1])[:10]

file.write('\n')
file.write(str(cent2))
file.write('\n')

g2_cored = nx.k_core(g2, 3)

file.write(str(g2_cored.number_of_edges()))
file.write('\n')
file.write(str(g2_cored.number_of_nodes()))
file.write('\n')

pos = nx.circular_layout(g2_cored)
plt.figure(5)
nx.draw(g2_cored, with_labels = False,font_size = 8, pos = pos)
file.write('\n')
file.write('''The graph is called Social Circles: Facebook. The dataset consists 
of 'circles' from Facebook, and all of the data has been anonymized for each 
user with a new value. From a qualatative perspective, it would appear that 
there are a multitude of edges in the upper right area of the graph that may 
signify a commonality in things such as interests, political affiliation, or 
hobbies between all of the remaining nodes.''')

file.close()