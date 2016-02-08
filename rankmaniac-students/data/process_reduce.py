#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

sum_squared_distances = 0.0


list_of_lines = []

list_of_final_rank_lines = []

for line in sys.stdin:

    list_of_lines.append(line)

    parsed_key_value = line.split("\t")

    assert len(parsed_key_value) == 2

    parsed_key = parsed_key_value[0]
    assert parsed_key.startswith("NodeId:")

    node_id = int(parsed_key[len("NodeId:"):])

    parsed_value = parsed_key_value[1].split(",")

    current_rank = float(parsed_value[0])

    previous_rank = float(parsed_value[1])

    links = map(int, parsed_value[2:])

    sum_squared_distances += (current_rank - previous_rank)**2

    final_rank_output = "FinalRank:" + str(current_rank) + "\t" + str(node_id) + "\n"

    list_of_final_rank_lines.append(final_rank_output)



if sum_squared_distances < 0.005:
    # Finish
    #this isn't right
    list_of_final_rank_lines = sorted(list_of_final_rank_lines)
    list_of_final_rank_lines.reverse()
    for line in list_of_final_rank_lines[:20]:
        sys.stdout.write(line)

else:
    #Another iteration
    for line in list_of_lines:
        sys.stdout.write(line)
    




