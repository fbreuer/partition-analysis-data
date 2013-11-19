import json

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
	return matrix

def instance(n,id=None):
	# the non-negativity constraints are implicit in our setup
    instance = {}
    instance["A"] = thematrix(n)
    instance["b"] = [1 for i in range(2*n)]
    instance["E"] = [1 for i in range(2*n)]
    if id != None:
    	instance["id"] = id
    return instance

def problem_set(n):
    instances = [ instance(i+1,id="%d" % i) for i in range(n)]
    return instances

def write_problem_set(instances,filename):
	file = open(filename,"w")
	json.dump(instances,file)
	file.close()

def plainify(obj):
	#print type(obj), obj
	if isinstance(obj,list):
		return [ plainify(e) for e in obj]
	elif isinstance(obj,dict):
		res = {}
		for key, val in obj.iteritems():
			res[key] = plainify(val)
		return res
	elif isinstance(obj,sage.rings.integer.Integer):
		return int(obj)
	elif isinstance(obj,sage.rings.rational.Rational):
		return {"numerator":obj.numerator(), "denominator":obj.denominator()}
	else:
		return obj

def generate(n,filename):
	instances = plainify(problem_set(n))
	write_problem_set(instances,filename)