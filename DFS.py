class Stack():
    """This class will define several methods which will work for stack"""

    def __init__(self):
        #Defining a list which will act as stack container
        self.mystack = []

    def is_empty(self):
        #This method will check whether the stack is empty or not
        if len(self.mystack) > 0:
            return False
        else:
            return True

    def push(self, item):
        #This method will push an item to the defined stack
        return self.mystack.append(item)

    def pop(self):
        #This method will pop an item from defined stack
        return self.mystack.pop()

    def peek(self):
        #This method will peek an item from the stack means won't remove it
        return self.mystack[len(self.mystack)-1]

def dfs(graph, start, end):
    # s is an object of Stack class
    s = Stack()
    temp_path = []
    s.push(start)
    while s.is_empty() is False:
        last_node = s.pop()
        if last_node not in temp_path:
            temp_path.append(last_node)
        print(temp_path)
        last_node = temp_path[len(temp_path) - 1]
        if last_node == end:
            print("Path: ", temp_path)
        try:
            for child_node in reversed(graph[last_node]):
                if child_node not in temp_path:
                    s.push(child_node)
        except:
            pass

def main():
    # Initializing the graph
    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'D', 'E'],
        'C' : ['A', 'F', 'G'],
        'D' : ['B', 'H', 'I'],
        'E' : ['B', 'J', 'K'],
        'F' : ['C', 'L', 'M'],
        'G' : ['C', 'N', 'O']
    }

    # Calling dfs function here
    dfs(graph, 'A', 'O')

if __name__ == '__main__':
    main()
