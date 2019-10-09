source = ["This", "is", "a", "list"]
so_far = []
for index in range(0, len(source)):
    so_far = [source[index]] + so_far
    print(so_far)
