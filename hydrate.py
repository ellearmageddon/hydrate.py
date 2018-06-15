import time
import webbrowser

count = 0

while(count < 3):

    break_count = 0

    while(break_count < 3):
        time.sleep(3600)
        webbrowser.open("https://youtu.be/TwSyrOnz8lY?t=9s")
        break_count = break_count + 1

    webbrowser.open("https://www.youtube.com/watch?v=hjB5gjTEEj8")
    count = count + 1

webbrowser.open("https://www.youtube.com/watch?v=Udj-o2m39NA")
