from util import *

# generate inequality descriptions of birkhoff polytopes
# variables are usually indexed by x_ij where i and j both range from 1 to n.
# we let i and j run from 0 to n-1
# we map these to the linear string of variables z via x_ij |-> z_{i+nj}

# birkhoff row constraints (fix i vary j)
def thematrix(n):
	matrix = []	
	for i in range(n):
		row = [0 for k in range(n**2)]
		for j in range(n):
			row[i+n*j] = 1
		matrix.append(row)
	for j in range(n):
		row = [0 for k in range(n**2)]
		for i in range(n):
			row[i+n*j] = 1
		matrix.append(row)
	for i in range(n-1):
		row = [0 for k in range(n**2)]
		row[i] = 1
		row[i+1] = -1
		matrix.append(row)	
	return matrix

def instance(n,id=None):
	# the non-negativity constraints are implicit in our setup
    instance = {}
    instance["A"] = thematrix(n)
    instance["b"] = [1 for i in range(2*n)] + [0 for i in range(n-1)]
    instance["E"] = [1 for i in range(2*n)] + [0 for i in range(n-1)]
    if id != None:
    	instance["id"] = id
    return instance

def problem_set(n):
    instances = [ instance(i+1,id="%d" % i) for i in range(n)]
    return instances

def generate(n,filename):
	instances = plainify(problem_set(n))
	print "writing", filename
	spit_json(instances,filename)