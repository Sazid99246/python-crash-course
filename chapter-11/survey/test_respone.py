from survey import AnnonymousServey

def test_store_single_response():
    """Test that three single responses ares stored properly."""
    question = "What languages did you first learn to speak?"
    language_survey = AnnonymousServey(question)
    responses = ["Bengali", "English", "Arabic"]
    for response in responses:
        language_survey.store_response(response)
        assert response in language_survey.responses