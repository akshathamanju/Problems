
from binarytree import build


def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None:
        return (root1.value  == root2.value  and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))

    return False
arr1 = [100,50,200,25,125,350]
arr2 = [1,2,10,50,180,199]
root1 = build(arr1)
print(root1)
root2 = build(arr2)
print(root2)

if(are_identical(root1, root2)):
  print("The trees are identical")
else:
  print("The trees are not identical")