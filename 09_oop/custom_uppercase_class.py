# Custom uppercase converter using a class

class TextConverter:

    def __init__(self, city):
        self.city = city

    def to_uppercase(self, text=""):
        result = ""

        for char in text:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char

        return result


city_name = "Ankara"
print(city_name.upper())

converter = TextConverter("Ardahan")

print("Type of city_name:", type(city_name))
print("Type of converter:", type(converter))

print(converter.to_uppercase("ardahan"))
