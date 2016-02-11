#!/usr/bin/env python

import sys
import heapq #wil this cause problems? Think is stdlib

#
# This program simply represents the identity function.
#




class NodeInformation(object):
    """docstring for NodeInformation"""
    def __init__(self, string):
        super(NodeInformation, self).__init__()

        parsed_key_value = line.split("\t")

        assert len(parsed_key_value) == 2

        parsed_key = parsed_key_value[0]

        assert parsed_key.startswith("NodeId:")

        self.node_id = int(parsed_key[len("NodeId:"):])

        parsed_value = parsed_key_value[1].split(",")

        self.current_rank = float(parsed_value[0])

        self.previous_rank = float(parsed_value[1])

        if len(parsed_value) > 2 and parsed_value[2].startswith("iters:"):
            self.num_iters = int(parsed_value[2][len("iters:"):])
            self.links = map(int, parsed_value[3:])

        
        else:
            self.links = map(int, parsed_value[2:])
            self.num_iters = 0
        


    def emit_string(self):
        output_string = "NodeId:"
        output_string += str(self.node_id)
        output_string += "\t"
        output_string += str(self.current_rank)
        output_string += ","
        output_string += str(self.previous_rank)
        output_string += ","
        output_string += "iters:"
        output_string += str(self.num_iters)

        if len(self.links) != 0:
            output_string += ","
            output_string += ",".join(map(str, self.links))
        
        output_string += "\n"
        
        sys.stdout.write(output_string)


    def emit_rank_contributions(self):
        for neighbor_id in self.links:
            sys.stdout.write("NodeId:" + str(neighbor_id) + "\t" + str(self.current_rank/len(self.links)) + "\n")

        if len(self.links) == 0:
            sys.stdout.write("NodeId:" + str(self.node_id) + "\t" + str(self.current_rank) + "\n")



    def emit_final_rank_string(self):
        sys.stdout.write("FinalRank:" + str(node.current_rank) + "\t" + str(node.node_id) + "\n")




#max_ratio_distances = 0.0


nodes = []

for line in sys.stdin:

    node = NodeInformation(line)

    nodes.append(node)

current_top_nodes = sorted(nodes, key=lambda x: x.current_rank, reverse=True)[:50]
previous_top_nodes = sorted(nodes, key=lambda x: x.previous_rank, reverse=True)[:50]



ended = True

for i in range(50):
    if current_top_nodes[i] != previous_top_nodes[i] and current_top_nodes[i].num_iters < 47:
        ended = False


if ended:
    for node in current_top_nodes[:20]:
        node.emit_final_rank_string()


else:
    for node in nodes:
        node.emit_string()


    




