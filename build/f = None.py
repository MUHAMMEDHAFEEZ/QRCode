file=open("C:\\Users\\prof\\Pictures\\dat.txt","w+")

file.write("Hello")

file.write("Python")

file.seek(5)

print(file.read())

file.close()