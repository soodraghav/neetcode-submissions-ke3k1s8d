

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # 1 2 n n 3 4 n n 5 n n

        ser = []

        def help(node):

            if not node: 
                ser.append("None")
                return None

            ser.append(str(node.val))

            help(node.left)
            help(node.right)


        help(root)

        return "#".join(ser)





        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        #       1

        #     2
        #   n   n


        deser = data.split("#")
        i= 0
        

        def help():

            nonlocal i

            if i>=len(deser) or deser[i] == "None": 
                i+=1
                return None

            node = TreeNode(deser[i])
            i+=1
            node.left = help()
            node.right = help()


            return node


        return help()


          



    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))