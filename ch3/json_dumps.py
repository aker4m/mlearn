import json

price = {
    "date": "2018-01-21",
    "price":{
        "Apple":80,
        "Orange":55,
        "Banana":40
    }
}

s = json.dumps(price)
print(s)
