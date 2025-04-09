import unicodedata

def hindi_tokenizer(text):
    """Basic Tokenizer for splitting text into unicode points"""
    normalized=unicodedata.normalize('NFC',text)
    return [ord(char) for char in normalized]

def decode_tokens(tokens):
    """Convert token codes back to text"""
    return ''.join(chr(token) for token in tokens)



# Hindi text sample

hindi_text = "यह एक हिंदी भाषा का उदाहरण है।" #Can be updated to take hindi text input from user 
hindi_tokens = hindi_tokenizer(hindi_text)
decoded_text = decode_tokens(hindi_tokens)

print("\nHindi text tokens\n", hindi_tokens)

print("\nDecoded tokens\n", decoded_text)


#unicode vocab size 137k approx