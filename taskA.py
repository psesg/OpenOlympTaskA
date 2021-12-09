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
        n = nm[0]
        m = nm[1]
        logging.info("n = {}, m = {}".format(n, m))
    if k == 1:
        n_list = workstr.strip("\n").split(" ", int(n))
        logging.info("n_list = {}".format(n_list))
    if k == 2:
        m_list = workstr.strip("\n").split(" ", int(m))
        logging.info("m_list = {}".format(m_list))

# print(m_list[-1:], len(m_list))

if len(m_list) > len(n_list):       # never found
    for i in range(len(n_list)):
        print("-1", end=" ")
        exit(0)

if m_list == n_list:
    for i in range(len(n_list)):
        print("1", end=" ")             # equal
        exit(0)

leastnotfound = False
for j in range(len(m_list) - 1, -1, -1):
    if not m_list[j] in n_list:
        leastnotfound = True
        break
if  leastnotfound ==  True:
    for i in range(len(n_list)):
        print("-1", end=" ")
    exit(0)

for i in range(len(n_list)):
    pos = -1
    minpos = -1
    bFit = False
    firstOc = True
    for j in range(len(m_list)-1, -1, -1):
        indexes = [k for k, l in enumerate(n_list) if l == m_list[j]]
        #print(indexes, end=" ")
        for x in  range(len(indexes)):
            #print(indexes[x], end=" ")
            if indexes[x] < len(m_list)-1:
                continue
            else:
                Fit = True
                if firstOc == True:

                    minpos = indexes[x]+1
                    firstOc = False
                    #print(minpos+1, end=" ")

    print(minpos, end=" ")