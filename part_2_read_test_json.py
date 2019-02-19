import json
import test_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):





    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    game_library.games = json_data["games"]

    print(game_library.games)







    return game_library


#Part 2
input_json_file = "data/test_data.json"

with open("data/test_data.json", "r") as reader:
    test_data_json = json.load(reader)

print("JSON data:")
print(test_data_json)
#
# test_data = make_game_library_from_json(test_data_json)
# print()
# print("Test data:")
# print(test_data)

