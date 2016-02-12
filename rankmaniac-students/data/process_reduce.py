#!/usr/bin/env python

import sys
import heapq #wil this cause problems? Think is stdlib

#
# This program outputs:
# NodeID: ID    iter, curr_rank, prev_rank, [outlinks]
# or
# FinalRank: rank   ID
# If it is the final iteration.



# This is a class which gives us some simple operations
# we can perform on nodes to get node information.
class NodeInformation(object):
    """docstring for NodeInformation"""
    def __init__(self, string):
        super(NodeInformation, self).__init__()

        # parsed key is first, parsed value is node info
        parsed_key_value = line.split("\t")

        assert len(parsed_key_value) == 2

        # NodeID
        parsed_key = parsed_key_value[0]

        assert parsed_key.startswith("NodeId:")

        # convert NodeID to integer
        self.node_id = int(parsed_key[len("NodeId:"):])

        # split current rank, previous rank, and outlinks by comma and put 
        # info into list
        parsed_value = parsed_key_value[1].split(",")

        # current rank is a float value
        self.current_rank = float(parsed_value[0])

        # previous rank is a float value
        self.previous_rank = float(parsed_value[1])

        # if it is not the first iteration, we get the links this node
        # connects to and the iteration number.
        if len(parsed_value) > 2 and parsed_value[2].startswith("iters:"):
            self.num_iters = int(parsed_value[2][len("iters:"):])
            self.links = map(int, parsed_value[3:])

        # if it is the frist map iteration, initialize number of iterations
        else:
            self.links = map(int, parsed_value[2:])
            self.num_iters = 0
        

    # This method outputs the node as a string.
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


    # For the node, we emit neighbor, 1/number it connects to * nodes it connects to * its rank, 
    # or if it connects to no nodes, just its itself, its rank.
    def emit_rank_contributions(self):
        for neighbor_id in self.links:
            sys.stdout.write("NodeId:" + str(neighbor_id) + "\t" + str(self.current_rank/len(self.links)) + "\n")

        if len(self.links) == 0:
            sys.stdout.write("NodeId:" + str(self.node_id) + "\t" + str(self.current_rank) + "\n")


# If we have determined we are on the final iteration, then we emit a string of the format
# Final Rank: .... We call this on a node if we have determined it is in the top 20.
    def emit_final_rank_string(self):
        sys.stdout.write("FinalRank:" + str(node.current_rank) + "\t" + str(node.node_id) + "\n")




# We store the node information in here.
nodes = []

# We put each passed in node into our nodes list.
for line in sys.stdin:

    node = NodeInformation(line)

    nodes.append(node)

# We sort the nodes by current and previous rank. We take the top 50
# in both cases, since we want the top 20 ordering and 50 gives us
# some wiggle room.
current_top_nodes = sorted(nodes, key=lambda x: x.current_rank, reverse=True)[:50]
previous_top_nodes = sorted(nodes, key=lambda x: x.previous_rank, reverse=True)[:50]


# This means that our iterations are over and we want to emit final
# rank strings.
ended = True

# For each of the top nodes, we check if they match the previous top node.
# If they don't, we set ended to False.
for i in range(50):
    if current_top_nodes[i] != previous_top_nodes[i] and current_top_nodes[i].num_iters < 47:
        ended = False

# If ended we emit the top 20 ranks.
if ended:
    for node in current_top_nodes[:20]:
        node.emit_final_rank_string()

# Else we emit our nodes.
else:
    for node in nodes:
        node.emit_string()


    




