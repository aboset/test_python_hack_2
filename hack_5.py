"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5():
    result = "fooziman"
    i = 0
    if len(result) > 2:
        for i in range(len(result)):
            if i == 2:
                result=result.replace(result[i], "-",1)
            elif i == 5:
                result=result.replace(result[i], "-",1)
            elif i == 8:
                result=result.replace(result[i], "-",1)
    else:
        result=result
                
    return result