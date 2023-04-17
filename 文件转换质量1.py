fd1 = open("in162.txt", "r")
sum = 0
n = 0
line = fd1.readline()
weight = list(line.split())
for item in weight:
    sum += eval(item)*0.454
    n += 1
    if n == 10:
        break
fd2 = open("out162.txt", 'w')
fd2.write("%.2f" % sum)
fd1.close()
fd2.close()
