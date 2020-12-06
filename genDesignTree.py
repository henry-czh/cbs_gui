#!/usr/bin/env python3

import re
import sys

def create_dict(tdict,inst_list):
    if len(inst_list)==1:
        tdict[inst_list[0]]=dict()
        tdict[inst_list[0]]['star']=True
    else:
        if not inst_list[0] in tdict:
            tdict[inst_list[0]] = {}
        create_dict(tdict[inst_list[0]],inst_list[1:])
    return tdict
    
def genDesignTree(cfg_file):
    tree_dict = dict()
    instance_pattern=re.compile(r'^[ \t]*\[instance\]')
    input_file = open(cfg_file,'r')
    for line in input_file.readlines():
        if re.match(instance_pattern,line):
            instance_list = re.sub('\[instance\]','',line).strip().split('.')
            tree_dict=create_dict(tree_dict,instance_list)
        else:
            continue
            print ('not found')
    input_file.close()
    return tree_dict

if __name__=='__main__':
    genDesignTree(sys.argv[1])
