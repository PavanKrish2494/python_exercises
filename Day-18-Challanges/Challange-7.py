

def equilibrium_index(num):
    for i in range(len(num)):
        left_sum = sum(num[:i])      # sum of elements before index i
        right_sum = sum(num[i+1:])   # sum of elements after index i

        if left_sum == right_sum:
            return i
    return False

result=[1,2,0,3]
print(equilibrium_index(result))