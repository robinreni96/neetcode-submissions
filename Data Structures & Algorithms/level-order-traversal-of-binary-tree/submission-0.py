from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root:
            queue.append(root)
        
        result = []
        while len(queue) > 0:
            tmp_result = []
            for i in range(len(queue)):
                cur = queue.popleft()
                tmp_result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(tmp_result)
        return result
