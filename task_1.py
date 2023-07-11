link ='C//docspython/3/faq/programming.txt'
*_, name = link.split('/')
_, extension = name.split('.')
print(f'{link}, {name}, {extension}')
