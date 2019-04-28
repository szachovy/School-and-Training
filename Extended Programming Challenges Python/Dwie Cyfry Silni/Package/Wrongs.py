def wrongType(num) -> int:
    try:
        num = int(num)
        assert num is not int
        return True
    except ValueError:
        print(str(ValueError) + ' ocurred')
        return False


def wrongRange(num):
    num = int(num)
    if num < 1:
        print('To small number')
        return False

    elif num > 10:
        print('To big number')
        return False

    else:
        return True
