n = str(input('Complete name: '))
print('Welcome, {}!'.format(n))
n1 = n.upper()
n2 = n.lower()
n3 = len(n.strip())-1
n.split()
n4 = len(n.split()[0])
print('Your name with caps lock: {}'.format(n1))
print('Your name without caps lock: {}'.format(n2))
print('Your name has {} characters'.format(n3))
print('Your first name has {} characters!'.format(n4))