import random
import time
DARTS = int(input())
hits = 0.0
start = time.perf_counter()
random.seed(123)
for i in range(1, DARTS+1):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    dist = pow(x**2+y**2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4*(hits/DARTS)
print("pi={:.6f},run time={:.2f}" .format(pi, time.perf_counter()-start))
