"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7():
    result = ["a","b","c","d","e"]
    i=0
    b=2
    frase=[]

    if result[0] == "":
        result=result[0].replace('', '0')

    elif len(result) >= 1:
        for i in result:
            if i in ('a', 'b', 'c', 'd', 'e'):
                i=i.replace('a', '1')
                i=i.replace('b', '2' )
                i=i.replace('c', '3')
                i=i.replace('d', '4')
                i=i.replace('e', '5')
                frase+=i
    return frase