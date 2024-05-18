import random
import time
import itertools
import threading
import sys

done = False


print("Hello my name is jarvis")
time.sleep(3)

print("The game is about to start...")
time.sleep(2)


def animate(): #this is for the loading screen animation
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\rloading {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone! ')

t = threading.Thread(target=animate)
t.start()

# Your long process here
time.sleep(10)
done = True


print("\n welcome to hangman!!") #greetings
time.sleep(2)

words = ["hacker", "docker", "ethical"] #word list that we have created

secret_word = random.choice(words) #system chooses a word randomly
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

num = 0
game_over = False

while not game_over:
   
    guess = input("enter the letter").lower()

    for position in range(len(secret_word)): 
   
        letter = secret_word[position]
          
        if letter == guess:
            display_word[position] = letter 
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print("you have", guesses_left, "guesses left ")
        if num >= 5:
            print("you loser")
            game_over = True
                     
    print(display_word)

    if "_" not in display_word:
        print("you win")
        game_over = True