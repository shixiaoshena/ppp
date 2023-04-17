# 读取文件
with open("mayun.txt", 'r') as f:
    s = f.read()
# 分类统计文件中的各种字母、符号个数
nUpper = nLower = nDigit = nSpace = nOther = 0
for i in s:
    if i.isupper():
        nUpper += 1
    elif i.islower():
        nLower += 1
    elif i.isdigit():
        nDigit += 1
    elif i.isspace():
        nSpace += 1
    else:
        nOther += 1
print(nUpper, nLower, nDigit, nSpace, nOther)
# 统计单词数量
s_ls = s.replace(',', ' ').split()
print(f"{len(s_ls)} words in all")
# 偏移量
week = input()
offset = sum([ord(i) for i in week]) % 26
print(offset)
# 用凯撒加密后的结果
s_cipher = ""
for i in s:
    if "a" <= i <= "z":
        s_cipher += chr((ord(i)-ord("a")+offset) % 26+ord("a"))
    elif "A" <= i <= "Z":
        s_cipher += chr((ord(i)-ord("A")+offset) % 26+ord("A"))
    else:
        s_cipher += i
print(s_cipher)
