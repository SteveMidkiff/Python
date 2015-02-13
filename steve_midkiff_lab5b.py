# This program displays an inverted triangle pattern

##cols = 11
##rows = 10

##for r in range (rows):
##    cols -= 1
##    for c in range (cols):
##        print('*', end='')
##    print(' ')

# I struggled a bit and ended up with a couple of ways to do this.
# I think the one below is probably what you were looking for?

for r in range (11, 0, -1):
    for c in range (r):
        print('*', end='')
    print(' ')

    
