people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:

    newlist=[]
    for x in people:
        newlist.append(x)
    
    for x in newlist: 
        if x == person_name:
            newlist.remove(x)
    return newlist
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))