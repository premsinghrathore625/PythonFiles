def squares():
    a=1
    while True:
        yield a * a
        a+=1
 
for f in squares():
    if f>100:
        break
    else:
        print(f)        