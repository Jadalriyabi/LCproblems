# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Questions
#What is the range of values for each node? Are they all integers?
#Can the tree be empty? If so, what should the output be?
#Do you want the count of good nodes or the nodes themselves?
#What is the maximum number of nodes in the tree? This will help us consider time and space complexity.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #use dfs to count good nodes
        def dfs(node, max_so_far):
            #cehcking if node is empty
            if not node:
                return 0

            #check if the current node is good
            good = 1 if node.val >= max_so_far else 0

            #update max to vefiy the good value so far
            max_so_far = max(max_so_far, node.val)

            #count good for left and right subtrees
            good += dfs(node.left, max_so_far) 
            good += dfs(node.right, max_so_far)

            return good
        
        return dfs(root, root.val)

            
