def fillable(stock, merch, n):
    if merch not in stock or stock[merch] < n:
        return False
    else:
        return True