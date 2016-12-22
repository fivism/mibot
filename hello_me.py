## Hello World
import sys
import markovify

lines = int(sys.argv[1])
# Get raw text
with open("fixedlines.txt") as f:
    text = f.read()

# Build model
text_model = markovify.NewlineText(text)

# # Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(lines):
    print(text_model.make_short_sentence(160))
