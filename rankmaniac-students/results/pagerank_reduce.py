#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

node_id_new_rank = dict()
node_id_old_rank = dict()
node_id_links = dict()

ALPHA = 0.85

for line in sys.stdin:
    
    parsed_key_value = line.split("\t")

    assert len(parsed_key_value) == 2

    parsed_key = parsed_key_value[0]

    node_id = int(parsed_key[len("NodeId:"):])

    if node_id not in node_id_new_rank:
            node_id_new_rank[node_id] = 0.0

    parsed_value = parsed_key_value[1].split(",")

    if len(parsed_value) == 1:

        parsed_rank = float(parsed_value[0])

        node_id_new_rank[node_id] += parsed_rank

    else:

        current_rank = float(parsed_value[0])

        node_id_old_rank[node_id] = current_rank

        links = parsed_value[2:]

        node_id_links[node_id] = links


for node_id in node_id_new_rank:

    output = ""
    output += "NodeId:"
    output += str(node_id)
    output += "\t"
    output += str(node_id_new_rank[node_id] * ALPHA + (1-ALPHA))
    output += ","
    output += str(node_id_old_rank[node_id])
    if len(node_id_links[node_id]) != 0:
        output += ","
        output += ",".join(node_id_links[node_id])
    else:
        output += "\n"

    sys.stdout.write(output)









