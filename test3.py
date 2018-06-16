# week.py
week = 'xq1xq2xq3xq4xq5xq6xq7'
n=input('请输入星期数')
pos = (int(n)-1) * 3
weekAbbrev = week[pos:pos+3]
print('今天是'+weekAbbrev)
