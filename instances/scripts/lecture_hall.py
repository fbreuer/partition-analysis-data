from util import *

def e(i,n):
    e = vector([ 0 for j in range(n)])
    e[i-1] = 1
    return e
def lecture_hall_row(i,n):
    row = (i+1)*e(i,n) - i*e(i+1,n)
    return row.list()
def lecture_hall_matrix(n):
    matrix = [lecture_hall_row(i+1,n+1) for i in range(n) ]
    return matrix
def lecture_hall_instance(n,id=None):
    instance = {}
    instance["A"] = lecture_hall_matrix(n)
    instance["b"] = [0 for i in range(n)]
    instance["E"] = [0 for i in range(n)]
    if id != None:
    	instance["id"] = id
    return instance
def lecture_hall_problem_set(n):
    instances = [ lecture_hall_instance(i+1,id="%d" % i) for i in range(n)]
    return instances

def generate(n,filename):
	instances = plainify(lecture_hall_problem_set(n))
	print "writing", filename
	spit_json(instances,filename)