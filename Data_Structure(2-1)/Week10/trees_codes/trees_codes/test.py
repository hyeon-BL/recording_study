from binary_search_tree import TreeMap

T = TreeMap()
T['a'] = 123
T['d'] = 890
T['c'] = 567
T['e'] = 101010
T['b'] = 456

print(T['a'])
print(T['b'])

print(list(T.find_range('b', 'e')))

print(T.after(T.find_position('c')).key())
print(T.before(T.find_position('c')).key())

print(list(T.items()))