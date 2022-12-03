#!/usr/bin/python

import sys


# FIlE READER

def read_line0(line):
    tmp = line.strip().split()
    m = int(tmp[0])
    n = int(tmp[1])

    return m, n


def readline_ressource(file, n):
    res = []
    while len(res) < n:
        line = file.readline()
        string = line.strip().split()

        for x in string:
            res.append(x)

    return res


def read_product(file, m):
    res = []
    while len(res) < m:
        line = file.readline()
        string = line.strip().split()

        lst_p = []

        for x in string:
            lst_p.append(x)
        res.append(lst_p)

    return res


def formatage(n, m, product, ressource):
    res = "max: "

    for i in range(m):
        res += product[i][-1] + product[i][0]
        if i < m - 1:
            res += " + "
        else:
            res += ";"

    for i in range(n):
        res += ressource[i][n] + ressource[i][0]
        if i < n - 1:
            res += " + "
        else:
            res += ";"

    return res


def file_read(name):
    res = ""
    try:
        f = open(name, 'r')
        line = f.readline()
        n, m = read_line0(line)
        resource = readline_ressource(f, n)
        product = read_product(f, m)
        res = formatage(n, m, product, resource)
    finally:
        f.close()
    return res


# FILE WRITER


# MAIN

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            stres = file_read(sys.argv[i])
            print(stres)
        # os.system('lp_solve output.lp')
