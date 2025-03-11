""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    #Write your code here
    answer = []
    def recursion(root):
        if root is None:
            return
        recursion(root.left)
        answer.append(root.data)
        recursion(root.right)

    recursion(root)

    sortedAnswer = sorted(answer)
    flag = all(x == y for x, y in zip(answer, set(sortedAnswer)))
    if len(sortedAnswer) != len(answer):
        flag = False
    return flag
