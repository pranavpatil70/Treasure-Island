print("Welcome to the treasure island!\nYour mission is to find the treasure!")
direction = input("Which direction you wanna go?")

if direction == "right":
    print("Game Over!")
else:
    way = input("You wanna swim or wait?")
    
if way == 'swim':
    print("game over!")
else:
    door = input("Select a door you wanna go from: red, Blue or Yellow?")

if door == "yellow":
    print("You Win!!!")
elif door == "red":
    print("it's the house full of fire! You lose")
elif door == 'blue':
    print("Game Over, You Lose!")