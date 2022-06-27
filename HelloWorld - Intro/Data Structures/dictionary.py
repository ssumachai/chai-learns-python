customer = {
    "name": "Im Nayeon",
    "color": "baby blue",
    "number": 9,
    "is_verified": True
}

print(customer.get("name"))
print(customer.get("favorite song", "Baby Blue Love"))

customer["is_verified"] = False
print(customer["is_verified"])


# Exercise

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!") + ' '
print(output)