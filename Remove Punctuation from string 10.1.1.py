text = input()

result = ""

for char in text:
    if char.isalnum() or char == " ":
        result += char

print(result)
