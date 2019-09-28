import sys
root = None
class Node:
    def __init__ (self, key):
        self.val = key
        self.left = self.right = None

def rec_inorder(root):
    if root:
        rec_inorder(root.left)
        print(root.val)
        rec_inorder(root.right)

def insertNode(data):
    global root
    parent = root
    current = parent
    if root == None:
        root=Node(data)
        return
    else:
        while(1):
            temp = current
            if data<temp.val:
                if temp.left is None:
                    temp.left = Node(data)
                    return
                else:
                    current=temp.left
            else:
                if temp.right is None:
                    temp.right = Node(data)
                    return
                else:
                    current= temp.right

def iter_inorder(root):
    current = root
    stack =[]
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val)
            current=current.right
        else:
            break





def main():
    insertNode(50)
    insertNode(10)
    insertNode(30)
    insertNode(1)
    insertNode(5)
    insertNode(2)
    rec_inorder(root)
    print("----------------------")
    iter_inorder(root)

if __name__ == "__main__":
    main()
    #sys.exit(main())
