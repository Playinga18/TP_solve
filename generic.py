#!/usr/bin/python

import sys


# UTIL

def display(product):
    for x in product:
        print(x)


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


def formatage(product, ressource):
    res = "max: "
    for i in range(len(product)):
        res += product[i][-1] + product[i][0]
        if i < len(product) - 1:
            res += "+"
        else:
            res += ";\n"
    for i in range(len(ressource)):
        for j in range(len(product)):
            res += product[j][i + 1] + product[j][0]
            if j < len(product) - 1:
                res += "+"
            else:
                res += " <= " + ressource[i] + ";\n"
    return res


def file_read(name):
    res = ""
    try:
        f = open(name, 'r')
        line = f.readline()
        n, m = read_line0(line)
        resource = readline_ressource(f, n)
        product = read_product(f, m)
        res = formatage(product, resource)
    finally:
        f.close()
    return res


# FILE WRITER

def fileWrite(stres):
    try:
        output = open("output.lp", "a")
        output.write(stres)
    finally:
        output.close()


# MAIN

if __name__ == '__main__':
    option = 0
    argc = 1
    if len(sys.argv) > 1:
        if sys.argv[1] == "-int":
            option = 1



        for i in range(1+option, len(sys.argv)):
            stres = file_read(sys.argv[i])
            print(stres)
            fileWrite(stres)
        # os.system('lp_solve output.lp')
