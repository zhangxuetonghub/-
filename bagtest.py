from arraybag import ArrayBag, ArraySortedBag
from linkedbag import LinkedBag


def test(bagtype):
    """
    """
    lyst = [2013, 61, 1973]
    print('The list of items added is:', lyst)
    b1 = bagtype(lyst)
    print('Expect 3:', len(b1))
    print("Expect the bag's string:", b1)
    print('Expect True:', 2013 in b1)
    print('Expect False:', 2012 in b1)
    print('Expect the items on separate lines:')
    for item in b1:
        print(item)

    b1.clear()
    print('Expect {}:', b1)
    b1.add(25)
    print('Expect {25}', b1)
    b1.remove(25)
    print('Expect {}:', b1)
    b1 = bagtype(lyst)
    b1 = bagtype(b1)
    print('Expect True:', b1 == b1)
    print('Expect False:', b1 is b1)
    print('Expect two of each item:', b1 + b1)
    for item in lyst:
        b1.remove(item)
    print('Expect {}:', b1)
    print('Expect crash with KeyError:')
    try:
        b1.remove(99)
    except KeyError as x:
        print(x)


test(LinkedBag)
test(ArraySortedBag)
test(ArrayBag)
