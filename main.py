import copy
import random
from PIL import Image

##vars
seed = 1232131
heigh = 1000
width = 1000
steps = 10000000000000000000000000000000000000000000000000000000000
file = "save"
sfile = "images/img"
##/vars
random.seed(seed)

def rand(n, seed):
    out = []
    for x in range(1, n):
            out.append(bool(random.getrandbits(1)))
    return out

# Init Board
board = []
for x in range(0,width):
    board.append(rand(heigh, seed))


for ñ in range(steps):

    next = copy.deepcopy(board)
    for x in range(1,len(board) - 2):
        for y in range(1, len(board) - 2):
            n = 0
            if board[x+1][y-1]:
                n +=1
            if board[x+1][y]:
                n +=1
            if board[x+1][y+1]:
                n +=1
            if board[x][y-1]:
                n +=1
            if board[x][y+1]:
                n +=1
            if board[x-1][y-1]:
                n +=1
            if board[x-1][y]:
                n +=1
            if board[x-1][y+1]:
                n +=1

            if board[x][y]:
                    if n < 2 or n > 3:
                        next[x][y] = False
                    else:
                        next[x][y] = True
            else:
                if n ==3:
                    next[x][y] = True
                else:
                    next[x][y] = False

    board = next.copy()
    img = Image.new( "1" , (width,heigh), "white")
    pixel = img.load()
    for x in range(0, width - 1):
        for y in range(0, heigh - 1):
            if board[x][y]:
                pixel[x,y] = (0)
    img.save((str(sfile) + str(ñ) + ".png"))


