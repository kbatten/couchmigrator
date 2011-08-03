#!/usr/bin/env python

import json
import sys

import mc_bin_client

# map:
#function (doc) {
#    emit(null, doc);
#}

if len(sys.argv) <= 2:
    print "couchmigrator.py <datafile> <ip>"
    sys.exit()

print "preloading data"
data = json.loads(file(sys.argv[1]).read())

client = mc_bin_client.MemcachedClient(sys.argv[2])

pring "uploading data"
for row in data["rows"]:
    # for some reason 0x80 is at the start of the string
    # this is a bit of a hack to make a valid json string
    key = json.dumps(row["id"]).strip('"')

    value = row["value"]
    if "_id" in value:
        del value["_id"]
    if "_rev" in value:
        del value["_rev"]

    client.set(key, 0, 0, json.dumps(value))
