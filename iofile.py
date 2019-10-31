from sys import argv

file=open(argv[0])
text=file.read()
print(text)

fileforw = open(argv[0], "w")
fileforw.write(text)
fileforw.write("\n23")
fileforw.close()
