#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ast

class pythonast:
    def __init__(self, ffile):

        pass

    def parse(self, ffile):
        
        fcode = ffile.read()
        funcs = []
        try:
            expr_ast = ast.parse(fcode)
            functions = []
            self.getfunclist(expr_ast, functions)
            for i in functions:
                funcs.append((i.lineno, self.getfunclastline(i.body)))
        except Exception, e:
            print Exception,":",e
        return funcs

    def getfunclastline(self, funcbody):

        x = funcbody[-1]
        if 'orelse' in x._fields and len(x.orelse)!=0:
            return self.getfunclastline(x.orelse)
        elif 'body' in x._fields:
            return self.getfunclastline(x.body)
        else:
            return x.lineno

    def getfunclist(self, expr_ast, functions):
        for i in expr_ast.body:
            if type(i).__name__ == 'FunctionDef':
                if i not in functions:
                    functions.append(i)
                self.getfunclist(i, functions)
            if 'body' in i._fields:
                self.getfunclist(i, functions)


    def finished(self):
        self.file_out.close()

def extractFunctions(fcode):
    pa = pythonast(fcode)
    funcs = pa.parse(fcode)
    return funcs


if __name__ == '__main__':
    # path = 'test_input/CodeJam/2A/python/AdGold_A.py'
    path = 'core.py'
    ffile = open(path, 'r')
    pythonast = pythonast(ffile)
