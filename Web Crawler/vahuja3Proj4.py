#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:14:34 2018

@author: varunahuja
"""

import urllib.request	as	ur
import re


def crawl(start, limit):
    """Takes url input with integer limit and returns string of emails."""
    visited = []
    strings = ' '
    strings2 = ' '
    url = start
    website = ur.urlopen(url)
    html = website.read()
    links = re.findall(r'href=[\'"]?([^\'" >]+)', str(html))
    for i in range(len(links)):
        address = links[i]
        if address not in visited:
            connection = ur.urlopen(address)
            content = connection.read()
            strings = get_addresses(content)
            print(strings,sep='\n')
            visited.append(address)
            strings2 = crawl1(address)
            connection.close()
            if len(visited)>=limit:
                break
    for i in range(0,len(strings2)):
        print(strings2[i],sep='\n')

def crawl1(address):
    """Takes links from start webpage and returns email addresses."""
    url = address
    visited = []
    strings = ' '
    website = ur.urlopen(url)
    html = website.read()
    links = re.findall(r'href=[\'"]?([^\'" >]+)', str(html))
    for i in range(len(links)):
        address = links[i]
        if address not in visited:
            connection = ur.urlopen(address)
            content = connection.read()
            strings = get_addresses(content)
            visited.append(address)
            connection.close()
    return strings
            
def get_addresses(content):
    """Function grabs all email addresses on the webpage."""
    strings = re.findall('[a-zA-Z0-9_.]*[@][a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',str(content))
    for x in range(0, len(strings)):
        if strings[x].endswith("."):
            strings[x] = strings[x][0:len(strings[x])-1]
            
    return strings 


    




    
