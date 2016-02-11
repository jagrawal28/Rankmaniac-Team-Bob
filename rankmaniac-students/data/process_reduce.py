#!/usr/bin/env python

import sys

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




max_ratio_distances = 0.0

max_iters = 0

list_of_nodes = []

for line in sys.stdin:

    node = NodeInformation(line)

    list_of_nodes.append(node)

    max_ratio_distances = max(max_ratio_distances, float(abs(node.current_rank - node.previous_rank))/node.current_rank)

    max_iters = max(max_iters, node.num_iters)




if max_ratio_distances < 0.00000005 or max_iters > 47:
    # Finish
    #this isn't right
    list_of_nodes.sort(key=lambda x: x.current_rank)
    list_of_nodes.reverse()
    for node in list_of_nodes[:20]:
        node.emit_final_rank_string()

else:
    #Another iteration
    for node in list_of_nodes:
        node.emit_string()
    




