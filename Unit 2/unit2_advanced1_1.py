# dictionary with keys (location) and values (number treasures buried)
# dictionary is for multiple locations on single island
# edge case: dictionary is empty

# Iterate through all the entries in dictionary, and add up the values in each entry


def total_treasures(treasure_map):
    result = 0

    for value in treasure_map.values():
        result += value

    return result


treasure_map1 = {"Cove": 3, "Beach": 7, "Forest": 5}

treasure_map2 = {"Shipwreck": 10, "Cave": 20, "Lagoon": 15, "Island Peak": 5}

print(total_treasures(treasure_map1))
print(total_treasures(treasure_map2))
