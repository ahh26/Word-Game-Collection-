import turtle
import random as rnd
import colorama
from colorama import Fore, Back, Style
import wordle
from wordle import wordlefive,wordlesix,wordleseven,wordleeight 
import hangmanword
from hangmanword import animal,food,music,sport,geography,random
import wordsearch1
from wordsearch1 import animal2,flavour,music2,sport2,geography2,random2
#all inputs are safeguarded so the program won't crash

#hangman
letter=[] #also used for wordle
hangmanlist=[animal,food,music,sport,geography,random]
blankboard=[]
type=0 #word set
guessedletter=[]
wrongletter=[]
wrong=0 #number of wrong guesses
nr=1 #prevent repeat drawing

#wordle
group=0 #word length
wordlelist=[wordlefive,wordlesix,wordleseven,wordleeight]
board=[[],[],[],[],[],[]]
round=1 #6 round in total
guess=""

#word search + hidden word
random=[]#store the randomly chosen word
position=[] #record the position of the start and end of each word, corresponds to the random list
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
found=[]
block=[]#the big word grid
count=5 #number of words that user has to find
size=20 #size of the word grid
word=[animal2,flavour,music2,sport2,geography2,random2]

#used for all games
win=False
end=True
again=True
gamchoice=""

def intro(): #the word game lobby, where user chooses the game to play
  global gamechoice
  print(Fore.WHITE+'''
Hi!!😎
Welcome to the Word Game Lobby, here are the word games you can play:

1-Hangman
2-Wordle
3-Word Search
4-Hidden Words

''')
  while True:
    gamechoice=input(Fore.WHITE+"Enter the number of the game you want to play: ")
    if gamechoice=="1" or gamechoice=="2" or gamechoice=="3" or gamechoice=="4": 
     break
    else:
      print(Fore.RED+"Invalid Input")
      
#hangman functions
def hangmanset(): #setup of hangman
  global hangmanlist,blankboard,letter,wrong,end,guessedletter,nr,found,wrongletter 
  #initializing all these variables and list
  letter=[]
  guessedletter=[]
  blankboard=[]
  found=[]
  wrongletter=[]
  wrong=0
  end=True
  nr=1
  t.left(90) #drawing the stand to hang the man
  t.pendown()
  t.forward(250)
  t.right(90)
  t.forward(100)
  t.penup()
  t.goto(-100,150)
  t.pendown()
  t.left(45)
  t.forward(70)
  t.penup()
  t.goto(0,200)
  t.right(135)
  while True: #choosing word set
    type=input(Fore.WHITE+'''Which word set do you want to play (input the number):
1-animal / 2-food / 3-music / 4-sport / 5-geography / 6-random ''')
    if type=="1" or type=="2" or type=="3" or type=="4" or type=="5" or type=="6":
      break
  type=int(type)-1 #tranfer type into integer here so that the program won't crash if it receives a random string
  a=rnd.randint(0,len(hangmanlist[type])-1)#random word
  wordis=hangmanlist[type][a] 
  for i in wordis: 
    letter.append(i.upper())#add the letters of the word, including blank separately into the list letter
    if i==" ":
      blankboard.append(" ")
    else:
      blankboard.append("_")#add the underscores or spaces into the list blankboard
    
def hangmanmain(): #main program for hangman
  global wrong,blankboard,letter,wrongletter
  print("")
  for i in blankboard: #print the underscores/correctly guessed letters
    print(Fore.WHITE+i,end=" ")
  print("")
  print("")
  if len(wrongletter): #print the incorrectly guessed letters if there are
    print(Fore.BLACK+"( Your wrong guesses: ",end="")
    for i in wrongletter:
      print(i,end=" ")
    print(")")
  while True: #accepting user input
    print("")
    guess=input(Fore.WHITE+"Enter your guess: ")
    guess=guess.upper() #transfer the input to uppercase so it accepts both lowercase and uppercase inputs
    if guess=="QUIT": #quit the game
      return 0
    if not(guess>="A" and guess<="Z" and len(guess)==1): #letting user enter again if the input is not a letter or already guessed
      print(Fore.RED+"Please guess a letter")
    elif guess in guessedletter:
      print(Fore.RED+"You've already guessed this letter")
    else:
      break
  guessedletter.append(guess) #add the guessed letters into the list
  if guess in letter: #outputing the result
    print(Fore.GREEN+f"Yeah! {guess} is in the word!")
    for i in range(0,len(letter)): #using a loop for the letter that appears more than 1 time in the word
      if guess==letter[i]: 
        blankboard[i]=guess
  else:
    wrong+=1
    print(Fore.RED+f"{guess} is not in the word")
    wrongletter.append(guess.upper()) #add to wrong letter list if it's incorrect

