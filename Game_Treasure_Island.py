print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
Left_or_Right = input("We are at the cross road. Life is like that my friend, you have to make choices. So! Which way would you like to take? Left or Right \n")
Left_or_Right = Left_or_Right.lower()
if Left_or_Right=="left":
  Swim_or_Wait = input("Wow! Here is a river in front of you, a treat for the eyes (only if you could stay!). There are two options, You choose? Swim or Wait \n")
  Swim_or_Wait = Swim_or_Wait.lower()
  if Swim_or_Wait=="wait":
    Choose_the_Door = input("Well! We! Thank god that was a big trout in the stream. Wait! What was that sound..... Three Doors have appeared behind you, Which one do you choose? Red, Blue or Yellow \n")
    Choose_the_Door = Choose_the_Door.lower()
    if Choose_the_Door=="yellow":
      print("You are now flying in those imaginary clouds with wings and body like hercules. YOU WIN!")
      print("Here is your Angel!")
      print(""" ___ .~- ` `' "' ` -~. ____
                 :~+.-`  .-"-.  .-"~._  `-.+~:
                 !  /  -`     `       `'--~:.l
                  :'         .              '.
                 /
                /-".        :  .            \`
                 .`      /.-"\ : `-  ^       :`
                 ^      "`    `.    \:'._  \ `!`
                :     :-===-.    .-===-.\  .!/'.
                 '.; /     .             : :
                : `.l   .mPm.\    .mPm.  |/    l
               .     :                   :':   |
                   \ '        d:         ' /   :
              :     '-:        "        :-;:   `
              .       .     ._..._.     :::`   _
             /        ::               ;::;.   !
            .      .  :;:.           .::::;:   '
            . :  : :  `:::'.       .'::::;::.   \
            '/.  .  .  `::l '-. .-' '|:::::::.   ;
            : |: :: ::__`.-.        _.-.::::::_  ;
            .~"` \ \ :`"/    `-..- `     \"`//    "~.
           /      \ \ .   ___ /\ ___      .//        \
          :        \ \.-`  _.~l)=~  `' -.:"
          `         '/  .    ":`-.       \            :
          .           -::    _lm.      .`         zi. |
                      \ /`-'  :::- ::.:
                       :       !:`   ":
                            :  .      '
                       "-._::  ^: .    ;
                            `-" \::_.~'
                             : : :
                             ' ' :
                               ' :""")
    elif Choose_the_Door=="blue":
      print("Woah! What are these beastly creatures, hoping they won't notice you. GAME OVER! Well, you got to see them.")
    elif Choose_the_Door=="red":
      print("You feel hot? And You are flying? NO! You are falling...... Into a fire! GAME OVER!")
      print("""(  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
    else:
      print("You should get a life man. You should have chosen a door my friend. GAME OVER!")
      print("""__
                              | \      _
                           ==='=='==  (o>
                              \++/   / )
                     __.-------------^^-.__
                        \----.  : .----/
                              \_/\|          ()
                              / _ \       _  \/()
                             / /|\ \     |/| | \/
                       snd _/_/ | \_\_     | |//
                          /_/   |   \_\    \_\|""")
  else:
    print("Wait! Wait! Wait! What is that? Oh No! You have been swallowed by a trout. GAME OVER!")
    print("Look at it!")
    print("""|
                 |
                ,|.
               ,\|/.
             ,' .V. `.
            / .     . \
           /_`       '_\
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-'""")   
else:
  print("Beep! Beep! You have fallen into a spiked pit. GAME OVER!")