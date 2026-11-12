from app.qualification import qualify_lead


def test_urgent_message_is_high():
    assert qualify_lead("I need help today, this is urgent.") == "high"


def test_pricing_question_is_medium():
    assert qualify_lead("Can you send me your pricing?") == "medium"


def test_general_message_is_low():
    assert qualify_lead("I would like to learn more about your business.") == "low"