def hangmanwin(): #determining if the user wins or if the game ends
  global wrong,end,win
  if wrong==7:
    end=False #game ends
    win=False #didn't win
  if "_" not in blankboard:
    end=False #game ends
    win=True #win
    print("")
    for i in blankboard: #print the final result again
      print(Fore.WHITE+i,end=" ")
    print("")
      
 
def drawman(a):#drawing the hangman(in a separate function to make it less messy)
  global nr
   #nr --> prevent drawing the same thing several times
  if a==1 and nr==1: #draw rope
    t.pendown()
    t.forward(30)
    nr=2
  elif a==2 and nr==2: #draw head
    t.right(90)
    t.circle(20)
    t.penup()
    t.goto(0,130)
    t.left(90)
    nr=3
  elif a==3 and nr==3: #draw body
    t.left(5)
    t.pendown()
    t.forward(60)
    t.penup()
    nr=4
  elif a==4 and nr==4: #draw left arm
    t.goto(0,120)
    t.right(20)
    t.pendown()
    t.forward(50)
    t.penup()
    nr=5
  elif a==5 and nr==5: #draw right arm
    t.goto(0,120)
    t.left(45)
    t.pendown()
    t.forward(50)
    t.penup()
    nr=6
  elif a==6 and nr==6:#draw left leg
    t.goto(4,70)
    t.right(20)
    t.pendown()
    t.forward(60)
    t.penup()
    nr=7
  elif a==7 and nr==7: #draw right leg and eyes
    t.goto(5,70)
    t.left(20)
    t.pendown()
    t.forward(60)
    t.penup()
    t.goto(-10,160)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(-10,150)
    t.left(120)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(5,160)
    t.right(120)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(5,150)
    t.left(120)
    t.pendown()
    t.forward(10)
    t.penup()


#wordle functions
def wordleset(): #choose a random word and set up the list for game
  global k,group,round,board,letter,win
  #resetting/initializing some variables and list
  board=[[],[],[],[],[],[]] 
  letter=[]
  round=1
  win=False
  while True: #choosing word length
    group=input(Fore.WHITE+"Choose the word length: 5/6/7/8 ")
    if group=="5":
      k=0
      break
    elif group=="6":
      k=1
      break
    elif group=="7":
      k=2
      break 
    elif group=="8":
      k=3
      break
  a=rnd.randint(0,len(wordlelist[k])-1) #choosing a random word from the word list
  group=int(group) #record the length of the word
  
  for i in wordlelist[k][a]:#add the words into the list letter
    letter.append(i.upper())
    
  for i in range(6):#create the board for wordle with all underscores
    for j in range(group):
      board[i].append("_")
   
def wordlemain(): # main program for wordle
  global round
  while True: #accepeting user input
    print("")
    guess=input(Fore.WHITE+"Enter your guess: ") 
    if len(guess)==group:
      break
    if guess.upper()=="QUIT":
      return 0
    print(Fore.RED+f"Please enter a {group}-letter word")
  for i in range(0,len(guess)): #change the uncerscores in board list into the letters in the input word
    board[round-1][i]=guess[i].upper()
    
def drawboard(): #output the board for wordle
  global group,win
  print("")
  print(Fore.WHITE+"┌"+"─"*group*2+"─"+"┐") #draw border
  for i in range(6): #output result
    a=0 #used to determine whether user has correctly guessed all the letters
    print(Fore.WHITE+"│",end=" ")
    for j in range(0,group): #green if in correct position
      if board[i][j]==letter[j]:
          print(Fore.GREEN+board[i][j],end=" ")
          a+=1
      elif board[i][j] in letter: #yellow if in the word but incorrect position
          print(Fore.YELLOW+board[i][j],end=" ")
      else: #white if not in the word
        print(Fore.WHITE+board[i][j],end=" ")
    print(Fore.WHITE+"│",end="")
    if a==group: #number of correctly guessed letters=word length->user wins
      win=True
    print("")
  print(Fore.WHITE+"└"+"─"*group*2+"─"+"┘")
  print("")

