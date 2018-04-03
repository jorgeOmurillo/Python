def binary_tree(r):
    return [r, [], []]

def insert_left(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root

def insert_right(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root

def get_root(root):
    return root[0]

def set_root(root, newVal):
    root[0] = newVal

def get_left(root):
    return root[1]

def get_right(root):
    return root[2]

# r = binary_tree(1)
# insert_left(r, 12)
# insert_left(r, 122)
# print(r)
# insert_right(r, 14)
# insert_right(r, 123)

# l = get_left(r)
# print(l)

# set_root(l, 9)
# print(r)

# insert_left(l, 11)
# print(r)

# print(get_right(get_right(r)))
