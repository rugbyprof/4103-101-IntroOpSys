def readHex(f):
    c1 = f.read(1)
    c2 = f.read(1)
    x = c1+c2
    return bytearray.fromhex(x).decode()

 
start=1117696 
size=35490
current = 0

f = open('Disk-512-0')
f.seek(start, 0)
# while current < start:
#     c = readHex(f)
#     current += 1

string = ""
while current < start + size:
    string += readHex(f)
    current += 1

print(string)
    