def wordlewin(): #determining if the user wins or the game ends
  if round<=6:
    if round<=2:
      emoji="🤩"
    elif round<=4:
      emoji="😊"
    elif round<=6:
      emoji="🙂"
    print(f"Congratulations! You got the Wordle in {round} {emoji}")
  else:
    print("You lose:( The word is",end=" ")
    for i in letter:
      print(Fore.GREEN+i,end="")
    print("")
  
#word search & hidden word setup
def wordsearchset(size,count): 
  global block,word,random,position,found
  #initializing lists
  random=[]  #store the randomly chosen words
  block=[] #the entire word grid
  position=[] #store the position of the chosen words
  found=[] #store the words found
  for i in range(size): #setting up word grid, all the letters are presented by spaces for now
    line=[]
    for i in range(size):
      line.append(" ")
    block.append(line)
  type=0
  if gamechoice=="3": #if the game is wordsearch, the word list will automatically be the random words
    type=5
  else: #if the game is hidden word
    print("")
    while True: #user chooses the preferred word set
      type=input(Fore.WHITE+'''Which word set do you want to play (input the number):
1-animal / 2-flavour / 3-music / 4-sport / 5-geography / 6-random ''')
      if type=="1" or type=="2" or type=="3" or type=="4" or type=="5" or type=="6":
        break
    type=int(type)-1 
  while len(random)<count: #choosing random words from the word set
    l=rnd.choice(word[type]).upper()
    if l in random: #make sure no repetitive words
      continue
    elif len(l)>=size: #reselect if the word is too long
      continue
    random.append(l)
  #loop to insert words into the list
  for i in random: 
    bad=True #Not in correct position
    direction=[0,1,-1] #different directions
    while bad:  #first check if the word can fit into the word grid
      while True:
        x=direction[rnd.randint(0,2)]
        y=direction[rnd.randint(0,2)]
        if x==0 and y==0: #both x and y equal 0 --> no direction
          continue 
        break
      startx=rnd.randint(0,size-1) #get a random starting position
      starty=rnd.randint(0,size-1)
      endx=startx+len(i)*x # calculate the ending position
      endy=starty+len(i)*y
      if endx<0 or endx>=size or endy<0 or endy>=size: #out of border, find a new place for the word
        continue 

      again=False #if again=True --> unable to put in the word, generate again
      for j in range(len(i)): #then check if the word can really be put at that position(if there's free space or the same letter)
        positionx=startx+j*x 
        positiony=starty+j*y
        a=block[positionx][positiony] #check if the corresponding position in the block list is free
        if a!=" ":
          if a==i[j]:
            continue
          else:
            again=True
            break
      if again:
        continue
      else: #if the word can be put into the grid
        temp=[] #temporary list
        for j in range(len(i)): #store all the column and row numbers for the letters in the word, used later to determine if user inputs the position correctly, and highlight the found words
          block[startx+j*x][starty+j*y]=i[j]
          temp.append(startx+j*x)
          temp.append(starty+j*y)
        bad=False
        position.append(temp)#add the temp list(positions of the letters in the word) into the position list
  for i in range(size): #after inserting all the random words into the word grid, fill the rest of the grid with random letters
    for j in range(size):
      if block[i][j]==" ":
        block[i][j]=alpha[rnd.randint(0,25)]
        
      
#word search function
def printgrid(size): #output the word grid for word search
  global block,word,count,found
  print("")
  print(Fore.LIGHTBLUE_EX+"WORDLIST:",end=" ") #print the list of words for the user    
  for i in random:
    if i in found:#if the word is found, print it in a different color
      print(Fore.LIGHTBLUE_EX+i.lower(),end=" ")
    else:
      print(Fore.WHITE+i.lower(),end=" ")
  print("")
  print("")
  print("    ",end="")
  for i in range(size): #printing column numbers
    if i<=9:
      print(" ",end="")
    print(Fore.BLACK+str(i),end=" ")
  print("")
  for i in range(size):
    print(" ",end="")
    if i<=9:
      print(" ",end="")
    print(Fore.BLACK+str(i),end="  ") #printing row number
    for j in range(size):
      if "a"<=block[i][j]<="z": # the letters in the block list are lowercased--> they are in the words found by the user, print them in a different color
        print(Fore.LIGHTMAGENTA_EX+block[i][j].upper(),end="")
      else:
        print(Fore.WHITE+block[i][j],end="")
      if j!=(size-1): #printing spaces between the letters (except for the last letter of the row)
        print("  ",end="")
    print(" ",end="")
    if i<=9:
      print(" ",end="") #if the number if one digit number, print one more space
    print(Fore.BLACK+str(i),end=" ") #printing row number
    print("")
  print("    ",end="")
  for i in range(size):#printing column numbers
    if i<=9:
      print(" ",end="")
    print(Fore.BLACK+str(i),end=" ")
  print("")
  print("")


  
