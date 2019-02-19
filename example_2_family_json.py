import json
import family_data

#Creates and returns a Family object(defined in example_data) from loaded json_data
def make_family_from_json(json_data):

    new_family = family_data.Family()

    #stoping here is a good check that this is a dictionary
    new_family.parents = json_data["parents"]


    for kid_json in json_data["kids"]:
        new_kid = family_data.Kid()
        new_kid.age = kid_json["age"]
        new_kid.name = kid_json["name"]
        new_family.kids.append(new_kid)





    return new_family




with open("data/family.json", "r") as reader:
    family_json = json.load(reader)

print("JSON data:")
print(family_json)

family_data = make_family_from_json(family_json)
print()
print("Family data:")
print(family_data)