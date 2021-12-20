import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL

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
        n_list = list(map(int, n_list))
        logging.info("n_list = {}".format(n_list))
    if k == 2:
        m_list = workstr.strip("\n").split(" ", int(m))
        m_list = list(map(int, m_list))
        logging.info("m_list = {}".format(m_list))

# print(m_list[-1:], len(m_list))

if len(m_list) > len(n_list):       # never found
    logging.info("len(m_list) > len(n_list)")
    for i in range(len(n_list)):
        print("-1", end=" ")
    exit(0)

if m_list == n_list:
    logging.info("m_list == n_list")
    print("1", end=" ")
    for i in range(len(n_list)-1):
        print("-1", end=" ")             # equal
    exit(0)

leastnotfound = False
for j in range(len(m_list) - 1, -1, -1):
    if not m_list[j] in n_list:
        leastnotfound = True
        break
if  leastnotfound ==  True:
    logging.info(" leastnotfound ==  True")
    for i in range(len(n_list)):
        print("-1", end=" ")
    exit(0)

for i in range(len(n_list)):

    ind_max_lim = len(n_list[i:])-1
    ind_max = -1
    res = "-1"
    ind_prev = 0
    for j in range(len(m_list)-1, -1, -1):
    #for j in range(len(m_list)):
        indexes = [k for k, l in enumerate(n_list[i:]) if l == m_list[j]]
        print(indexes, end=" ")
        for indx in range(len(indexes)-1, -1, -1):
            print(indexes[indx]+i, end="*")
            if indexes[indx] < ind_max_lim and  indexes[indx] > len(m_list)-1 and indexes[indx] > ind_prev:
                ind_max = indexes[indx]+i+1
                ind_prev = ind_max
                break

        #for x in  range(len(indexes)):
            #print(indexes[x], end=" ")
    print("ind_max = ", ind_max)

# for i in range(len(n_list)):