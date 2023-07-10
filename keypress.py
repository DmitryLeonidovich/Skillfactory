import msvcrt
print('Press any key.')
n = 0
loops = 0
while True:
    if msvcrt.kbhit():
        s = msvcrt.getch()
        if s == "\000" or s == "xe0":
            s = msvcrt.getch()
        n = ord(s)
        print('\n', n, chr(n))
    else:
        if loops > 10000:
            # print(loops, '>', '\b\b\b\b\b\b\b')
            print(loops, '>')
            loops = 0
        loops += 1
        
    if n == 27:
        break
print('Done.')
print('Press Ctrl+C for closing window.')
while True:
    pass
