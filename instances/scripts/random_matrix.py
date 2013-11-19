import json

# in proper sage code, we should use sage.misc.randstate instead - but this is not necessary here,
# since we don't care about reproducibility of the output of this file
import random
random.seed()

# produces a random m by n matrix with integer entries drawn uniformly from the interval [a,b]
def rand_mat(m,n,a,b):
	matrix = [ [randint(a,b) for j in range(n)] for i in range(m) ]
	return matrix

def rand_vec(m,a,b):
	vector = [ randint(a,b) for i in range(m) ]
	return vector

def instance(m,n,a,b,id=None):
	# the non-negativity constraints are implicit in our setup
    instance = {}
    instance["A"] = rand_mat(m,n,a,b)
    instance["b"] = rand_vec(m,a,b)
    instance["E"] = [0 for i in range(m)]
    if id != None:
    	instance["id"] = id
    return instance

def problem_set(the_n,the_m,a,b,draws):
    instances = [ instance(the_m,the_n,a,b,d) for d in range(draws)]
    return instances

def write_problem_set(instances,filename):
	print "writing", filename
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

def generate(m,n,a,b,draws):
	instances = problem_set(m,n,a,b,draws)
	print instances
	write_problem_set(plainify(instances),"tests/random_%dx%d_matrices_in_%d_%d.json" % (m,n,a,b) )