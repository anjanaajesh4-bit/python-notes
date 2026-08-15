# f=open("new.txt","w+")
# print(f.tell())
# f.write("hello")
# print(f.tell())

# f=open("new.txt","r")
# print(f.read())
# print(f.tell())
# f.seek(4)
# print(f.tell())

try:
    f=open("file.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    f.close()