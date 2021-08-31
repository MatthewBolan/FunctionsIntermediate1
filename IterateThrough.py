students = [

        {'first_name':  'Michael', 'last_name' : 'Jordan'},

        {'first_name' : 'John', 'last_name' : 'Rosales'},

        {'first_name' : 'Mark', 'last_name' : 'Guillen'},

        {'first_name' : 'KB', 'last_name' : 'Tonel'}

    ]

def iterate_Dictionary(list):

    for x in range (len(list)):

        output = ''

        for key,val in list[x].items():

            output += f' {key} - {val},'

        print(output)

iterate_Dictionary(students)


