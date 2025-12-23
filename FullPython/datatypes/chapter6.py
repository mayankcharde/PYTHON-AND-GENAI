chai_type = "Ginger chai"
customer_name = "mayank"

print(f" oreder for { customer_name} : {chai_type}")

chai_desc = "aromatic and bold"

print(f"First word: {chai_desc[:8]}")
print(f"Last word: {chai_desc[12:]}")
#  YE SENTENCE KE SAATH WORDS KO BHI ULTA KR DEGA
print(f"Last word: {chai_desc[::-1]}")


label_text = "chai special"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")