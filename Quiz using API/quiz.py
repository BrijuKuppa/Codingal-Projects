import requests
import html
import random

amount = 1
url = f"https://opentdb.com/api.php?amount={amount}&category=9&type=multiple"

def get_questions():
    questions = requests.get(url)
    if questions.status_code == 200:
        parse = questions.json()
        if parse["response_code"] == 0 and parse["results"]:
            return parse["results"]
        else:
            return None
    
def main():
    questions = get_questions()
    if not questions:
        questions = []
        print("There was an error getting the questions.")
    
    loop = len(questions)
    print("\n\nWelcome to Trivia!")
    print(f" Category: {questions[0]["category"]}")
    print(f" Amount of questions: {loop}")
    print("Make sure to put the number or put the option exactly how it is in your answer.")
    print("Read to start?")
    choice = input(">")
    result = 0

    if choice == "yes" or choice == "y":
        for i in range(loop):
            question_of_quiz = html.unescape(questions[i]["question"])
            correct = html.unescape(questions[i]["correct_answer"])
            incorrect = html.unescape(questions[i]["incorrect_answers"])
            answers = incorrect + [correct]
            random.shuffle(answers)

            print(f"\n{question_of_quiz}")
            for index, answer in enumerate(answers, 1):
                print(f" {index}. {answer}")

            option = input(">")

            if option == correct or option.isdigit() and int(option) - 1 == answers.index(correct):
                print("Your answer is correct!")
                result += 1
            else:
                print("Your answer is wrong.")


        percentage = round(result / loop * 100, 2)
        print("\nYour quiz is complete.")
        print(f" Your results are: {result} / {loop}. ({percentage}%)")
        if percentage >= 90:
            print("Nice job on your quiz!")
        elif percentage >= 80 and percentage < 91:
            print("Not bad at all!")
        elif percentage >= 70 and percentage < 81:
            print("Not the best, you can do better!")
        elif percentage >= 60 and percentage < 71:
            print("Not great, try another quiz!")
        else:
            print("Thats a failing score, you should try another quiz.")

        print("\nWould you like to start over?")
        action = input(">")

        if action == "yes" or action == "y":
            print("\nLets start over...")
            main()
        else:
            print("Quiz you later!\n")
            exit()
    else:
        print("Lets start the quiz later.")

    
if __name__ == "__main__":
    main()