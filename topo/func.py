def get_quarter(d_y, d_x):
    if d_y >= 0:
        if d_x >= 0:
            return 1
        else:
            return 2
    else:
        if d_x <= 0:
            return 3
        else:
            return 4


def are_valid_cords(cords):
    l = len(cords)
    if l % 2 != 0:
        return False
    elif l > 10:
        return False
    else:
        return True


def valid_Kz(Kz):
    return int(Kz)