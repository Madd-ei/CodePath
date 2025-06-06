def hulk_smash(num):
    result = []

    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("HulkSmash")
        elif i % 3 == 0:
            result.append("Hulk")
        elif i % 5 == 0:
            result.append("Smash")
        else:
            result.append(i)

    return result


n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))