def wordsearchmain(size): #main program for word search
  global block,count,found
  printgrid(size)
  while True: #accepting user input for starting point
    print("")
    findstart=input(Fore.WHITE+"Enter the starting point of the word: Column:_ Row:_ ")
    if findstart.upper()=="QUIT":
      return 0
    start=findstart.split(" ") #split the input and make it a list
    if len(start)==2: #break if user has correctly inputted 2 numbers
      if "0"<=start[0]<="9" and "0"<=start[1]<="9":
        break
    print(Fore.RED+"Invalid input")
  while True: #accepting user input for ending point(same code as the starting point)
    findend=input(Fore.WHITE+"Enter the ending point of the word: Column:_ Row:_ ")
    if findend.upper()=="QUIT":
      return 0
    end=findend.split(" ")
    if len(end)==2:
      if "0"<=end[0]<="9" and "0"<=end[1]<="9":
        break
    print(Fore.RED+"Invalid input")

  find=False #used to determine whether the user has found the word
  for i in range(len(position)):
    if start[1]==str(position[i][0]) and start[0]==str(position[i][1]) and end[1]==str(position[i][len(position[i])-2]) and end[0]==str(position[i][len(position[i])-1]): #if the user input and the positions stored in the list match, then user has correctly found the word
      find=True
      for j in range(0,len(position[i])-1,2):
        block[position[i][j]][position[i][j+1]]=block[position[i][j]][position[i][j+1]].lower() #making the letters of the found words lower case, so it will be easier for me to print them in another colour
      break
  if find:  #telling user whether the input is correct or not
    found.append(random[i])
    count-=1
    print(Fore.GREEN+f"Yay you found {random[i]} :) {count} words left!")
  else:
    print(Fore.RED+f"Can't find the word:( {count} words left!")

#Hidden word function
def hiddengrid(size): #printing grid for the game hidden word
  global block
  print("")
  for i in range(size):
    for j in range(size):
      if "a"<=block[i][j]<="z": #lower case -> letters are in the words correctly found by the user
        print(Fore.LIGHTCYAN_EX+block[i][j].upper(),end=" ")
      else:
        print(Fore.WHITE+block[i][j],end=" ")
    print("")  


def hiddenmain(): #main program for hidden word
  global count,found,position
  hiddengrid(size)
  print("")
  ans=input(Fore.WHITE+"Enter the word you found: ") #accepting input
  if ans.upper()=="H": #if input=h -> print the hint
    while True:
      i=rnd.randint(0,len(random)-1)
      if random[i] not in found: #making sure to give hint for unfound words
        print(Fore.YELLOW+f"Hint- First two letters: {random[i][0]}{random[i][1]}")
        break
    ans=input(Fore.WHITE+"Enter the word you found: ")#asking user for input again after giving the hint
  if ans.upper()=="QUIT":
    return 1 #quit the function
  elif ans.upper()=="L":
    return 0 #quit the function
  if ans.upper() in found: #if user inputs the word that's already found
    print(Fore.RED+"You already got this word")
  elif ans.upper() in random: #input in the list 
    print(Fore.GREEN+f"Yayy you found the word {ans.upper()}")
    found.append(ans.upper())
    idx=random.index(ans.upper())
    for j in range(0,len(position[idx])-1,2):
      block[position[idx][j]][position[idx][j+1]]=block[position[idx][j]][position[idx][j+1]].lower() #make the letters of found words lower case, so it will be easier for me to print them in another color
    count-=1 
  else: #input not in the list
    print(Fore.RED+"Not in the list!")
  print("")
  print(Fore.CYAN+"Words you have found:",end=" ") #print the words user has already found
  for i in found:
    print(Fore.WHITE+i,end=" ")
  print("")
  if count>1:
    print(Fore.WHITE+f"{count} words left!")
  else:
    print(Fore.WHITE+f"{count} word left!") #print "1 word" instead of "1 words"

    
 
