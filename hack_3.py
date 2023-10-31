"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3():
    result = "fooziman"
    frase = ""
    i=0
    result= result.capitalize()
    if result[2] == 'x':
        result=result.replace(result[2], result[2].upper(),1)
    else:
        pass 
    for i in result:
        if i in ('a', 'e', 'i', 'o', 'u'):
            i= i.replace('a','@')
            i= i.replace('e','3')
            i= i.replace('i','¡')
            i= i.replace('o','0')
            i= i.replace('u','v')
            frase+=i
        else:
            frase+=i
    
    return frase