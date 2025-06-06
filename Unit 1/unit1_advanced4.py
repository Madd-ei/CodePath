def minimum_boxes(meals, capacity):
    capacity.sort(reverse=True)

    packs = sum(meals)
    result = 0

    for i in capacity:
        packs -= i
        result += 1

        if packs <= 0:
            return result

    return result


meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))
