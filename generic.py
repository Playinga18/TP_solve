#!/usr/bin/python
import os
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


def formatage(product, ressource, option):
    res = "max: "
    str_option = ""
    for i in range(len(product)):
        res += product[i][-1] + product[i][0]
        if i < len(product) - 1:
            res += "+"
        else:
            res += ";\n"

        if option == 1:
            str_option += product[i][0]
            if i < len(product) - 1:
                str_option += ", "
            else:
                str_option += ";\n"

    for i in range(len(ressource)):
        for j in range(len(product)):
            res += product[j][i + 1] + product[j][0]
            if j < len(product) - 1:
                res += "+"
            else:
                res += " <= " + ressource[i] + ";\n"

    if option == 1:
        res += "free " + str_option
    return res


def file_read(name, option):
    res = ""
    try:
        f = open(name, 'r')
        line = f.readline()
        n, m = read_line0(line)
        resource = readline_ressource(f, n)
        product = read_product(f, m)
        res = formatage(product, resource, option)
    finally:
        f.close()
    return res


# FILE WRITER

def file_write(stres, name):
    try:
        output = open(name, "w")
        output.write(stres)
    finally:
        output.close()


# MAIN

if __name__ == '__main__':
    option = 0
    argc = 1
    if len(sys.argv) > 2:
        if sys.argv[1] == "-int":
            option = 1
        file_in = sys.argv[1 + option]
        file_out = sys.argv[2 + option]
        res = file_read(file_in, option)
        file_write(res, file_out)
        os.system('lp_solve ' + file_out)
