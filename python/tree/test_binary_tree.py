from binary_tree import BinaryTree, _Node


def test_exists():
    assert BinaryTree


def test_rootless_tree():
    tree = BinaryTree()
    expected = []
    actual = tree.breadth_first()
    assert actual == expected


def test_single_node():
    tree = BinaryTree()
    tree._root = _Node('apples')
    expected = ['apples']
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected


def test_add_two_nodes():
    tree = BinaryTree()
    tree._root = _Node('apples')
    tree._root.left = _Node('bananas')
    assert tree._root.value == 'apples'
    assert tree._root.left.value == 'bananas'


def test_two_nodes():
    tree = BinaryTree()
    tree._root = _Node('apples')
    tree._root.left = _Node('bananas')
    expected = ['apples', 'bananas']
    actual = tree.breadth_first()
    assert actual == expected


def test_four_nodes():
    tree = BinaryTree()
    tree._root = _Node('apples')
    tree._root.left = _Node('bananas')
    tree._root.right = _Node('cucumbers')
    tree._root.left.right = _Node('dates')
    expected = ['apples', 'bananas', 'cucumbers', 'dates']
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected
