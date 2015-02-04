# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 13:16:04 2015

@author: raphaeltam
"""

import csv
#Data starts from 1969 and ends on 2012.
start_year = 1969
cur_yr = start_year
population = 0

# open output file and write header
fo = open ('us_population1.csv', 'w') 
fieldnames = ['year','pop']
writer = csv.DictWriter (fo, fieldnames=fieldnames)
writer.writeheader()

# read data from 'us_pop.txt'
with open ('us_pop.txt', 'rb') as fi:
    lines = fi.readlines()
    
#Sum data by year and zip code
#Data dictionary says each line is 26 digits long. The first 4 digits is year
#and the last 8 digits is population.  
for l in lines:
    yr = int(l[0:4])
    if yr != cur_yr:
        writer.writerow({'year':cur_yr, 'pop':population})
        cur_yr += 1
        population = int(l[18:25])
    else:
        population = population + int(l[18:26])
writer.writerow({'year':cur_yr, 'pop':population})
fo.close()