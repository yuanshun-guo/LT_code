'''
栈是先进后出的规则，把一个栈中的数据导入另一个栈中，数据的顺序发生改变，变成先进先出的顺序。

1.此题利用的是栈，而不是列表，但在python中这些都是以列表为底层进行实现的
  所以在这里：以列表实现栈，以栈实现队列；实现队列需要两个栈，所以也就在最初设置两个列表
'''


class MyQueue:

    def __init__(self):
        """
        in主要负责进push，out主要负责出pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        when new element come in，就在in里push
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        remove the element from in front of queue and return the element
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        # if self.stack_out:
        #     return self.stack_out.pop()
        # else:
        #     while self.stack_in:
        #         self.stack_out.append(self.stack_in.pop())
        #     return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not(self.stack_in or self.stack_out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
