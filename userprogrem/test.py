notes =  [1,3,5]
header = ['DATE']
print(header)
header.extend((notes))
print(header)
header = ','.join(map(str,header))  + '\n'
print(header)