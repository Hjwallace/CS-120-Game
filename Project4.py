#Hunter Wallace | Project 4
# December 8th, 2017

#Make some kind of score
  #Lose points if you attack a guard
  #Lose points if you trip the alarm
#Items
  #File - get it and escape
  #ScrewDriver - opens easy escape
  #Paper - gives passcode to avoid alarm
#Bonus: Have items displayed

#----------Rooms----------
#Enteryway x=537, y = 529
#Lobby x=537, y=447
#Office x=394,449
#Hall 1 400,388
#Guard Room 409,300
#Back Room 410,251
#Hall 2,483,301
#Hall 3 503,236
#Pathway 1 558,350
#Pathway 2 558,236
#Helipad 556,154
#Lab 702,452
#Closet 782,446
#File Room 711,364
#Air Vent 1 710,246
#Air Vent 2 596,234
#-------------------------------

from random import randint

map = makePicture(getMediaPath("map.png"))
disc = makeSound(getMediaPath("discover.wav"))
gameOver = makeSound(getMediaPath("gameover.wav"))
winning = makeSound(getMediaPath("win.wav"))
filePic = makePicture(getMediaPath("file.jpg"))
gOne = "guard room"
gTwo = "guard room"
file = "file room"
fileNum = 0
gLoc = 0
win = 0



def adventure():
  global win
  global gOne
  global gTwo
  location = "entryway"
  name = requestString("What is your name?")
  intro(name)
  show(map)
  endgame = ""
  while location!="exit" or win != 1:
    wipe(location)
    wipe(gOne)
    wipe(gTwo)
    marker(location,green)
    repaint(map)
    roomNoises(location)
    guards(location)
    marker(gOne,red)
    marker(gTwo,red)
    repaint(map)
    showRoom(location)
    direction = requestString("Which direction?").lower()
    printNow("==============================================")
    printNow("You typed: "+ direction)
    location = pickRoom(direction,location)
    location = lose(location)
    

#------Room Navigator---------
def pickRoom(direction,room):
  if (direction == "quit") or (direction == "exit"):
    showInformation("Goodbye!")
    return "exit"
  if direction == "help":
    showIntroduction()
    return room
#-------------Entry Options----------
  if room == "entryway":
    if direction == "north":
      return "lobby"
    else:
      return "entryway"
#---------Lobby Options----------
  if room == "lobby":
    if direction == "north":
      return "path one"
    if direction == "east":
      return "lab"
    if direction == "south":
      return "entryway"
    if direction == "west":
      return "office"
#-------------------Office Options ------------
  if room=="office":
    if direction == "north":
      return "hall one"
    if direction == "east":
      return "lobby"
    else:
      return "office"
#-------------------Lab Options ------------      
  if room=="lab":
     if direction == "north":
      return "file room"
     if direction == "east":
      return "closet"
     if direction == "west":
       return "lobby"
     else:
      return "lab"
#-------------------Closet Options ------------
  if room=="closet":
    if direction == "west":
      return "lab"  
    else:
      return "closet" 
#-------------------File Room Options------------
  if room=="file room":
    if direction == "north":
      return "air vent one" 
    if direction == "south":
      return "lab"  
    else:
      return "file room"   
#-------------------Path One Options  ------------
  if room=="path one":
    if direction == "north":
      return "path two"  
    if direction == "south":
      return "lobby"  
    if direction == "west":
      return "hall two"  
    else:
      return "path one"   
#-------------Hall One Options----------
  if room == "hall one":
    if direction == "south":
      return "office"
    if direction == "north":
      return "guard room"
    else:
      return "hall one"
#-------Guard Room options---------
  if room == "guard room":
    if direction == "north":
      return "back room"
    if direction == "east":
      return "hall two"
    if direction == "south":
      return "hall one"
    else:
      return "guard room"
#-------Hall Two options---------
  if room == "hall two":
    if direction == "west":
      return "guard room"
    if direction == "east":
      return "path one"
    else:
      return "hall two"
#-------Back Room options--------- 
  if room == "back room":
    if direction == "south":
      return "guard room"
    if direction == "east":
      return "hall three"
    else:
      return "back room"
#-------Hall Three options--------- 
  if room == "hall three":
    if direction == "east":
      return "path two"
    if direction == "west":
      return "back room"
    else:
      return "hall three"

#-------Path two options---------
  if room == "path two":
    if direction == "north":
      return "helipad"
    if direction == "east":
      return "air vent one"
    if direction == "south":
      return "path one"
    if direction == "west":
      return "hall three"
    
#-------Air Vent one options---------
  if room == "air vent one":
    if direction == "west":
      return "air vent two"  
    if direction == "south":
      return "file room"
    else:
      return "air vent one"

#-------Air Vent Two options---------
  if room == "air vent two":
    if direction == "east":
      return "air vent one"  
    if direction == "west":
      return "path two"
    else:
      return "air vent two"
          
#-------Helipad options---------
  if room == "helipad":
    if direction == "south":
      return "path two"
      
#--------------------------------------------------
#--------------------------------------------------  
                                                                                                                                
