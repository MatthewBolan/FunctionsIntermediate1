dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):

    for key,val in dict.items(): # Loops around Locations & Instructors

        print(f"{len(val)} {key.upper()}") # Prints the amount of locations{len(val)} & the key word Location in all Upper caps {key.upper()}

        for i in range(len(val)): #Loops Inside  Locations & Instuctors

            print(val[i]) # Prints indivdual locations

printInfo(dojo) # Connects dojo contents to the Function (def printInfo(dict):)