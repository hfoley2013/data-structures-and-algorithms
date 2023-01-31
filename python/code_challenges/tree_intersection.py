from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    dic = dict(zip(tree1.pre_order(), tree2.pre_order()))
    common_key_value = {key: value for key, value in dic.items() if key == value}
    return common_key_value.keys()