#-------Room Description Activators-------
def showRoom(room):
 printNow("==============================================")
 if room =="entryway":
   showEntryWay() #DONE
 if room == "lobby":
   showLobby() #DONE
 if room=="office":
   showOffice() #DONE
 if room=="hall one":
   showHallOne()#DONE
 if room=="guard room":
   showGuardRoom() #DONE
 if room=="back room":
   showBackRoom() #DONE
 if room=="hall two":
   showHallTwo() #DONE
 if room=="hall three":
   showHallThree() #DONE
 if room=="path one":
   showPathOne() #DONE
 if room=="path two":
   showPathTwo() #DONE
 if room=="helipad":
   showHelipad() #DONE
 if room=="lab":
   showLab() #LAB
 if room=="closet":
   showCloset() #DONE
 if room=="file room":
   showFileRoom() # DONE
 if room=="air vent one":
   showAvOne() #DONE
 if room=="air vent two":
    showAvTwo()#DONE
    
#---Room Story Board---
def showEntryWay():
  ew = "You sit outside of a large building. You see multiple cameras and towers guarding the area. You disable the front door security. You can now enter the building."
  showInformation(ew)

def showLobby():
  L = "You walk in to the building's lobby. A large logo lays on the floor and a desk stands in middle. No one is at it though, that seems odd.You look east to see an office, west to see the lab, and north to go down a long hall way."
  showInformation(L)

def showOffice(): 
  off = "You walk in to an office. Papers are cluttered all around the room, it seems like someone was trying to get rid or hide something. You rummage around and see something under a coffee mug"
  showInformation(off)
  showInformation("You look north and see a hall into some large room")

def showHallOne():
  ho = "You move down the hall quietly. You see a large room ahead of you. Something seems ominous about it"
  showInformation(ho)

def showGuardRoom():
  gr = "You walk into a large room. One wall is stocked with weapons and armor. This must be the guard room. You look to the wall and see camera's of every room. The guards seem aware of your presence and are searching the building. You take note of their positions"
  showInformation(gr)
#print guard one position
#print two
#print three

def showBackRoom():
  showInformation("You walk into a small room. Nothing interesting to be honest besides a water cooler")

def showHallTwo():
  showInformation("You switfly move through the hall, narrowly avoid some spilt coffee")
  
def showHallThree():
  showInformation("Just another hall. You see the long passageway at the end of it.")
  
def showPathOne():
  po = "You walk into the main corridor in the building. It's a long and bleak sight, not giving much to the imagination. You see some plants and some benches, it's no time to sit down though."
  showInformation(po)

def showPathTwo():
  showInformation("You walk down the passage way and reach the end of the hall. The door in front seems to lead outside.")
  
def showHelipad():
  global win
  global fileNum
  showInformation("You walk outside on to a helipad. A helicopter awaits you but you still need something")
  if fileNum == 1:
    win += 1
    showInformation("Great job Agent. ||MISSION COMPLETE||")
    play(winning)
    showInformation("Restarting mission.....")
    adventure()
    
    
def showLab():
  showInformation("You sneak into the lab. You see strange vials lining the walls. Papers are scattered all over the floor and some vials are broken. Seems like someone was in a hurry.")
  #DO FANCY KEY CODE STUFF HERE
def showCloset():
  showInformation("You open the door and walk into a small closet. Nothing special here, just a broom, mop and water, and some cleaning supplies. You notice a key though and decide to take it.")

def showFileRoom():
  global filePic
  global map
  showInformation("You finally reach the file room. You scour around and finally find what you need. It's time to get out and escape")
  file()
  paste(filePic,map,4,38)
  
def showAvOne():
  showInformation("You move through the vent working your way to the exit")
  
def showAvTwo():
  showInformation("You move through the vent working your way to the exit")
#------Intro-------
def intro(name):
 tro1 = "Welcome Agent " + name + "."
 showInformation(tro1)
 tro2 = "You must sneak into lab and steal the file. You can move north, south, east, or west in order to naviagte the lab. We've given you a map to find your way. **Watch out for guards though. If you are caught, you lose.**"
 showInformation(tro2)
 tro3 = "Good luck Agent " + name
 showInformation(tro3)
 showInformation("PS: Type quit or exit to leave the game")

