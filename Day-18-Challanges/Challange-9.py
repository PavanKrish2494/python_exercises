

def draw_tree(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2*i + 1))
    return ""

print(draw_tree(10))