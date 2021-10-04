#dict, list, boolean
#key-value
car = {
    "color": 50,
    50:[1, 2, 3, 4, 5,6 ],
    "fuel_consumption":"low",
    "is_suv": True
}
print(car[50])
if car["is_suv"]:
    print(car["color"])

car["color"] = "red"
print(car)
