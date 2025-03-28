import json

data = '{"firstName":"engin","lastName":"demiroğ"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])


customer = {
        "firstName":"engin",
        "email":"engindemirog@gmail.com"
        }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))
