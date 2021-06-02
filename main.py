from repository.functions import *

list = ['name', 'age', 'address']
clas_name = 'client'
form_name = 'form_client'

print('Creating an class/entity with encapsulation.')
create_class(clas_name, list)

print('')
print('Creating an object.')
print(object_creator(clas_name, list))

print('')
print('Creating an django form object.')
django_form = django_object_creator(clas_name, list)
for i in django_form:
    print(i)

print('')
print('Creating an api object.')
api_attributes = api_object_creator(list)
for i in api_attributes:
    print(i)


