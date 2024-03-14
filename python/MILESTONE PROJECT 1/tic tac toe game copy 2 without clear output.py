board=[' ']*9
x=[' ']*9
def start():
  chaos="hero"
  while chaos not in ["Y","N","y","n"]:
   chaos=input("do want to start the game Y or N :")
   if chaos not in ["Y","N","y","n"]:
     print("sry invalid input")
  if chaos=="Y" or chaos=="y":
   return True
  elif chaos=="N" or chaos=="n":
   return False  
def bored():
 print(board[6]+"|"+board[7]+"|"+board[8])
 print("-----")
 print(board[3]+"|"+board[4]+"|"+board[5])
 print("-----")
 print(board[0]+"|"+board[1]+"|"+board[2])
def inut():
    input1="voi"
    while input1 not in ["x","o"]:
      inp=input("player1 choose 'x' or 'o':")
      input1=inp.lower()
      if input1 not in ["x","o"]:
        print("invalid input")
    return input1
def ink():
  inpu="amaterasu"
  while inpu not in range(1,10):
   inpu=int(input("enter a number (1-9):"))
   if inpu not in range(1,10):
     print("wrong input")
  return inpu
def func(inpu,player):
    board[inpu-1]=player
    return board
def check():
 if board[6]==board[7] and board[6]==board[8]:
   v=board[6]
   return v
 elif board[3]==board[4] and board[3]==board[5]:
   v=board[3]
   return v
 elif board[0]==board[1] and board[1]==board[2]:
   v=board[0]
   return v
 elif board[6]==board[3] and board[3]==board[0]:
   v=board[6]
   return v
 elif board[4]==board[7] and board[4]==board[1]:
   v=board[4]
   return v
 elif board[8]==board[5] and board[5]==board[2]:
   v=board[8]
   return v
 elif board[6]==board[4] and board[4]==board[2]:
   v=board[6]
   return v
 elif board[0]==board[4] and board[4]==board[8]:
   v=board[0]
   return v
def ch(x,inp):
  if inp in x:
    return True
  else:
    return False 
def conti():
  chaos="hero"
  while chaos not in ["Y","N"]:
   cha=input("do want to continue the game Y or N :")
   chaos=cha.upper()
   if chaos not in ["Y","N"]:
     print("sry invalid input")
  if chaos=="Y":
   return True
  else:
   return False 
def dink(x):
  inpu="amaterasu"
  while inpu not in range(1,10) or inpu in x:
   inpu=int(input("enter a number (1-9):"))
   if inpu not in range(1,10) or inpu in x:
     print("wrong input")
  return inpu
def bor():
 print(board[6]+"|"+board[7]+"|"+board[8])
 print("-----")
 print(board[3]+"|"+board[4]+"|"+board[5])
 print("-----")
 print(board[0]+"|"+board[1]+"|"+board[2])
print("welcome to tic tac toe game")
star=start()
if star:
  os.system('cls')
  print("you are player 1 u make the first move")
  print("Here is your board,grids are same like a number pad so acordingly choose the number")
  bored()
  print("player1 go ahead")
  input1=inut()
  if input1=='x':
     input2='o'
  else:
     input2='x'
if star:
  print("player1 your input")
  inpu1=ink()
  x[0]=inpu1
  board=func(inpu1,input1)
  bored()
  print("player2 your input")
  inpu2=dink(x)
  x[1]=inpu2
  board=func(inpu2,input2)
  bored()
  print("player1 your input")
  inpu3=dink(x)
  x[2]=inpu3
  board=func(inpu3,input1)
  bored()
  print("player2 your input")
  inpu4=dink(x)
  x[3]=inpu4
  board=func(inpu4,input2)
  bored()
i=3
while i<8:
  print("player1 your input")
  i1=dink(x)
  i+=1
  x[i]=i1
  if check()=='x':
    board=func(i1,input1)
    bored()
    print("congo player1 winner")
    break
  elif i==8:
    bored()
    print("its a draw!!")
    break
  else:
    bored()
  
  print("player2 your input")
  i2=dink(x)
  i+=1
  x[i]=i2
  board=func(i2,input2)
  if check()=='o':
    bored()
    print("congo player 2 winner")
    break
  else:
    bored()

  
     
   

    

