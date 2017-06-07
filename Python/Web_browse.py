import webbrowser
import time

i = 1
total_breaks = 5

print("This program starts at"+time.ctime())
while (i <= total_breaks):
    time.sleep(30)
    webbrowser.open("https://www.youtube.com/watch?v=SevHZgBnfF0")
    i = i+1
    print ("number of breaking time:")


