


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name,list):

    for i in range(len(list)):
        
        for key,val in list[i].items():

            if key == key_name:

                print(val)

iterateDictionary2('first_name',students)

iterateDictionary2('last_name',students)


