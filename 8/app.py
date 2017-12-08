#!/usr/bin/env python

import sys

def eval_expression(lhs, expr, rhs):

    if expr == '>':
        return lhs > rhs
    elif expr == '<':
        return lhs < rhs
    elif expr == '==':
        return lhs == rhs
    elif expr == '!=':
        return lhs != rhs
    elif expr == '>=':
        return lhs >= rhs
    elif expr == '<=':
        return lhs <= rhs
    else:
        print("Error, unknown expression %s" % expr)

def solve(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        rows = [x.strip().split(" ") for x in rows] 

        # Initialize all registers
        registers = {}

        for x in rows:
            registers[x[0]] = 0

        v_all_time_max = 0
        for row in rows:
            reg = row[0]
            oper = row[1].strip()

            condition_true = eval_expression(int(registers[row[4]]),
                                             row[5].strip(),
                                             int(row[6]))

            if(condition_true):
                if(oper == 'inc'):
                    registers[reg] += int(row[2])
                elif(oper == 'dec'):
                    registers[reg] -= int(row[2])
                else:
                    print("unknown operator %s" % oper)

            if(registers[reg] > v_all_time_max):
                v_all_time_max = registers[reg]

        v_max = max(list(registers.values()))
        print("Output 1: %d" % v_max)
        print("Output 2: %d" % v_all_time_max)
            
            
if __name__ == "__main__":
    solve(sys.argv[1])
