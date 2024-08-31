def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#print_params(a, b) # ошибка
#print_params(b, c) # ошибка
#print_params(a,b,c) # ошибка
print_params(b=25) #работает
print_params(c=[1,2,3]) #работает
print_params() # работает

values_list = [2, 'name', False]
values_dict = {'a': 3, 'b': 4, 'c': 5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)