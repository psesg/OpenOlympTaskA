import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL

with open('input.txt', 'r') as f:
    lines = f.readlines()
f.close()
for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    if k == 0:
        nm = lines[k].strip("\n").split(" ", 2)
        n = nm[0]
        m = nm[1]
        logging.info("n = {}, m = {}".format(n, m))
    if k == 1:
        n_list = lines[k].strip("\n").split(" ", 200000)
        logging.info("n_list = {}".format(n_list))
    if k == 2:
        m_list = lines[k].strip("\n").split(" ", 200000)
        logging.info("m_list = {}".format(m_list))

print(m_list[-1:], len(m_list))
