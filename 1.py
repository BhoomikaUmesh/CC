def gen(prime,base,private_key):
    return pow(base,private_key,prime)
prime=int(input("enter prime no:"))
base=int(input("enter base"))
apr=int(input("enter alice private"))
apu=gen(prime,base,apr)
print(apu)
bpr=int(input("enter bob private"))
bpu=gen(prime,base,bpr)
print(bpu)
ash=gen(prime,bpu,apr)
bsh=gen(prime,apu,bpr)
print(ash)
print(bsh)
if ash==bsh:
    print("same")
else:
    print("error")
