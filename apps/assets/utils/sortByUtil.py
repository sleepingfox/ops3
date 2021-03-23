class sortByUtil():
    def __init__(self,sortBy,order,queryset):
        self.queryset = queryset
        self.sortBy = sortBy
        self.order = order

    order_status = {
        "ascending": "",
        "descending": "-",
        "null": "",
    }


    def get_sort_order(self):
        if self.order=="null" or self.sortBy==None or self.order==None:

            return self.queryset

        print(self.order)
        print(self.sortBy)

        sort_order = self.order_status[self.order] + self.sortBy

        # print("=================")
        # print(sort_order)

        return self.queryset.order_by(sort_order)

