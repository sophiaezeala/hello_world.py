
#dictionary:key + value
alien_0={'name': 'john','points': 5}
print(alien_0)
print(alien_0['name'])
print(alien_0['points'])
print(alien_0['name'] + ' has won ' + str(alien_0['points']) + ' points')
alien_0['football']='Messi'
alien_0['food']='rice'
del alien_0['points']
print(alien_0)

favourite_language={'name':'john',
                    'food':'rice',
                    'country':'germany',
                    'age':24
                    }
print(favourite_language['name'].title()+' is eating '+ favourite_language['food']+' in ' + favourite_language['country'].title() + str(favourite_language['age'])+' road ')

user=input('enter username:')
print('Hello,'+ user + "!")

About_a_person={'first_name':'praise','last_name':'ambrose','age':27,'city':'portharcourt'}
print(About_a_person)
