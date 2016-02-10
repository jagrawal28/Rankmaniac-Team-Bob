#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:

    parsed_key_value = line.split("\t")

    assert len(parsed_key_value) == 2

    parsed_key = parsed_key_value[0]
    assert parsed_key.startswith("NodeId:")

    node_id = int(parsed_key[len("NodeId:"):])

    parsed_value = parsed_key_value[1].split(",")

    current_rank = float(parsed_value[0])

    previous_rank = float(parsed_value[1])

    links = map(int, parsed_value[2:])



    for neighbor_id in links:
    	sys.stdout.write("NodeId:" + str(neighbor_id) + "\t" + str(current_rank/len(links)) + "\n")

    if len(links) == 0:
    	sys.stdout.write("NodeId:" + str(node_id) + "\t" + str(current_rank) + "\n")

    sys.stdout.write(line)