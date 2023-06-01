about_a_person={'first_name':'praise','last_name':'ambrose','age':27,'city':'portharcourt',}
print(about_a_person)
print(about_a_person['first_name'])
print(about_a_person['last_name'])
print(about_a_person['age'])
print(about_a_person['city'])

# Arrange items in a lists
favourite_numbers = {'hephzibah': 3, 'michael': 1, 'sophia': 36, 'anthony': 40, 'gift': 29}
print(favourite_numbers['hephzibah'])
print(favourite_numbers['michael'])
print(favourite_numbers['sophia'])
print(favourite_numbers['anthony'])
print(favourite_numbers['gift'])

glossary={'concantanation':'Operation of joining characters strings end-to end\n',
          'tuples':'Immutable as opposed to lists which are mutable\n',
          'list':'Used to store the sequence of various types of data\n',
          'function':'It is a block of code which only runs when it is called\n',
          'dictionary':'Refers to a hashed structure of various pairs of keys and values\n'
          }
print(glossary)
print(glossary['concantanation'])
print(glossary['tuples'])
print(glossary['list'])
print(glossary['function'])
print(glossary['dictionary'])


#looping through dictionary
students_course = {'sophia':'dataanalysis',
                   'emeka':'coding',
                   'chisom':'graphic designer',
                   'gift':'computer',
                   'hope':'cybersecurity',
                   }
for key, value in students_course.items():
    print("key:" + key)
    print("value:" + value)


# concantenation
for names, courses in students_course.items():
    print(names.title() + ' is learning ' + courses)


# looping through keys

students_course = {'sophia':'dataanalysis',
                   'emeka':'coding',
                   'chisom':'graphic designer',
                   'gift':'computer',
                   'hope':'cybersecurity',
                   }
for names in students_course.keys():
    print(names)

friends =["sophia", "gift"]

if names in friends:
    print(" are happy ")
else:
    print(" are sad ")

#river and country
rivers_country = {"nile": "egypt",
                  "mississippi": "united states of america",
                  "volga": "europe"
                  }

#concatenation
for rivers, country in rivers_country.items():
    print(" The " + rivers.title() + " runs through " + country.title())

#loop through keys
for rivers in rivers_country.keys():
    print(rivers)

#loop through values
for country in rivers_country.values():
    print(country)



