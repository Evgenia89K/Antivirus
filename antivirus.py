import os
a=str(input("Enter the name of the program with its extension "))
while True:
    to="taskkill /f /IM "+str(a)
    os.system(to)