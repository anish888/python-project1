

#queue is ann abstract data structure
#class for creating queue
class queue:
    #creating blank queue
    def __init__(self):
        self.items = []
    #functiqueue for checking queue is empty or not     
    def is_empty(self):
        return self.items == []
    # defining enqueue for inserting     
    def enqueue(self, item):
        self.items.insert(0, item)
    #defining dequque for poping element    
    def dequeue(self):
        return self.items.pop()
    #defining the size of the queue    
    def size(self):
        return len(self.items)
#initalizing queue as queue        
queue=queue()
print(queue.is_empty()) 
#use for loop to insert element in queue
for i in range(1,10):
    queue.enqueue(i)
print(queue.items) 
print(queue.dequeue())
print(queue.size())   
