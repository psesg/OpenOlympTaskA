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

ans = [-1] * n
j = 0
p = 0
for cur in range(n):
    if a[cur] == b[j] and j < m-2:
        j = j + 1
    if a[cur] == b[m - 2] and j == m-2:
        p = cur
        if j != n - 1:
            j = j + 1
    if a[cur] == b[m - 1] and j == m-1:
        for k in range(p, 0, -1):
            if ans[k] == -1:
                ans[k] = cur + 1
        j = j - 1

print(*ans)