# Non existent nodes in the tree are marked as -1.
tree = [0,0,0,0,0,-1,0,-1,-1,0,0]
sz = len(tree)
iterations = 0

def right(index):
    return index*2+2

def left(index):
    return index*2+1

def notExists(index):
    return index >= sz or tree[index]== -1

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.right = right
        self.left = left
        self.val = 0

#Uses tree represented by array
def minVertexCover(index):
    global iterations
    iterations += 1
    if(notExists(index) or notExists(right(index)) or notExists(left(index))):
        print("gonna return 0 on ", str(index))
        return 0
    print("Gonna work with " + str(index))
    if tree[index] == 0:
        #Root is part of MVC
        tempval = 1 + minVertexCover(left(index)) + minVertexCover(right(index))
        #Root is not part of MVC
        tempval2 = 0
        if(not notExists(left(index))):
            tempval2 = 1 + minVertexCover(left(left(index))) + minVertexCover(right(left(index)))
        if(not notExists(right(index))):
            tempval2 += 1 + minVertexCover(left(right(index))) + minVertexCover(right(right(index)))
        tree[index] = min(tempval, tempval2)
    else:
        print("DP effect!")
    return tree[index]

# Uses node structure that builds up for a tree
def minVertexCoverNodes(root):
    global iterations
    iterations += 1
    if(root == None or (root.right == None and root.left == None)):
        print("gonna return 0", end = " ")
        if(root):
             print("in", root.name, end = "")
        print("")
        return 0
    print("Gonna work with", root.name)
    if (not root.val):
        #Root is part of MVC
        tempval = 1 + minVertexCoverNodes(root.left) + minVertexCoverNodes(root.right)
        #Root is not part of MVC
        tempval2 = 0
        if(root.left):
            tempval2 = 1 + minVertexCoverNodes(root.left.left) + minVertexCoverNodes(root.left.right)
        if(root.right):
            tempval2 += 1 + + minVertexCoverNodes(root.right.left) + minVertexCoverNodes(root.right.right)
        root.val = min(tempval, tempval2)
    else:
        print("DP effect!")
    return root.val



print(minVertexCover(0))
print("Iterations were", iterations)
print("-----------")
iterations = 0
c1 = Node("c1", None, None)
c2 = Node("c2", None, None)
b1 = Node("b1", None, None)
b2 = Node("b2", c1, c2)
b3 = Node("b3", None, None)
a1 = Node("a1", b1, b2)
a2 = Node("a2", None, b3)
root = Node("root", a1, a2)
print(minVertexCoverNodes(root))
print("Iterations were", iterations)

