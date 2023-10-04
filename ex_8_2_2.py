from operator import itemgetter

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
products = sorted(products, key=itemgetter(1))
print(products[::-1])
