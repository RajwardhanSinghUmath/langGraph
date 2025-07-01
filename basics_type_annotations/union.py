from typing import Union

def square(x:Union[int,float])->float:
    return x*x

x=5 # fine
x=1.234 #fine
x="String" #fail

# flexible and easy to code and still provide type safety 
