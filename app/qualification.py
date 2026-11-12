def qualify_lead(message: str) -> str:
    """Return a transparent baseline priority; this is not an AI model."""
    text = message.casefold()

    high_intent = (
        "urgent",
        "today",
        "this week",
        "ready to book",
        "as soon as possible",
    )
    medium_intent = (
        "price",
        "pricing",
        "quote",
        "cost",
        "interested",
        "appointment",
        "book",
    )

    if any(term in text for term in high_intent):
        return "high"
    if any(term in text for term in medium_intent):
        return "medium"
    return "low"
