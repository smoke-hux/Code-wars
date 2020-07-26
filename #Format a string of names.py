#Format a string of names

def namelist(names):
    huxley = ''
    if(len(names) == 1):
        return names[0]['name']
    elif(len(names) == 2):
        huxley = huxley + names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for i in range(0, len(names)-1):
            huxley = huxley + names[i]['name'] + ", "
        huxley = huxley[:-2] + " & " + names[len(names)-1]['name']
    return huxley




#other solutions
def namelist1(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),names[-1]['names'])
    elif names:
        return names[0]['name']
    else:
        return ''

    
    
    
#another solution

def namelist2(names):
    if len(names)==0:
        return ''
    if len(names)==1:
        return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']



#another solution 
def namelist3(names):
    return ", ".join([name["name"] for name in names])[::-1].replace("," "&", 1)[::-1]