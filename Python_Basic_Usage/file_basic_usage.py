#file_handler=open("example.txt","x")
#The previos command only can run once.

file_handler=open("moon.txt","r")
#file_handler=open("~/桌面/Learning/LearnPython/langur.txt","r")

file_handler.close()
try:
    file_handler=open("moon.txt","w")
    try:
        file_handler.write("Hello World.\n")
        file_handler.write("This is a huge world,and I will explore it oneday.\n")
    finally:
        file_handler.close()#This 'finally' will run finally?
except IOError:
    print("Oops!")

def read_file():
    file_handler=open("moon.txt")
    print("Print each line in the text file")
    for each_line in file_handler:
        print(f"{each_line}")
    file_handler.close()

read_file()
