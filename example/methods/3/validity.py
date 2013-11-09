# -*- coding: utf-8 -*-

def correct(output,answer):
    from sage.all import *
    R=PolynomialRing(QQ,answer[0])
    F=FractionField(R)
    output_answer=""
    for line_index in range(len(output)):
        if "writestat(terminal,r,\"END OF RATFUN\");" in output[line_index]:
            for line in range(len(line_index,output)):
                if ", \"END OF RATFUN\"" in output[line]:
                    output_answer=output_answer+output[line_index].split("=")[1]
            for output_index in range(line_index+1,len(output)):
                output_answer=output_answer+sum(output[line_index:line])
                output_answer.trim()
                print output_answer
                break

    a=F(sage_eval(output_answer, locals=F.gens_dict()))
    b=F(sage_eval(answer[1], locals=F.gens_dict()))
    print a==b
    return a==b
