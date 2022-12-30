## find max and min of 5 number

a, b, c, d, e = map(int, input('enter 5 numbers : ').split())

if a >= b and a >= c and a >= d and a >= e:
    print('max', a)
if b >= a and b >= c and b >= d and b >= e:
    print('max', b)
if c >= b and c >= a and c >= d and c >= e:
    print('max', c)
if d >= b and d >= c and d >= a and d >= e:
    print('max', d)
if e >= b and e >= c and e >= d and e >= a:
    print('max', e)

if a <= b and a <= c and a <= d and a <= e:
    print('min', a)
if b <= a and b <= c and b <= d and b <= e:
    print('min', b)
if c <= b and c <= a and c <= d and c <= e:
    print('min', c)
if d <= b and d <= c and d <= a and d <= e:
    print('min', d)
if e <= b and e <= c and e <= d and e <= a:
    print('min', e)
