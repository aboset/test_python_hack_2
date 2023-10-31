"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6():
    result = ["a","b","c","d","e"]
    i=0
    frase=[]

    if result[0] == "":
        result=result[0].replace('', '0')

    elif len(result) >= 1:
        for i in result:
            if i in ('a', 'b', 'c', 'd', 'e'):
                i=i.replace('a', '1')
                i=i.replace('b', '-')
                i=i.replace('c', '3')
                i=i.replace('d', '-')
                i=i.replace('e', '5')
                frase+=i
    return frase