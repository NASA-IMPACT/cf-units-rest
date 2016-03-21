#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2016-03-17 14:35:05
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-03-21 10:54:34

import json
import csv

input_filename = "../sweetCF.csv"
output_filename = "../cf_units.json"

def get_cf_units():
	cf_units = dict()

	csvfile = open(input_filename, "r")
	reader = csv.DictReader(csvfile)
	for row in reader:

		print type(row), row
		cf = row.pop("StandardName")
		cf_units[cf] = dict((k, v) for k, v in row.iteritems() if v)
	return cf_units

def main():
	cf_units = get_cf_units()
	print "Reading Completed."

	""" Write to cf_units file here """
	with open(output_filename, "wb") as cffile:
		json.dump(cf_units, cffile, indent=4)
	print "Writing cf Completed"


if __name__ == '__main__':
	main()