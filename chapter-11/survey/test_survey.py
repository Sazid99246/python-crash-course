import pytest
from survey import AnnonymousServey

@pytest.fixture

def language_survey():
    """A survey that will be available to all test functions."""
    question = "What languages did you first learn to speak?"
    language_survey = AnnonymousServey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('Bengali')
    assert 'Bengali' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ["Bengali", "English", "Arabic"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses