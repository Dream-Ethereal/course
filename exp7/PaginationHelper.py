class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.len=len(collection)
        self.page=items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return self.len
    
    # returns the number of pages
    def page_count(self):
        if self.len%self.page ==0 :
            return self.len//self.page
        else:
            return self.len//self.page +1 

    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        if self.len%self.page ==0 :
            return self.page
        else:
            if page_index == self.page_count()-1:
                return self.len%self.page
            else:
                return self.page
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >=self.len:
            return -1
        return item_index//self.page
