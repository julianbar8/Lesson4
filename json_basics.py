import json
car_data = {"name":"tesla","engine":"electric"} #dictionary

#print(type(car_data))

#2 methods in json

# json.dumps() - serialises json to a forward string
# json.dump() - create stream object and expects a file object to write to

# car_data_json_string = json.dumps(car_data)
#
# print(car_data_json_string)
#
# print(type(car_data_json_string))

with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data,jsonfile)

#using json.load

with open("new_jason_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print (car['name'])
    print (car['engine'])

