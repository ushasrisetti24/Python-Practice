class myQueue:
    def __init__(self, capacity):
        self.capacity= capacity
        self.arr=[0]*capacity
        self.size=0

    def Enqueue(self,x):
        if(self.size== self.capacity):
            print("Queue Overflow")
            return
        self.arr[self.size]=x
        self.size+=1

    def Dequeue(self):
        if(self.size==0):
            print("Stack Underflow")
            return
        for i in range(1,self.size):
            self.arr[i-1]=self.arr[i]
        self.size-=1

    def getfront(self):
        if self.size==0:
            print("Queue is empty")
            return -1
        return self.arr[0]

    def getRear(self):
        if self.size==0:
            print("Queue is empty")
            return -1
        return self.arr[self.size-1]



if __name__=="__main__":
    qu= myQueue(4)
    qu.Enqueue(30)
    qu.Enqueue(56)
    qu.Enqueue(21)
    qu.Enqueue(7)
    print(qu.arr)
    qu.Dequeue()
    print(f" Front element : {qu.getfront()}")
    print(f" Rear Element: {qu.getRear()}")
