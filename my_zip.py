def my_zip(first,secoud):
    first_it=iter(first)
    secoud_it=iter(secoud)
    while True:
        try:
            yield (next(first_it),next(secoud_it))
        except StopIteration:
             return

a=['s','gff x','c']
b=range(15)
m= my_zip(a,b)

for pair in my_zip(a,b):
    print(pair)
    a,b
