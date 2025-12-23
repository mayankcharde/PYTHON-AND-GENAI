import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")

#  HENCE THIS TEXT WILL GENERATE SUM TOKENS THROUGH AI MODEL
text =" hey my name is mayank charde"
tokens = enc.encode(text)

# Tokens:  [45233, 922, 1308, 382, 1340, 1104, 549, 11236]
print("Tokens: ", tokens)

decoded = enc.decode( [45233, 922, 1308, 382, 1340, 1104, 549, 11236])
print("Decoded", decoded)
