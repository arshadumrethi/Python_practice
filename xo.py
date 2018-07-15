def xo(s):
    count_x = 0
    for i in s:
        if i == 'x':
            count_x += 1
        if i == 'X':
            count_x += 1

    # print count_x

    count_o = 0
    for i in s:
        if i == 'o':
            count_o += 1
        if i == 'O':
            count_o += 1

    # print count_o

    if count_x == count_o:
        print True

    else:
        print False
        
    # if 'x' and 'X' and 'o' and 'O' not in s:
    #     return True


xo('vxQxpxxSxfmExkxAxGborNLxooxxxoxxCodoooxxoxxootxhUoJox')
xo('xo0')
xo('x0xxxooooxxxxxx')
xo('frtxioopx')
xo('FFFF')
