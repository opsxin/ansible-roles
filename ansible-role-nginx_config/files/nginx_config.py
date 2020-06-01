#!/usr/bin/python3

import os
import sys
import json
import hashlib


def count():
    count = 0
    for file in files:
        if os.path.isfile(os.path.join(nginx_path, file)):
            count += 1
    print(count)


def md5sum(filename):
    if os.path.isfile(os.path.join(nginx_path, filename)):
        # 如果结果为“e10adc3949ba59abbe56e057f20f883e”
        # 则文件中不存在“root /xxx/xxx;”
        d = hashlib.md5("123456".encode('utf-8'))
        for line in open(os.path.join(nginx_path, filename), mode='r'):
            line_split = line.split()
            if len(line_split) > 1 and line_split[0] == "root" and line_split[1].endswith(";"):
                s = ""
                d = hashlib.md5(s.join(line_split).encode('utf-8'))
                break
        print(d.hexdigest())


def discovery():
    data = {"data": []}
    for file in files:
        if os.path.isfile(os.path.join(nginx_path, file)):
            data["data"].append({"{#SITENAME}": file})
    print(json.dumps(data))


if __name__ == "__main__":
    # nginx_path = sys.argv[1]
    nginx_path = "/etc/nginx/sites-enabled"
    files = os.listdir(nginx_path)
    if sys.argv[1] == "discovery":
        discovery()
    elif sys.argv[1] == "count":
        count()
    else:
        md5sum(sys.argv[1])
