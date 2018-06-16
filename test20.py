import time
'''
start_time = time.time()
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a**2+b**2 == c**2 and a+b+c == 1000:
                print('a,b,c:%d,%d,%d' % (a, b, c))
end_time = time.time()
print('elapsed:%f' % (end_time-start_time))
print('complete')
'''

start_time = time.time()
for a in range(1001):
    for b in range(1001-a):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print('a,b,c:%d,%d,%d' % (a, b, c))
end_time = time.time()
print('elapsed:%f' % (end_time-start_time))
print('complete')
