#!/usr/bin/env python3
start = 1
end = 100
testdict = {
    3: 'fizz',
    5: 'buzz',
    7: 'biff',
    11: 'fuzz'
}
for i in range(start, end + 1):
    s = ''
    for k in testdict:
        if i % k == 0:
            s = s + testdict[k]
    if s == '':
        s = i
    print(s)