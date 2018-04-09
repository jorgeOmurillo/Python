class BinaryTree:

r = BinaryTree('a')
print(r.get_root())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root())
r.get_right_child().set_root('hello')
print(r.get_right_child().get_root())
