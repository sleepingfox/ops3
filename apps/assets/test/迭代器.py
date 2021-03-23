
# class MyList:
#
#     def __init__(self,nums:list):
#         self.data = nums
#
#     def __iter__(self):
#
#         return




class MyList:

    def __init__(self,num):
        self.data = num

    def __iter__(self):
        return MyListTterator(self.data)

class MyListTterator:
    def __init__(self,data):
        self.data = data
        self.now = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.now < self.data:
            self.now += 1
            return self.now - 1
        else:
            raise StopIteration


a = MyList(5)
for i in a:
    print(i)


