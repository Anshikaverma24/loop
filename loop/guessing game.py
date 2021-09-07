# GUESSING GAME

# WHILE LOOP
i=0
while i<=4:
 guessed_number=int(input("guessd the number-"))
 if guessed_number==4:
   print("woah! you win")
   break
 elif guessed_number!=4:
  print("wrong, you loose one chance")
 else:
    print("you loose")
 i+=1