# -*- coding: iso-8859-1 -*-

def total_time(output):
    if output==[]: return "-"
    for line in output:
        if "Total time:" in line:
            return line.split()[-2]

def empty_or_unbounded(output):
    if output==[]: return "-"
    for line in output:
        if "Empty polytope or unbounded polytope!" in line:
            return "1"
    return "0"
