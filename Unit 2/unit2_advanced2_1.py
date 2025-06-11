# 2 dictionaries - expected, actual
# looping: actual - expected
# return: dictionary - key (room name), value (actual - expected)

# Loop through 1 dictionary


def analyze_library(library_catalog, actual_distribution):
    result = {}

    for key in library_catalog:
        val = actual_distribution[key] - library_catalog[key]

        result[key] = val

    return result


library_catalog = {"Room A": 150, "Room B": 200, "Room C": 250, "Room D": 300}

actual_distribution = {"Room A": 150, "Room B": 190, "Room C": 260, "Room D": 300}


print(analyze_library(library_catalog, actual_distribution))
