import time

""" time.time(): returns the current time in seconds since  (January 1, 1970, 00:00:00 UTC) """
start_time = time.time()

questions={"What is the largest ocean on Earth?": "Pacific Ocean", 
           "What is the boiling point of water in Celsius?": "100",
           "Who is the author of 'To Kill a Mockingbird'?": "Harper Lee",
           "What is the chemical symbol for gold?": "Au",
           "What is the largest planet in our solar system?": "Jupiter",
           }

score_counter=0

""" for loop: Because the quiz has a known ending point (once every question's been asked) """
for question, answer in questions.items():
    print(question)
    answer_input = input("What is your answer? ").lower().strip() 

    if answer_input==answer.lower().strip():
        print("Correct!")
        score_counter += 1

    else:
        print(f"Incorrect. The correct answer is: {answer}")

print(f"Your final score is: {score_counter}/{len(questions)}")

end_time = time.time()
time_spent = end_time - start_time
print(f"Quiz completed in {time_spent:.2f} seconds.")
""" .2f: formats time_spent as a floating-point number with 2 decimal places """
