def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0 

    for key in question:
        print("-------------------------------")
        print(key)
        # Using nested for loop for displaying options
        for i in options[question_num]:
            print(i)

        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question[key], guess)
        question_num += 1  # Increment question_num after each question

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------")
    print("RESULTS")
    print("-------------------")

    print("Answers: ", end="")
    for i in question.values():
        print(i, end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = ((correct_guesses/len(question))*100)
    print("Your score is: "+str(score)+"%")


def play_again():
    response = input("Do you want to play again? (yes or no): ")


# Dictionary for questions and options
question = {
    "What is the largest planet in our solar system?: ": "C",
    "Who painted the Mona Lisa?: ": "D",
    "What is the capital city of Australia?: ": "C",
    "Which famous scientist developed the theory of relativity?: ": "B",
    "What is the chemical symbol for gold?: ": "C"
}

options = [["a. Earth ", "b. Mars", "c. Jupiter", "d. Saturn"],
           ["a. Michelangelo", "b. Vincent van Gogh", "c. Pablo Picasso", "d. Leonardo da Vinci"],
           ["a. Sydney", "b. Melbourne", "c. Canberra", "d. Brisbane"],
           ["a. Isaac Newton", "b. Albert Einstein", "c. Marie Curie", "d. Galileo Galilei"],
           ["a. Gd", "b. Ag", "c. Au", "d. Pt"]]

new_game()
