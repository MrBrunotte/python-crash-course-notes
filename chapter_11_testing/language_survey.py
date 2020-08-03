from survey import AnonymousServey

# Define a question and maka a survey
question = "What language did you first speak?"
my_survey = AnonymousServey(question)

# Show the question, and store the response
my_survey.show_question()
print("\nEnter 'q' at any time to quit!\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey result
print("\nThanks for participating in the survey!")
my_survey.show_results()
