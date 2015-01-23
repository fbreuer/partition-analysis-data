import sage
import json
import os
import os.path

def spit_json(obj,filename):
    file = open(filename,"w")
    json.dump(obj,file)
    file.close()

def slurp_json(obj,filename):
    file = open(filename,"r")
    result = json.load(file)
    file.close()
    return result

def plainify(obj):
    if isinstance(obj,list) or isinstance(obj,sage.modules.vector_rational_dense.Vector_rational_dense) or isinstance(obj,sage.modules.vector_integer_dense.Vector_integer_dense):
        return [ plainify(e) for e in obj]
    elif isinstance(obj,dict):
        res = {}
        for key, val in obj.iteritems():
            res[key] = plainify(val)
        return res
    elif isinstance(obj,sage.matrix.matrix_integer_dense.Matrix_integer_dense):
        return [ plainify(row) for row in obj.rows()]
    elif isinstance(obj,sage.modules.vector_integer_dense.Vector_integer_dense) or isinstance(obj,tuple):
        return [ plainify(e) for e in obj]
    elif isinstance(obj,sage.rings.integer.Integer):
        return int(obj)
    elif isinstance(obj,sage.rings.rational.Rational):
        if obj.is_integral():
            return int(obj)
        else:
            return {"num":int(obj.numerator()), "den":int(obj.denominator())}
    else:
        if not (isinstance(obj,int) or isinstance(obj,float) or isinstance(obj,str)):
            print type(obj)
        return obj

def write_out(directory,instances):
    """Takes a directory (given as a string) and an array of instances and writes them out into separate JSON files in the given directory. Each instance is required to have an 'id' attribute."""
    plain_instances = plainify(instances)
    os.mkdir(directory)
    for instance in plain_instances:
        basename = str(instance["id"])
        filename = os.path.join(directory,basename+".json")
        spit_json(instance,filename)
