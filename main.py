
name = input("enter name: ")
word = "eyoya"
guess = " "
guess_count = 1
guess_limit = 4
out_of_guesses = False

while guess != word and not out_of_guesses:
    guess = (input("enter guess: "))
    if guess_count < guess_limit:
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print(f"{name}" + "! YOU DUMB. THE ANSWER WAS  " + f"{word}")
else:
    print("how did you know! " + f"{name}")