#!/usr/bin/env python

import sys

class node:

    def __init__(self, name):
        self.parents = []
        self.childs = []
        self.name = name

    def set_weight(self, weight):    
        self.weight = int(weight)

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.childs.append(child)

    def __repr__(self):
        return self.name

    def calc_weight(self):
        s = self.weight

        for c in self.childs:
            s += c.calc_weight()

        return s

    def is_balanced(self):

        s = set()
        for c in self.childs:
            s.add(c.calc_weight())
            
        return len(s) < 2

    def is_leaf(self):
        return len(self.childs) is 0

    def childs_balanced(self):

        childs_balanced = True
        for c in self.childs:
            if not c.is_balanced():
                return False
        return True
        
def solve1(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        rows = [x.strip().split(" ") for x in rows] 

        nodes = {}
        for row in rows:

            weight = row[1].replace("(","").replace(")","")
            try:
                cur_node = nodes[row[0]]
            except:
                cur_node = node(row[0])
                nodes[row[0]] = cur_node

            cur_node.set_weight(weight)

            for child in row[3:]:
                child = child.replace(",","")
                try:
                    child_node = nodes[child]
                except:
                    child_node = node(child)
                    nodes[child] = child_node

                child_node.add_parent(cur_node)
                cur_node.add_child(child_node)
                nodes[child] = child_node
                
            nodes[row[0]] = cur_node

        print("output 1")
        for k in nodes:
            if(len(nodes[k].parents) == 0):
                bottom = nodes[k].name

        print(bottom)
        print("output 2")

        top = nodes[bottom]

        n = top
        while(True):
            
            if not n.is_balanced():
                childs = n.childs

                if(n.childs_balanced()):
                    print("candidate table:")
                    print("----------------------------------------------------")
                    for c in childs:
                        print("child %s tree_weight: %d, weight: %d balanced=%d" % (c, c.calc_weight(), c.weight, c.is_balanced()))
                    print("\nSubtract the difference in tree_weight from the node_weight in the table above to get the answer:")
                    return
                else:
                    for c in childs:
                        if not c.is_balanced():
                            n = c
                    

                        

if __name__ == "__main__":
    solve1(sys.argv[1])
