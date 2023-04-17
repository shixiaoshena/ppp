s = input()
if s == '1':
    lst = [i**3 for i in range(10)]
if s == '2':
    lst = [i**3 for i in range(10) if i % 2 == 0]
if s == '3':
    lst = [(i, i**3) for i in range(10) if i % 2 == 1]
if s == '4':
    ls = ['the lord of the rings', 'anaconda',
          'legally blonde', 'gone with the wind']
    lst = [i.capitalize() for i in ls]
if s in ['1', '2', '3', '4']:
    print(lst)
else:
    print('End of the program')
