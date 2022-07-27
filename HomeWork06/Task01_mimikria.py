values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

transformation = lambda x: x

transformed_values = list(map(transformation, values))

print('transformed_values:', transformed_values)
print(f'{"values:":>19}', values)

print(values == transformed_values, values is transformed_values)
