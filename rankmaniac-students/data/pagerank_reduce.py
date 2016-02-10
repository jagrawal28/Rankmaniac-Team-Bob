#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

node_information_dict = dict()
contribution_set = set()

ALPHA = 0.85



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

        self.links = map(int, parsed_value[2:])

    def emit_string(self):
        output_string = "NodeId:"
        output_string += str(self.node_id)
        output_string += "\t"
        output_string += str(self.current_rank)
        output_string += ","
        output_string += str(self.previous_rank)

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




class RankContribution(object):
    """docstring for RankContribution"""
    def __init__(self, string):
        super(RankContribution, self).__init__()

        parsed_key_value = line.split("\t")

        assert len(parsed_key_value) == 2

        parsed_key = parsed_key_value[0]

        assert parsed_key.startswith("NodeId:")

        self.node_contributed_to = int(parsed_key[len("NodeId:"):])

        self.value_contributed = float(parsed_key_value[1])





        


for line in sys.stdin:

    try:
        node = NodeInformation(line)
        node_information_dict[node.node_id] = node
    except:
        contribution = RankContribution(line)
        contribution_set.add(contribution)


for node_id in node_information_dict:

    node = node_information_dict[node_id]

    node.previous_rank = node.current_rank

    node.current_rank = 1-ALPHA

for contribution in contribution_set:

    node_information_dict[contribution.node_contributed_to].current_rank += ALPHA * contribution.value_contributed



for node_id in node_information_dict:

    node = node_information_dict[node_id]

    node.emit_string()








