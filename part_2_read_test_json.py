import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data):


    #Initialize a new GameLibrary
    Game_library = test_data.GameLibrary()

    game = test_data.Game()


    for Game_Library in json_data["GameLibrary"]:


        game.title = Game_Library["title"]
        game.year = Game_Library["year"]
        game.platform = Game_Library["platform"]




        return Game_Library




    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
#Part 2
input_json_file = "data/test_data.json"

with open("data/test_data.json", "r") as reader:
    test_data = json.load(reader)

print("JSON data:")
print(test_data)

Game_library = make_game_library_from_json( test_data)

print()

print(Game_library)


### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
