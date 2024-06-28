

stock_price={}
with open("stock.csv","r") as f:
    for line in f:
        data= line.split(",")
        day=data[0]
        price=int(data[1])
        stock_price[day]=price
print(stock_price )       