# работа с файлами

f = open("task4.txt", "r")
lines = f.readlines()
for line in lines:
    print(line[:-1])
f.close()   

f = open("task3.txt", "r")
print(f.readline()[:-1])
f.close()  

f = open("diskra_s.pdf", "rb")
str = f.read(3000)
print(str)
while (len(str) == 3000):
    str = f.read(3000)
    print(str)
f.close()

f = open("test.txt", "w")
f.write("Hello, world!")
f.close()


# хеширование
import hashlib

print(hashlib.algorithms_guaranteed)

str = "Pa$$w0rd"

hash_object_md5 = hashlib.md5(str.encode())
print(hash_object_md5.hexdigest())

hash_object_sha256 = hashlib.sha256(str.encode())
print(hash_object_sha256.hexdigest())

hash_object_blake2s = hashlib.blake2s(str.encode())
print(hash_object_blake2s.hexdigest())






