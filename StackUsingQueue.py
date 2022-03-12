'''
  Author: Shaik Faizan Roshan Ali
  Link: https://leetcode.com/problems/implement-stack-using-queues/
  Date: 12th March 2022
  Approach: Push operation is direct append. 
            While the pop and top operation basically loops through the queue and append the n-1 elements
            back to the queue. 
'''
class MyStack:

    def __init__(self):
        
        self.queue1 = []
        
    def push(self, x: int) -> None:
        
        self.queue1.append(x)
        
    def pop(self) -> int:
        
        size = len(self.queue1)
        for i in range(0, size-1):

            self.queue1.append(self.queue1.pop(0))
        
        return self.queue1.pop(0)
    
    def top(self) -> int:
        
        size = len(self.queue1)
        for i in range(0, size-1):

            self.queue1.append(self.queue1.pop(0))
        
        value = self.queue1.pop(0)
        self.queue1.append(value)
        return value
    
    def empty(self) -> bool:
        
        if len(self.queue1) == 0:
            
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
