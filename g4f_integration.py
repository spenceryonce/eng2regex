import g4f

def generate_regex_from_english(englishInput: str, exampleText: str, exampleResultText: str):
    """
    This function takes English instructions, example text, and example expected result text to generate a regex pattern using the g4f library.
    
    Parameters:
    - englishInput: A string containing the English instructions for the regex pattern.
    - exampleText: A string containing the example text to be used with the regex.
    - exampleResultText: A string containing the example of the expected result from the regex.
    
    Returns:
    - A string containing the generated regex pattern.
    """
    messages = [
        {"role": "user", "content": "You are an english to regex translator. You will be given instructions in english for what the regex is to do, and an example text to operate upon, and an example text to demonstrate the expected found characters with the regex.\n You will only generate javascript regex code. You will not say any words in english. You will not ask the user for any questions, you will only generate javascript regex code that meets the users requirements. The user will give you their request now. \n USER REQUEST BEGIN: "},
        {"role": "user", "content": f"English Input: {englishInput} \n Example Text: {exampleText} \n Example Result Text: {exampleResultText}"}
    ]
    
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=messages
    )
    
    # Assuming the response object has a 'choices' attribute with the regex pattern in its 'text' attribute.
    # This might need adjustment based on the actual structure of the response from g4f.
    regex_pattern = response.choices[0].text.strip() if response.choices else "No regex generated."
    
    return regex_pattern
