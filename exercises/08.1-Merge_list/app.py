chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    empty_list = []
    for i in chunk_one:
        empty_list.append(i)
    for i in chunk_two:
        empty_list.append(i)
    return empty_list

print(merge_list(chunk_one, chunk_two))
