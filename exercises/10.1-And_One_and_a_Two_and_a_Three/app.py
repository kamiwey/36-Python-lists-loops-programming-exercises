contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:

for i in contact.items():

    print(f'{i[0]} : {i[1]}')

    #another nice way

    print(" : ".join(i))