#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:34:36 2018

@author: varunahuja
"""

import urllib.request	as	ur
import re

f = ur.urlopen('https://www.cs.uic.edu/~sloan/CS111Law/crawlerstart.html')
s = f.read()
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",str(s))
print(emails)

