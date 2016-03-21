#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-03-21 10:53:06
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-03-21 11:34:53

"""
For Now directly use csv to import into mongo db
mongoimport -d cf_units -c sweet_cf --type csv --file sweet_cf.csv --headerline --ignoreBlanks
"""


import json
import csv
import pymongo

input_filename = "../sweetCF.csv"
output_filename = "../cf_units.json"

def get_cf_units():
	cf_units = dict()

	csvfile = open(input_filename, "r")
	# fieldnames = ("FirstName","LastName","IDNumber","Message")
	# reader = csv.DictReader( csvfile, fieldnames)
	# out = json.dumps( [ row for row in reader ] )
	# jsonfile.write(out)
	reader = csv.DictReader(csvfile)
	print type(reader)

	# for row in reader:

	# 	print type(row), row
	# 	cf = row.pop("StandardName")
	# 	cf_units[cf] = dict((k, v) for k, v in row.iteritems() if v)
	# return cf_units

def main():
	pass
	# cf_units = get_cf_units()
	# print "Reading Completed."

	# """ Write to cf_units file here """
	# with open(output_filename, "wb") as cffile:
	# 	json.dump(cf_units, cffile, indent=4)
	# print "Writing cf Completed"


if __name__ == '__main__':
	main()