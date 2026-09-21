class Node:
    def __init__(self, val):
        self.data= val
        self.next= None

class myqueue:
    def __init__(self):
        self.front= None
        self.rear= None
        self.size=0

    def enqueue(self, x):
        node= Node(x)
        if self.isEmpty():
            self.front= self.rear= node
        else:
            self.rear.next= node
            self.rear= node
        self.size+=1

    def dequeue(self):
        if self.isEmpty():
            print("Queue Overflow")
            return
        temp=self.front
        res= self.front.data
        self.front= self.front.next
        if self.front is None:
            self.rear = None
        self.size-=1
        return res
    
    def isEmpty(self):
        return self.front is None

    def getfront(self):
        if self.isEmpty():
            return -1
        return self.front.data

    def getrear(self):
        if self.isEmpty():
            return -1
        return self.rear.data

    def sizequeue(self):
        return self.size


if __name__ == "__main__":
    q = myqueue()
    
    q.enqueue(10)
    q.enqueue(20)
    
    print(q.dequeue())
    
    q.enqueue(30)
    
    print(q.getfront())
    print(q.getrear())
    print( q.sizequeue())
