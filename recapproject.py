def recap_function(totals, limit):
    for item in totals:
        print(item["name"])
        if item["total"] >= limit:
            print("Item is greater or equal to limit")
        else:
            print("needs to be upgraded")
            diff = limit - item["total"]
            item["total"] += diff
        print(item["total"])
    


food_list = [
    {
"name": "egg",
"total": 50
        },
    {
"name": "beans",
"total": 80
        },
    {
"name": "rice",
"total": 30
        },
    {
"name": "carrot",
"total": 35
        },
    {
"name": "apple",
"total": 45
        },
    {
"name": "cucumber",
"total": 52
        },
    {
"name": "bread",
"total": 60
        },
    {
"name": "spaghetti",
"total": 50
        },
    {
"name": "macaroni",
"total": 90
        },
    ]

recap_function(food_list, 50)
