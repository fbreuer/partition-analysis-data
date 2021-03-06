from util import *

# generate restricted partition function cone instances

# unit vectors indexed starting from 1
def e(i,n):
    e = vector([ 0 for j in range(n)])
    e[i-1] = 1
    return e

# indexed starting from 1
def rp_cone_row(i,n):
    row = e(i,n) - e(i+1,n)
    return row.list()
def rp_cone_matrix(n):
    matrix = [rp_cone_row(i+1,n) for i in range(n-1) ] + [ e(n,n).list() ]
    # if we wanted to have restricted partition function cones, we would also need these rows:
    # ... + [ [1 for i in range(n)] ]
    return matrix
def rp_cone_instance(n,id=None):
    instance = {}
    instance["A"] = rp_cone_matrix(n)
    instance["b"] = [0 for i in range(n)]
    instance["E"] = [0 for i in range(n)]
    if id != None:
    	instance["id"] = id
    return instance

# lecture hall cones are indexed starting from 0. 
# that is, the case of m parts is indexed by m-1. i.e., index i means i+1 parts.
# the dimension of the cone is i+1. the dimension of the polytope is i.
def rp_cone_problem_set(n):
    instances = [ rp_cone_instance(i+1,id="%d" % i) for i in range(n)]
    return instances

def generate(n,filename):
	instances = plainify(rp_cone_problem_set(n))
	print "writing", filename
	spit_json(instances,filename)