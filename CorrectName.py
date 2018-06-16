#!/sur/bin/env python
# -*- coding: utf-8 -*-


def toright(line):
    temp1 = line.split('?')
    temp2 = line.split('"')

    last = temp1[0] + '" "' + temp2[3] + '"\n'
    return last


file = open('1.bat', mode='r')

L = []
for l in file:
    L.append(toright(l))

file_new = open('1_new.bat', mode='w')
file_new.writelines(L)
file.close()
file_new.close()
print('OK')
