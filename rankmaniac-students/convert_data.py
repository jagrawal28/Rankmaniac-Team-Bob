import sys

node_outs = dict()
values = []

for line in sys.stdin:
    parsed_key_value = line.strip("\n").split("\t")
    
    assert len(parsed_key_value) == 2
    
    parsed_key = parsed_key_value[0]
    parsed_value = parsed_key_value[1]
    
    if parsed_value not in values:
        values.append(parsed_value)
        
    if parsed_key not in node_outs:
        node_outs[parsed_key] = parsed_value
        
    else:
        node_outs[parsed_key] = node_outs[parsed_key] + ',' + parsed_value
        
    
for key in values:
    if key in node_outs.keys():
        sys.stdout.write('NodeId:' + key + '\t' + '1.0,0.0,' + node_outs[key] + "\n")
    else:
        sys.stdout.write('NodeId:' + key + '\t' + '1.0,0.0' + "\n")     