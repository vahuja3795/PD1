#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:47:41 2018

@author: varunahuja
"""
"""This program takes an input file, opens the file, reads the file, 
and outputs four (4) different plots using pandas and matplotlib.pyplot."""

import pandas
import matplotlib.pyplot as	plt


fileref = open('SCDB_2018_01_justiceCentered_Citation.csv',
               encoding='ISO-8859-1')

scdb	= pandas.read_csv(fileref)

scdb_subset =	scdb[scdb.term >= 2000]

scdb_subset.groupby('term').caseId.nunique()

f = plt.figure(figsize=(8,6))
scdb_subset.groupby('term')['caseId'].nunique().plot(kind ='bar')
																								
scdb_subset.groupby(['justiceName','direction']).caseId.nunique()

f = plt.figure(figsize=(12,8))
scdb[scdb.term >= 2000].groupby(['justiceName', 'direction'])['caseId'
    ].nunique().plot(kind="bar")
												
f.tight_layout()

fileref =	 open('SCDB_2018_01_caseCentered_Citation.csv',
                encoding='ISO-8859-1')
               													
scdb	= pandas.read_csv(fileref)

scdb_subset =	scdb[scdb.term >= 2005]

scdb_subset.groupby(['caseDisposition']).caseId.nunique()

f =	plt.figure(figsize=(8,6))
scdb_subset.groupby('caseDisposition')['caseId'].nunique().plot(kind ='bar')
																								
scdb_subset.groupby(['issueArea']).caseId.nunique()

f =	plt.figure(figsize=(8,6))
scdb_subset.groupby('issueArea')['caseId'].nunique().plot(kind ='bar')

'''The graph created for #6 of the project is a visual representation of the 
column titled issueArea. The x-axis of the graph contains values from 1-14 and
each value is representative of the issue that the case dealt with, and the 
y-axis is the number of cases that have been heard since the year 2000 in 
regards to each specific issue. Each value is as the followings: 1-criminal 
procedure, 2-civil rights, 3-first amendment, 4-due process, 5-privacy, 
6-attorneys, 7-unions, 8-economic activity, 9-judicial power, 10-federalism,
11-interstate relations, 12-federal taxation, 13-miscellaneous, and 
14-private action. It would appear that cases concerning criminal procedure, 
civil rights, economica activity, and judicial power compromise a majority of 
the cases that are heard by the Supreme Court'''