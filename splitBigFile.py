#! /usr/bin/env python
# -*- coding:utf-8 -*-

#  argument: Specify the number of rows for each small file after the split.
#  Example: $python2 splitBigFile.py  20000

import os
import sys
import random


def main(num):
    name = "result_"
    file_obj = open("e1000Transfer-VPall.trace", "r")
    head_content = list()
    for _ in range(4):
        head_content.append(file_obj.readline())
    seq = 1
    status = False
    try:
        while True:
            body_content = list()
            for _ in range(num):
                value = file_obj.readline()
                if value:
                    body_content.append(value)
                else:
                    status = True
                    break
            if status and len(body_content) == 0:
                break
            else:
                filepath = "".join(["dataInfo4/", name, str(seq), ".trace"])
                with open(filepath, "w") as ohandler:
                    ohandler.writelines(head_content)
                    ohandler.writelines(body_content)
                seq += 1
    finally:
        file_obj.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "python {} num".format(sys.argv[0])
        sys.exit(0)
    num = int(sys.argv[1])
    main(num)
