import collections



"""
       
        
        Approach:
        - Perform a level-order traversal (BFS) on the binary tree using a queue.
        - At each level, keep track of the last node encountered (the rightmost node in that level).
        - Append the value of this rightmost node to the result list for each level.
        
        Time Complexity (TC): O(N), where N is the number of nodes in the binary tree, 
        as each node is processed once during the BFS traversal.
        
        Space Complexity (SC): O(N), where N is the number of nodes in the binary tree,
        accounting for the queue and the output list. The queue may hold up to O(N) nodes
        in the worst case (for a completely balanced tree).
        """

class Solution(object):
    def rightSideView(self, root):
        
        res = []

        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            rightMost = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightMost = node  # Track the last node in the current level
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)

        return res
