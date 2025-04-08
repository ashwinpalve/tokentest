from json import encoder
import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size", encoder.n_vocab)

text = "Much Ado about nothing"
tokens = encoder.encode(text)

print("Tokens", tokens)

mytokens = [54041, 355, 2408, 1078, 6939]
decoded = encoder.decode(mytokens)

print("Decoded", decoded)