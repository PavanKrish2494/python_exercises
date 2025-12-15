

def repeat(num):
    sample = []

    for n in num:
        if n not in sample:
            sample.append(n)
    return sample


numbers = [1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5]

print(repeat(numbers))
