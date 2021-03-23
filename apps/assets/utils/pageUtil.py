class pageUtil():
    def __init__(self,data,pageSize=10,currentPage=1,):
        self.data = data
        self.pageSize = pageSize
        self.currentPage = currentPage

        # self.limit = limit


    def pageData(self):

        if self.currentPage==None or self.pageSize==None:

            return self.data

        start = ((int(self.currentPage) - 1) * int(self.pageSize))

        stop = ((int(self.currentPage) - 1) * int(self.pageSize) + int(self.pageSize))

        fin_data = self.data[start:stop]

        return fin_data

