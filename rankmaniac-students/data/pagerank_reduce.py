#!/usr/bin/env python

import sys

#
# This program takes in lines outputted from pagerank_map and outputs the node 
# and its information with previous and current ranks updated.
#
# NodeID: ID    iter, new_curr_rank, new_prev_rank, [outlinks]

node_information_dict = dict()
contribution_set = set()

ALPHA = 0.85


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

        # if it is the first map iteration, initialize numebr of iterations 
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


# Rank contribution class. This is what we use to parse the objects emited by
# pagerank_map.
class RankContribution(object):
    """docstring for RankContribution"""
    def __init__(self, string):
        super(RankContribution, self).__init__()

        # This gives us node, contribution received.
        parsed_key_value = line.split("\t")

        assert len(parsed_key_value) == 2

        parsed_key = parsed_key_value[0]

        assert parsed_key.startswith("NodeId:")

        self.node_contributed_to = int(parsed_key[len("NodeId:"):])

        self.value_contributed = float(parsed_key_value[1])


for line in sys.stdin:

    # if line outputted from pagerank_map is a node with iters, current rank, previous rank, outlinks, then add to node_information_dict
    try:
        node = NodeInformation(line)
        node_information_dict[node.node_id] = node
    # if line outputted from pagerank_map is node with the contribution it recieved, then add to contribution set 
    except:
        contribution = RankContribution(line)
        contribution_set.add(contribution)


for node_id in node_information_dict:

    node = node_information_dict[node_id]

    # current rank is now the old rank
    node.previous_rank = node.current_rank

    # calculate and update the current rank
    node.current_rank = 1-ALPHA

    # update number of iterations
    node.num_iters += 1

for contribution in contribution_set:
    # add all of the page rank contributions to the node from other nodes 
    node_information_dict[contribution.node_contributed_to].current_rank += ALPHA * contribution.value_contributed


# output 
for node_id in node_information_dict:

    node = node_information_dict[node_id]

    node.emit_string()








