# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:22:46 2017

@author: Hershel Rege
"""

import csv

txt_file = r"all_reviews.txt"
csv_file = r"yelp_reviews.csv"

with open(txt_file, "r") as infile, open(csv_file, 'w') as outfile:
    in_txt = csv.reader(infile, delimiter = '"')
    out_csv = csv.writer(outfile)
    out_csv.writerows(in_txt)