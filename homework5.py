immutable_var = 1,2,3,True,'OK'
print('Immutable tuple: ', immutable_var)
#immutable_var[3] = False # Ошабка потому что кортеж относиться к неизменяемому типу данных
mutable_list = [3,4,5,'Bad',False]
mutable_list[3] = 'OK'
print('Mutable list: ', mutable_list)
