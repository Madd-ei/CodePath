# rounds of votes
# all volunteers must be in the same group to declare victory
# votes start from left to right


def predictAdoption_victory(votes):
    voters = list(votes)

    i = 0
    while "C" in voters and "D" in voters:
        if i == len(voters):
            i = 0

        if voters[i] == "C" and "D" in voters:
            voters[voters.index("D")] = "X"

        elif voters[i] == "D" and "C" in voters:
            voters[voters.index("C")] = "X"

        i += 1

    if "D" in voters:
        return "Dog Lovers"
    elif "C" in voters:
        return "Cat Lovers"


print(predictAdoption_victory("CD"))
print(predictAdoption_victory("CDDC"))
