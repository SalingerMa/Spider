# -*- coding: utf-8 -*-


def dtes():
    q = 1
    for each in [1,2,3,4,5]:
        yield {"rank":"the %s test1" % each,
            "desc":"the %s test2" % each,
               }
        print(q)
        q+=1
    if q ==5:
        print(q)

for i in dtes():
    print(i)

