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


if len(b) > len(a):       # never found
    logging.info("len(m_list) > len(n_list)")
    for i in range(len(a)):
        print("-1", end=" ")
    exit(0)

leastnotfound = False
for j in range(len(b) - 1, -1, -1):
    if not b[j] in a:
        leastnotfound = True
        break
if  leastnotfound ==  True:
    logging.info(" leastnotfound ==  True")
    for i in range(len(a)):
        print("-1", end=" ")
    exit(0)


res = []
ind_b_beg_prev = -1
ind_b_beg = -1
ind_b_1 = -1
ind_b_end = -1

i = 0
j = 0
while i < n:
    if a[i] == b[j]:
        if j == 0:
            ind_b_beg = i
            ind_b_1 = i
        if j == 1:
            ind_b_1 = i
        if j == m - 1:
            ind_b_end = i

            for ii in range(ind_b_1 - 1, ind_b_beg, -1):
                if a[ii] == b[0]:
                    ind_b_beg = ii
                    break

            res += [ind_b_end + 1] * (ind_b_beg - ind_b_beg_prev)
            i = ind_b_1 + 1
            j = 0
            ind_b_beg_prev = ind_b_beg
            ind_b_beg = -1
            ind_b_1 = -1
            ind_b_end = -1
        else:
            i += 1
            j += 1
    else:
        i += 1

res += [-1] * (n - len(res))
#print(res)
for i in range(len(res)):
    print(res[i], end=" ")
