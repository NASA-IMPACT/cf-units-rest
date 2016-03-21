#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-12-22 12:06:24
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-03-21 11:01:34

""" Mongodb
    Database    :       cf_units
    Collections :
            sweet_cf    :   cf_to_units_list
"""

from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost', 27017)
    db = client.cf_units      # mapper collection
    return db


def insert_into_cf(db, doc):
    db.sweet_cf.insert_one(doc)


def insert_into_cf_multi(db, doc_list):
    db.sweet_cf.insert(doc_list)

def main():
    db = get_db()
    single_doc = None
    doc_list = None

    insert_into_cf(db, single_doc)
    insert_into_cf_multi(db, doc_list)

if __name__ == '__main__':
    main()

# db.keywords.insert_one(name_keywords_dict)