#function for all games
def sure(): #before the game, asking user if he/she wants to play the game after reading the instructions
  yes=""
  while True:
    yes=input("Play this game? (y/n) ")
    if yes=="y" or yes=="n":
      break
  return yes
  
def playagain(): #letting user to choose what to play next after a game ends
  global gamechoice,again
  while True:
    ans=input(Fore.MAGENTA+''' 
1-Play Hangman
2-Play Wordle
3-Play Wordsearch
4-Play Hidden Words
5-End playing
    
''')
    if ans=="1" or ans=="2" or ans=="3" or ans=="4" or ans=="5":
      break
  if ans=="5":#if user inputs 5, the program ends
    again=False
  else:
    gamechoice=ans


#main program, calling for all of the functions
intro() 
while True:
  if again==False: #ending the program if user has inputted "5" in playagain()
    print("")
    print(Fore.WHITE+"Bye!")
    break
    
  if gamechoice=="1": #hangman
    screen = turtle.Screen() #setting up turtle
    screen.setup(1.0, 1.0)
    print(Fore.WHITE+'''
————————————————————————————
''')
    print(Fore.BLUE+'''Welcome to Hangman!

Here are the rules:)

  1.Start by selecting a word set. A word will be randomly chosen from your selected set.
  2.Your goal is to guess the chosen word. The word is initially hidden and represented by a row of underscores, each underscore symbolizing a letter of the word.
  3.In each round, enter a letter as your guess to uncover the mystery word.
  4.If your guessed letter is in the word, it will appear in its correct position.
    If the letter is not in the chosen word, a part of the hangman is drawn. 
  5.The hangman is drawn in the order: rope, head, body, left arm, right arm, left leg, right leg(7 parts in total)
  6.If you correctly guess the word before the hangman is completed, you win; otherwise, you lose.
  7.The game ends when the word is correctly guessed or the hangman is fully drawn (meaning that you have guessed 7 wrong letters).
  **Input the word "quit" if you want to quit after the game has started**

''')
    if sure()=="n": # jumping back to the word lobby if user chooses not to play the game
      print(Fore.WHITE+'''
————————————————————————————
''')
      intro()
      continue
    print(Fore.BLUE+'''
    
Enjoy your game!
''')
    print(Fore.WHITE+'''
————————————————————————————
''')
    
    t = turtle.Turtle()
    t.shape("classic")
    t.pensize(5)
    turtle.colormode(255)
    t.penup()
    t.goto(-100,-50)
    hangmanset()
    q=0
    while end: 
      if hangmanmain()==0: #if user inputs the word "quit" to quit the game
        q=1
        break
      drawman(wrong)
      hangmanwin()
    if q==1:
      playagain()
      continue
    #after the game ends
    if win: 
      print("")
      print(Fore.WHITE+"You win! The word is",end=" ")
    else:
      print("")
      print(Fore.WHITE+"You lose:( The word is",end=" ")
    for i in letter:
      print(Fore.GREEN+i,end="")
    print("")
    playagain()
    t.hideturtle()
    t.clear()
    
  elif gamechoice=="2": #wordle
    print(Fore.WHITE+'''
————————————————————————————
''')
    print(Fore.BLUE+'''Welcome to Wordle!!!
    
Here are the rules:)

  1.Start by selecting your preferred word length: 5, 6, 7, or 8 letters. 
  2.In each round, input a word with the correct number of letters that you think might be the hidden word.
  3.Each letter of the word you input will appear in different colours. 
    The meaning of the colours are --
        White: the letter is not present in the correct word.
        Yellow: the letter is in the hidden word but in an incorrect position.
        Green: the letter is in the hidden word and correctly positioned.
  4.You have six attempts to guess the correct word. The game automatically ends after six attempts.
  5.If you guess the correct word within six attempts, you win; otherwise, you lose.
  **Input the word "quit" if you want to quit after the game has started**

''')
    if sure()=="n":
      print(Fore.WHITE+'''
————————————————————————————
''')
      intro()
      continue
    print(Fore.BLUE+'''
    
Enjoy your game!
''')
    print(Fore.WHITE+'''
————————————————————————————
''')
    wordleset()
    q=0
    for i in range(6):
      if wordlemain()==0: #if user wants to quit the game
         q=1
         break
      drawboard()
      if win:
        break
      round+=1
    if q==1:
      playagain()
      continue
    wordlewin()
    playagain()
    
  elif gamechoice=="3": #word search
    print(Fore.WHITE+''' 
————————————————————————————
''')
    print(Fore.BLUE+'''Welcome to Word Search!!!
    
Here are the rules:)

  1.Start by choosing the size of your word grid. The options are: 10*10 / 15*15 / 20*20 
  2.You will be provided with a list of words that you have to find in the word grid.
  3.If you find a word, you have to locate it by inputting its starting position(first letter) and ending position(last letter) respectively. 
  4.When you input a position, please enter the column number first then the row number and separate the two numbers by a space. e.g. For the grid below, the correct input for F is "2 1". 
           0  1  2
        0  A  B  C  0
        1  D  E  F  1
        2  G  H  I  2
           0  1  2
  5.After you have found all the words in the list, the game ends:)
  **Input the word "quit" if you want to quit after the game has started**
       
''')
    if sure()=="n":
      print(Fore.WHITE+'''
————————————————————————————
''')
      intro()
      continue
    print(Fore.BLUE+'''
    
Enjoy your game!
''')
    print(Fore.WHITE+'''
————————————————————————————
''')
    while True:
      a=input(Fore.WHITE+"Which grid size do you want to play: 10 / 15 / 20 ") #asking user for the preferred grid size
      if a=="10":
        size=10 #size of word grid
        count=5 #number of words user needs to find
        break
      elif a=="15":
        size=15
        count=8
        break
      elif a=="20":
        size=20
        count=10
        break
    wordsearchset(size,count) #passing the size and count to the function to create the word grid
    q=0
    while True:
      if wordsearchmain(size)==0:#quit the game
        q=1
        break
      if count==0:
        break
    if q==1:
      playagain()
      continue
    printgrid(size)
    print("")
    print(Fore.GREEN+"Congratulations!!🤩 You have found all the words!")
    playagain()
    
  elif gamechoice=="4": #hidden word
    print(Fore.WHITE+'''
————————————————————————————
''')
    print(Fore.BLUE+'''Welcome to Hidden Words!!!

Here are the rules:)

    1.Start by choosing a level and a topic you wish to play.
    2.You will be provided with a word grid containing randomly selected hidden words related to the topic you have chosen.
    3.Enter the words(no spaces) you found in the word grid that are related to the chosen topic. If your input is correct, the word will be highlighted in the word grid. Your goal is to find all the hidden words in the word grid. Note that entering a word that seems related but is marked wrong indicates it's not part of the computer's selection —— try finding other possibilities!
    4.If you find yourself stuck finding the words, you can input a "h" to get a hint(the first two letters of a word). 
    5.If you find the level too easy or too hard and want to change it, input the letter "l" to rechoose a level. 
    6.After you have found all the hidden words, the game ends:)
    **Input the word "quit" if you want to quit after the game has started**
    
''')
    if sure()=="n":
      print(Fore.WHITE+'''
————————————————————————————
''')
      intro()
      continue
    print(Fore.BLUE+'''
    
Enjoy your game!
''')
    print(Fore.WHITE+'''
————————————————————————————
''')
    size=count=0 
    while True:
      while True: #choosing level
        a=input(Fore.WHITE+'''
Choose your level:

Easy - finding 1 word in 5*5 grid
Medium - finding 3 words in 10*10 grid
Hard - finding 5 words in 15*15 grid
Expert - finding 10 words in 20*20 grid (Very Hard)

(1-Easy / 2-Medium / 3-Hard / 4-Expert) ''')
        if a=="1" or a.upper()=="EASY": #accept both lowercase and uppercase input, or number
          size=5
          count=1
          break
        elif a=="2" or a.upper()=="MEDIUM":
          size=10
          count=3
          break
        elif a=="3" or a.upper()=="HARD":
          size=15
          count=5
          break
        elif a=="4" or a.upper()=="EXPERT":
          size=20
          count=10
          break
      wordsearchset(size,count)
      q=0
      while True:
        a=hiddenmain()
        if a==0: #rechoose the level if it's too hard/easy
          q=1
          break
        elif a==1:#quit hidden word, and rechoose a game
          q=2
          break
        if count==0:
          break
      if q==1:  #rechoose level
        continue
      elif q==2: #quit the game
        playagain()
        break
      hiddengrid(size)
      print("")
      print(Fore.GREEN+"Congratulations!!🤩 You have found all the words!")
      playagain()
      break

    