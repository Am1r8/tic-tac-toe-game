scoreX = 0
scoreO = 0
playCount = 1
tieCount = 0


def TicTacToe():
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  def PrintBoard():
    print()
    print('', board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print('', board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print('', board[6], "|", board[7], "|", board[8])
    print()

  def GetNumber():
    while True:
      number = input()
      try:
        number  = int(number)
        if number in range(1, 10):
          return number
        else:
          print("\nNumber not on board")
      except ValueError:
        print("\nThat's not a number. Try again")
        continue

  def printScore():
    print("\nTotal Played:", playCount, "\'X\' won:", scoreX, "\'O\' won:", scoreO, "Ties:", tieCount)

  def CheckWin(player):
    global scoreX
    global scoreO
    global tieCount

    count = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if board[x] == player and board[y] == player and board[z] == player:
              if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                if player == "X":
                  scoreX += 1
                elif player == "O":
                  scoreO += 1
                print("Player", player ,"wins!\n")
                printScore()
                return True

    for a in range(9):
      if board[a] == "X" or board[a] == "O":
        count += 1
      if count == 9:
        print("The game ends in a Tie\n")
        tieCount += 1
        printScore()
        return True
  
  def Turn(player):
    n = GetNumber()
    if board[n-1] == "X" or board[n-1] == "O":
      print("\nBox is already occupied. Try again")
      Turn(player)
    else:
      board[n-1] = player

    
  
  end = False

  while not end:
    PrintBoard()
    end = CheckWin("O")
    if end == True:
      break
    print("Choose a box Player X")
    Turn("X")


    PrintBoard()
    end = CheckWin("X")
    if end == True:
      break
    print("Choose a box Player O")
    Turn("O")
    
  if input("Play again? (y/n)\n") == "y":
    global playCount
    playCount += 1
    print()
    TicTacToe()

TicTacToe()