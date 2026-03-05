def build_analysis_prompt(text: str):
    return f"""
    Analyze the following text.

    Provide:
    1. A short summary
    2. Action items
    3. Key decisions

    Text:
    {text}
    """