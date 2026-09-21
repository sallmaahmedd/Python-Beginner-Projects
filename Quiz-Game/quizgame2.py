import random
import time

all_questions = {
    "What is the capital of France?": "Paris",
    "What is 4*8?": "32",
    "What planet is known as the Red Planet?": "Mars",
    "Who wrote Romeo and Juliet?": "Shakespeare",
    "What is the largest ocean on Earth?": "Pacific",
    "What gas do plants absorb from the air?": "Carbon Dioxide",
    "How many continents are there?": "7",
    "What is the boiling point of water in Celsius?": "100"
}


score_counter = 0
num_questions = 100
""" Limit the number of questions to the total available """
num_questions = min(num_questions, len(all_questions))

""" 
    random.sample() needs something it can index into and pick randomly from, it can't do that with a dict so it has to convert it to a list of tuples. 
    random.sample(the_list, num_questions) — picks num_questions distinct items(tuples) from that list, in random order, with no repeats. 
    This is different from calling random.choice() five times because choice() could accidentally pick the same question twice, but sample() guarantees each pick is unique.
"""
selected_questions = random.sample(list(all_questions.items()), num_questions)
questions = dict(selected_questions)

start_time = time.time()

for question, answer in questions.items():
    print(question)
    answer_input = input("What is your answer? ").lower().strip()
    if answer_input == answer.lower().strip():
        print("Correct!")
        score_counter += 1
    else:
        print(f"Incorrect. The correct answer is: {answer}")
end_time = time.time()
print(f"Your final score is: {score_counter}/{num_questions}")
print(f"Quiz completed in {end_time - start_time:.0f} seconds.")

