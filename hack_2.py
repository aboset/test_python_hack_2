"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2():
    result = "fooziman"
    frase = ""
    i=0
    for i in result:
        if i in ('a', 'e', 'i', 'o', 'u'):
            pass
        else:
            frase+=i
            
    return frase