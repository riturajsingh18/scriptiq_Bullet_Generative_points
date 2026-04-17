from services.llm_service import call_llm

def analyze_script(script):

    prompt = f"""
    Analyze this script and return structured output:

    Script:
    {script}

    Return:
    1. Summary (3-4 lines)
    2. Emotional tone
    3. Engagement score (0-10)
    4. Improvements
    5. Cliffhanger moment
    """

    return call_llm(prompt)