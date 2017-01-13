"""This is the entry point of the program."""


def highest_number_cubed(limit):
    nums = []
    for i in range(limit):
        if i**3 < limit:
            nums.append(i)
    return nums[-1]
            
    pass
