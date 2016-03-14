class Queue():
    """This class will define several functions which will work for queue"""

    def __init__(self):
        # Defining a list which will act as queue container
        self.myqueue = []

    def is_empty(self):
        # This method will check whether the queue is empty or not
        if len(self.myqueue) > 0:
            return False
        else:
            return True

    def enqueue(self, item):
        # This method will enqueue a item to the defined queue
        return self.myqueue.insert(0, item)
        # innsert(0, item) will insert "item" to the 0th position of the
        # defined list

    def dequeue(self):
        # This method will dequeue an item from defined queue
        return self.myqueue.pop()

def bfs(graph, start, end):
    # q is an object of Queue class
    q = Queue()
    temp_path = [start]
    q.enqueue(temp_path)
    while q.is_empty() is False:
        temp_path = q.dequeue()
        print(temp_path)
        last_node = temp_path[len(temp_path) - 1]
        if last_node == end:
            print("Path: ", temp_path)
            return
        try:
            for child_node in graph[last_node]:
                if child_node not in temp_path:
                    new_path = []
                    new_path = temp_path + [child_node]
                    q.enqueue(new_path)
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

    # Calling bfs function here
    bfs(graph, 'A', 'O')

if __name__ == '__main__':
    main()
