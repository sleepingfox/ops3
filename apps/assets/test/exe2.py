import datetime
def exe_time(func):

    print("start")
    start = datetime.datetime.now()
    # print(start)
    def inner(self,a,b):
        # print(stop)
        res = func(self, a, b)
        print("运行了多少时间%s" %(datetime.datetime.now()))
        return res
    print("stop")
    # time.sleep(1)


    return inner



class Test2:

    def __init__(self, nums):
        self.list = nums

    @exe_time
    def sumRange(self, i: int, j: int) -> int:
        res = 0
        for v in range(i,j+1):
            res = res + self.list[v]
        return res



class Test1:
    def __init__(self, nums):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

        print("_sums")
        print(_sums)

    @exe_time
    def sumRange(self, i, j):

        _sums = self.sums
        return _sums[j + 1] - _sums[i]

    # @exe_time
    # def test1(self,a,b):
    #     print(a)
    #     print(b)


l2 = [-2, 0, 3, -5, 2, -1]
numArray = Test1(l2)

# res = numArray.test1(3,4)
res1 = numArray.sumRange(0,5)
print(res1)
# print(res)
#


# #Test2
# test2 = Test2(l2)
#
# res1 = test2.sumRange(0,5)
# print(res1)


