s = input()
str_upper, str_lower, str_digit = 0, 0, 0
for i in s:
    if i.isupper():
        str_upper += 1
    elif i.islower():
        str_lower += 1
    elif i.isdigit():
        str_digit += 1
print(str_upper)
print(str_lower)
print(str_digit)

