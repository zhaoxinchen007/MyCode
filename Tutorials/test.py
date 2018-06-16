# TempConvert.py
val = input("temp")
if val[-1] in ['C', 'c']:
    f = 1.8 * float(val[0:-1])+32
    print('temp:%.2fF' % f)
elif val[-1] in ['f', 'F']:
    c = (float(val[0:-1])-32)/1.8
    print('temp：%.2fc' % c)
else:
    print('error')
