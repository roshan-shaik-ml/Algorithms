'''
    Author: Shaik Faizan Roshan Ali
    Link: https://leetcode.com/problems/implement-queue-using-stacks/
    Date: 12th March 2022
    Approach: I chose not to use python list inbuilt methods, but make the traditional implementation of Stack for fun.
              Use two stacks; stack-1 handles the push operation while stack-2 handles pop and peek
              if stack-2 is empty push existing stack-1 elements to stack-2 and then use stack-2 top for peek and pop
'''


class MyStack:
    
    def __init__(self):
        
        self.stack = [0 for _ in range(0, 100)] # max hundred calls
        self.top = -1
    
    def push(self, x):
        
        if self.top >= -1:
            
            self.top += 1
            self.stack[self.top] = x
            
    def pop(self):
        
        x = self.stack[self.top]
        self.top -= 1
        
        return x
    
    def peek(self):
        
        x = self.stack[self.top]
        return x
    
    
    def isEmpty(self):
        
        if self.top == -1:
            return True

        return False
    
class MyQueue:

    def __init__(self):
        
        self.stack1 = MyStack()
        self.stack2 = MyStack()


    def push(self, x: int) -> None:
        
        self.stack1.push(x);

    def pop(self) -> int:
        
        if self.stack2.isEmpty() == True:
            
            while(self.stack1.isEmpty() != True):
                
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        
        if self.stack2.isEmpty():
            
            while (self.stack1.isEmpty() != True):
                
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.peek()

    def empty(self) -> bool:
        
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
