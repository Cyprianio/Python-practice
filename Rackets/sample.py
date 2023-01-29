from rocket import RocketBoard

newBoard = RocketBoard(5)

newBoard[2].x = 2

for rocket in newBoard.rockets:
    print(rocket)

print("\n", newBoard.getDistance(newBoard[0], newBoard[2]))

print(len(newBoard))

print(newBoard[0].id)