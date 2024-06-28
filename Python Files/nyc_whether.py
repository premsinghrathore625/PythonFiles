arr={}
with open("nyc_weather.csv","r")as f:
    for line in f:
        data=line.split(',')
        date=data[0]
        temp=int(data[1])
        arr[date]=temp

print(arr)        