class myQueue:
    def __init__(self, capacity):
        self.capacity= capacity
        self.arr=[0]*capacity
        self.size=0
        self.front=0

    def Enqueue(self,x):
        if(self.size== self.capacity):
            print("Queue Overflow")
            return
        rear= (self.front + self.size)% self.capacity
        self.arr[rear]=x
        self.size+=1

    def Dequeue(self):
        if(self.size==0):
            print("Stack Underflow")
            return -1
        res=self.arr[self.front]
        self.front= (self.front+1)%self.capacity
        self.size-=1
        return res

    def getfront(self):
        if self.size==0:
            print("Queue is empty")
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.size==0:
            print("Queue is empty")
            return -1
        rear= (self.front + self.size -1 )%self.capacity
        return self.arr[rear]



if __name__=="__main__":
    qu= myQueue(4)
    qu.Enqueue(30)
    qu.Enqueue(56)
    qu.Enqueue(21)
    qu.Enqueue(7)
    print(qu.arr)
    qu.Dequeue()
    print(qu.getfront(), qu.getRear())
    qu.Dequeue()
    print(qu.getfront(), qu.getRear())
    qu.Enqueue(40)
    print(qu.getfront(), qu.getRear())