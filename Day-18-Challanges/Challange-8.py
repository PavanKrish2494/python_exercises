
def equilibrium_index(num):
    for i in range(len(num)):
        if sum(num[:i]) == sum(num[i+1:]):
            return i
    return False


nums = input("Enter numbers separated by commas: ")
num = list(map(int, nums.split(",")))

print(equilibrium_index(num))
