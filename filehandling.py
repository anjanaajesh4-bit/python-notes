# f=open("sample.txt","w")
# f.write("learn python")
# f.close()

# f=open(r"C:\Users\ASUS\OneDrive\Desktop\python\data.txt","w")
# f.close()

# f=open("sample.txt","r")
# print(f.read())
# f.close()

# f=open("sample.txt","a")
# f.write("learn javascript\n")
# f.close()

# f=open("sample.txt","r")
# # print(f.readline())
# # print(f.readline())
# print(f.readlines())
# f.close()/

# f=open("sample2.txt","x")
# f.close()

# f=open("image.jpg","rb")
# # print(f.read())
# print(f.read(20))
# f.close()

# f=open("sample.txt","r+")
# print(f.read())
# f.write("goodbye\n")
# print(f.read())
# f.close()
# f=open("sample.txt","r+")
# print(f.read())
# f.close()
      
# f=open("sample.txt","w+")
# print(f.read())
# f.write("goodbye!\n")
# print(f.read())
# f.close()

# f=open("sample.txt","a+")
# print(f.read())
# f.write("goodbye!\n")
# print(f.read())
# f.close()

# f=open("sample4.txt","w")
# f.write("welcome to python")
# print(f.name)
# print(f.mode)
# print(f.closed)
# f.close()
# print(f.closed)

# f=open("sample2.txt","w")
# f.writelines(['hello world\n','learn python\n','learn java\n','learn javascript\n','learn c\n','goodbye!\n'])
# f.close()

with open("data.txt","w")as f:
    f.write("hello")