code_compiled = compile("print(x+y)","func1","exec")
param="x=1;y=2"
exec(param)
exec(code_compiled)