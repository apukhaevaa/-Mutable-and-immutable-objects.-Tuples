# Пухаева Алина Александровна
#  Mutable and immutable objects. Tuples.
# 27.08.2024

immutable_var = (1, 2, False, 'Maths', 'English')
print(type(immutable_var))
print(immutable_var)
#immutable_var[2] = True # Изменение объектов внутри кортежа не предусмотрено, так как в некоторых случаях, программисты не хотят, чтобы данные были изменены. Этот объект необходим для обеспечения безопасности в некоторых случаях.
#print(immutable_var) # Ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам.
mutable_list = [11, 12, True, 'Spain', 'Japan']
print(type(mutable_list))
print(mutable_list)
mutable_list[0:4] = 17, 'Germany'
mutable_list[2] = 'China'
print(mutable_list)

