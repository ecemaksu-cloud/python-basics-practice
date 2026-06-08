# Count how many times the letter 'a' appears in a sentence

count = 0
text = "hello world"

for character in text:
    if character == "a":
        count += 1

print("Count =", count)