#------Room Noises-------------
def roomNoises(location):
  #-------Entry-------
  entryway = 0
  if entryway != 1:
    if location == "entryway":
      play(disc)
      entryway += 1
      
  #-------Lobby-------
  lobby = 0
  if lobby != 1:
    if location == "lobby":
      play(disc)
      lobby += 1
      
  #------Office-------
  office = 0
  if office != 1:
    if location == "office":
      play(disc)
      office += 1
      
  #------Hall One-------
  hallone = 0
  if hallone != 1:
    if location == "hall one":
      play(disc)
      hallone += 1
      
  #------Guard Room-------
  guardroom = 0
  if guardroom != 1:
    if location == "guard room":
      play(disc)
      guardroom += 1 
       
  #-------Back Room-------
  backroom = 0
  if backroom != 1:
    if location == "back room":
      play(disc)
      backroom += 1
      
  #------Hall Two-------
  halltwo = 0
  if halltwo != 1:
    if location == "hall two":
      play(disc)
      halltwo += 1
      
  #-------Hall Three-------
  hallthree = 0
  if hallthree != 1:
    if location == "hall three":
      play(disc)
      hallthree += 1
      
  #------Lab-------
  lab = 0
  if lab != 1:
    if location == "lab":
      play(disc)
      lab += 1
      
  #------Closet-------
  closet = 0
  if closet != 1:
    if location == "closet":
      play(disc)
      closet += 1 
      
  #-------File Room-------
  fileroom = 0
  if fileroom != 1:
    if location == "file room":
      play(disc)
      hallthree += 1
      
  #------Air Vent 1-------
  av1 = 0
  if av1 != 1:
    if location == "air vent one":
      play(disc)
      av1 += 1
      
  #------Air Vent 2-------
  av2 = 0
  if av2 != 1:
    if location == "air vent two":
      play(disc)
      av2 += 1 
  
  #------Pathway 1-------
  pw1 = 0
  if pw1 != 1:
    if location == "pathway one":
      play(disc)
      pw1 += 1
      
  #------Pathway 2-------
  pw2 = 0
  if pw2 != 1:
    if location == "pathway two":
      play(disc)
      pw2 += 1 
      
  #------Helipad-------
  hp = 0
  if hp != 1:
    if location == "helipad":
      play(disc)
      hp += 1
      
def marker(location,color):
  if location == "entryway":
    for x in range(537,547):
      for y in range(529,539):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "lobby":
    for x in range(537,547):
      for y in range(447,457):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "office":
    for x in range(394,404):
      for y in range(449,459):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "hall one":
    for x in range(400,410):
      for y in range(388,398):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "guard room":
    for x in range(409,419):
      for y in range(300,310):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "back room":
    for x in range(410,420):
      for y in range(251,261):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "hall two":
    for x in range(483,493):
      for y in range(301,311):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "hall three":
    for x in range(503,513):
      for y in range(236,246):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "path one":
    for x in range(558,568):
      for y in range(350,360):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "path two":
    for x in range(558,568):
      for y in range(236,246):
        p = getPixel(map,x,y)
        setColor(p,color)
  
  if location == "helipad":
    for x in range(581,591):
      for y in range(161,171):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "lab":
    for x in range(702,712):
      for y in range(452,462):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "closet":
    for x in range(782,792):
      for y in range(446,456):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "file room":
    for x in range(711,721):
      for y in range(364,374):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "air vent one":
    for x in range(710,720):
      for y in range(246,256):
        p = getPixel(map,x,y)
        setColor(p,color)
        
  if location == "air vent two":
    for x in range(596,606):
      for y in range(234,244):
        p = getPixel(map,x,y)
        setColor(p,color)
      
  
def wipe(location):
    for x in range(537,547):
      for y in range(529,539):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(537,547):
      for y in range(447,457):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(394,404):
      for y in range(449,459):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(400,410):
      for y in range(388,398):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(409,419):
      for y in range(300,310):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(410,420):
      for y in range(251,261):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(483,493):
      for y in range(301,311):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(503,513):
      for y in range(236,246):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(558,568):
      for y in range(350,360):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(558,568):
      for y in range(236,246):
        p = getPixel(map,x,y)
        setColor(p,white)
  
    for x in range(581,591):
      for y in range(161,171):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(702,712):
      for y in range(452,462):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(782,792):
      for y in range(446,456):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(711,721):
      for y in range(364,374):
        p = getPixel(map,x,y)
        setColor(p,white)
        
    for x in range(710,720):
      for y in range(246,256):
        p = getPixel(map,x,y)
        setColor(p,white)
   
    for x in range(596,606):
      for y in range(234,244):
        p = getPixel(map,x,y)
        setColor(p,white)
        
def lose(location):
  global gOne
  global gTwo
  if gOne == location or gTwo == location:
    play(gameOver)
    showInformation("You got caught by guards. ||MISSION FAILED||")
    redo = requestString("Play Again?(Y/N)").lower()
    if redo == "y":
      adventure()
    if redo == "n":
      return "exit"
  else:
    return location
#------------------------
def guards(location):
  global gOne
  onePos = randint(1,4)
  if onePos ==1:
      gDir = "north"
  if onePos == 2:
      gDir = "east"
  if onePos == 3:
      gDir = "south"
  if onePos == 4:
      gDir = "west"
  gOne = pickRoom(gDir,gOne)

  global gTwo
  twoPos = randint(1,4)
  if twoPos == 1:
      gDir2 = "north"
  if twoPos == 2:
      gDir2 = "east"
  if twoPos == 3:
      gDir2 = "south"
  if twoPos == 4:
      gDir2 = "west"
  gTwo = pickRoom(gDir2,gTwo)
#-------------------------
def file():
  showInformation("You picked up the file")
  global fileNum
  fileNum += 1
  
def paste(picture,canvas,xCord,yCord):
  targetX = xCord
  for sourceX in range(0,getWidth(picture)):
    targetY = yCord
    for sourceY in range(0,getHeight(picture)):
      color = getColor(getPixel(picture,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY +1
    targetX = targetX +1

                                                                                                                                            