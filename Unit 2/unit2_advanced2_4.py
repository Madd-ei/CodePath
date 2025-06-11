from collections import Counter


def num_of_time_portals(portals: list[str], destination: str):
    freq = Counter(portals)
    count = 0

    for prefix in portals:
        if destination.startswith(prefix):
            suffix = destination[len(prefix) :]
            count += freq[suffix]

            if prefix == suffix:
                count -= 1

    return count


portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
