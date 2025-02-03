# example of default argument
def net_price(list,discount=0,tax=0.13):
    return list*(1-discount)*(1+tax)


print(net_price(500))