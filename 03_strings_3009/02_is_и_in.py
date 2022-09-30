x = 5
y = x
print(y is x)  # х и у ссылаются на один и тот же объект
x = 5
y = 5
print(y is x)

animal = 'elephant'
print('e' in animal)  # True
print('eleph' in animal)  # True
print('lphe' in animal)  # False, потому что буквы написаны не в том порядке, в котором они написаны в строке
