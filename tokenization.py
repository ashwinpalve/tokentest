from json import encoder
import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size", encoder.n_vocab)

text = "Much Ado about nothing\n"
tokens = encoder.encode(text)

print("\nTokens", tokens)

mytokens = [54041, 355, 2408, 1078, 6939]
decoded = encoder.decode(mytokens)

print("\nDecoded", decoded)

# Hindi Text tokenization 

# Hindi text sample
hindi_text = "यह एक हिंदी भाषा का उदाहरण है।"
hindi_tokens = encoder.encode(hindi_text)
print("\nHindi text tokens\n", hindi_tokens)

# Full decoding
decoded_text = encoder.decode(hindi_tokens)
print("\nDecoded Text:\n", decoded_text)

