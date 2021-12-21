import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

with open('input.txt', 'r') as f:
    lines = f.readlines()
f.close()
n_list = []
m_list = []
for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    workstr = lines[k].strip()
    if k == 0:
        nm = workstr.strip("\n").split(" ", 2)
        n = int(nm[0])
        m = int(nm[1])
        logging.info("n = {}, m = {}".format(n, m))
    if k == 1:
        n_list = workstr.strip("\n").split(" ", int(n))
        a = list(map(int, n_list))
        logging.info("n_list = {}".format(a))
    if k == 2:
        m_list = workstr.strip("\n").split(" ", int(m))
        b = list(map(int, m_list))
        logging.info("m_list = {}".format(b))


res = []
for idx in range(n):
    i = idx
    j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            j += 1
        i += 1
    res.append(i if j == m else -1)

for i in range(len(res)):
    print(res[i], end=" ")

#print(*res)