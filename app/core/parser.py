def clean_requirement(text: str) -> str:
    """
    Normalize requirement text before sending to LLM
    """
    return text.strip()
