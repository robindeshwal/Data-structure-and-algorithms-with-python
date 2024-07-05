from stack.stack import Stack, TwoStackInArray


class Practice:

  def impement_two_stack(self):
    """
    Implement two stack in an array.
    """

    stack_size = 10
    sq = TwoStackInArray(stack_size)

    sq.push1(5)
    sq.push1(6)
    sq.push1(7)
    sq.push1(8)
    sq.push2(1)
    sq.push2(2)
    sq.push2(3)
    sq.push2(4)

    sq.printS()
    print(f"popped stack1: {sq.pop1()}")  # Should print 5
    print(f"popped stack2: {sq.pop2()}")  # Should print 10
    sq.printS()

  def reverse_str(self):
    """
    Reverse string using stack.
    """
    string = "robin"

    s = Stack()
    for i in range(len(string)):
      s.push(string[i])

    reversed = ""
    while not s.is_empty():
      reversed += s.pop()

    print(reversed)

  def middle_element(self):
    """
    find middle element in a stack.
    all element should not me deleted.
    
    Input  : Stack[] = [1, 2, 3, 4, 5]
    Output : Stack[] = [1, 2, 4, 5]
    """

    def solve(s, total_size):
      #  base
      middle = (total_size //
                2) if total_size % 2 == 0 else (total_size // 2) + 1  # middle
      if s.size() == middle:
        print(s.peek())
        return

      temp = s.pop()
      solve(s, total_size)

      s.push(temp)

    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)
    s.push(70)
    s.push(80)
    s.push(90)

    total_size = s.size()

    solve(s, total_size)

  def insert_at_bottom(self):
    """
    """

    def solve(s, x):
      if s.is_empty():
        s.push(x)
        return
      temp = s.pop()
      solve(s, x)
      s.push(temp)

      return s

    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)
    s.push(70)
    s.push(80)
    s.push(90)

    x = 99
    solve(s, x)

    # print(s.items)

  def reverse_stack(self):
    """
    """

    def insertAtBottom(s, x):
      if s.is_empty():
        s.push(x)
        return
      temp = s.pop()
      insertAtBottom(s, x)
      s.push(temp)

      return s

    def solve(s):
      # base
      if s.is_empty():
        return

      target = s.pop()

      solve(s)
      insertAtBottom(s, target)

    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)

    solve(s)
