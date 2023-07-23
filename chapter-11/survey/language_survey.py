from survey import AnnonymousServey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
language_survey = AnnonymousServey(question)

# Show the question and store responses to the question
language_survey.show_questions()
print("Enter 'q' at any time to quit.")
while True:
    response = input("language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey result
print("\nThank you to everyone who participated in the survey.")
language_survey.show_results()