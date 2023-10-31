"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1():
    result = "fooziman"

    if len(result) >=3:
        result =result.replace(result[1], result[1].upper(),1)
        result =result.replace(result[4], result[4].upper(),1)
    print(result)

    
    return result

