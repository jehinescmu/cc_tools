import cc_dat_utils
import cc_data
import json



# Part 3 ===================================================================================
# Creates and returns a a level (defined in jehines_ccl.json) from loaded json_data
def make_cc_level_from_json(level_json):
    # Initialize a new level
    new_level = cc_data.CCLevel()
    # Pull the corresponding field from the JSON File
    new_level.level_number = level_json["level_number"]
    new_level.num_chips = level_json["num_chips"]
    new_level.time = level_json["time"]
    new_level.upper_layer = level_json["upper_layer"]

    # Loop through each detail of the platform
    for field_json in level_json["optional_fields"]:
        #check the type and if that field exits within the json, make a new field with that data
        # If there is a title create a title field
        if field_json["type"] == "title":
            new_field = cc_data.CCMapTitleField(field_json["title"])
            new_level.add_field(new_field)
        # If there is a hint create a hint field
        elif field_json["type"] == "hint":
            new_field = cc_data.CCMapHintField(field_json["hint"])
            new_level.add_field(new_field)
        # If there is a password create a password field
        elif field_json["type"] == "password":
            new_field = cc_data.CCEncodedPasswordField(field_json["password"])
            new_level.add_field(new_field)
        elif field_json["type"] == "monsters":
            # The monsters parameter is a list of coordinates
            # Create an Empty list to hold coordinates
            monster_coordinates = []
            # For every item in the monster data list, build a new coordinate from the json file 0 = x 1 = y
            # Create a new field with these new coordinates
            for monster_json in field_json["monsters"]:
                monster_coordinates.append(cc_data.CCCoordinate(monster_json[0], monster_json[1]))
                new_field = cc_data.CCMonsterMovementField(monster_coordinates)
            new_level.add_field(new_field)

    # return the completed level
    return new_level


with open("data/jehines_ccl.json", "r") as reader:
    library_json = json.load(reader)

    # Open the file specified by input_json_file + use the json module to load the data from the file
    cc_level_data = cc_data.CCDataFile()

    # Loop through levels in the json file
    for level_json in library_json:
        cc_level_data.add_level(make_cc_level_from_json(level_json))

# Print the resulting Level
print(cc_level_data)
# Write the resulting levels to a .dat file
cc_dat_utils.write_cc_data_to_dat(cc_level_data, "data/jehines_ccl.dat")