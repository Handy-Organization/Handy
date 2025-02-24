#Text-Gloss-Model

from transformers import MarianMTModel, MarianTokenizer

# Define the model name for Hebrew to English translation
MODEL_NAME = "Helsinki-NLP/opus-mt-he-en"

# Load the tokenizer and model (this may download the model the first time)
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_hebrew_to_english(hebrew_text: str, max_length: int = 128) -> str:
    """
    Translates a single Hebrew sentence into English.
    
    Parameters:
      - hebrew_text (str): The input sentence in Hebrew.
      - max_length (int): The maximum token length for input and output (default 128).
    
    Returns:
      - str: The translated English sentence.
    
    Note:
      128 is a reasonable limit for most sentence-level inputs.
      If you expect longer inputs, you can increase this value.
    """
    # Tokenize the Hebrew text with truncation to handle long inputs
    inputs = tokenizer(hebrew_text, return_tensors="pt", truncation=True, max_length=max_length)
    
    # Generate the translated output tokens
    translated_ids = model.generate(**inputs, max_length=max_length)
    
    # Decode the tokens to obtain the English text
    english_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    return english_text

# Example usage:
if __name__ == "__main__":
    # Sample Hebrew input (modify as needed)
    sample_hebrew = "הכנס טקסט בעברית"
    print("Hebrew Input:", sample_hebrew)
    
    english_output = translate_hebrew_to_english(sample_hebrew)
    print("Translated English:", english_output)
