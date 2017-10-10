#!/usr/bin/env python
# -*- coding:utf-8 -*-


a = {1:2, 3:4}
for i in a:
    print(i)

for i in a:
    a[i] = str(a[i])
print(a)
