# _*_ coding: UTF-8 _*_

import sys

if __name__ == '__main__':

    for s in sys.argv:
        print(s)
    print(sys.path)
    tuple1 = (1, 2, 3, 4)
    tuple2 = ("name", "age", "sex")
    tuple3 = ()
    tuple4 = ("特殊", )
    print(tuple3, tuple4, tuple1 + tuple2)
    set1 = set()
    set1.add(1)
    set2 = {"name", "age", "sex", "sex", 1, 2, 1}
    set3 = set2
    print(set1, set2, set3)

    a = set('abracadabra')
    b = set('alacazam')
    print("a-b:", a-b)
    print("a|b:", a|b)
    print("a&b:", a&b)
    if (n := 16) > 5:
        print("a^b:", a^b)
        c = (a := 6)
        print(c, a)
    print(a, n)
    pass