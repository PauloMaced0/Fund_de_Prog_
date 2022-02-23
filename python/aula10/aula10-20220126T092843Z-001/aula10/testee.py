from unicodedata import digit


def tostr(num):
    assert num >= 0
    digits = '0123456789'
    if num < 10:
        return digits[num]
    return tostr(num//10) + digits[num%10]

assert tostr(0) == '0'
assert tostr(9) == '9'
assert tostr(10) == '10'
assert tostr(128) == '128'
assert tostr(2976) == '2976'
print('ALL TESTS PASSED !')



