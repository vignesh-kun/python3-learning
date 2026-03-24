#To create a number guessing game

numb = int(10)
while True:
    print("Number is between 1 and 100")
    print("Guess the number: ");
    no = int(input())
    if(no>numb):
        print("U guessed too high")
        continue
    elif(no<numb):
        print("U guessed too low")
        continue
    else:
        print("U guessed right")
        break

print("Thx for playing!")

