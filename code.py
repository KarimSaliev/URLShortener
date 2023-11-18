import tkinter as tk
import pyshorteners

root = tk.Tk()
root.title("URL Shortener")
root.geometry("300x150")

# function
def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)

# labels

longurl_label = tk.Label(root, text="Enter Long URL")
longurl_entry = tk.Entry(root)
shorturl_label = tk.Label(root, text="Shortened URL")
shorturl_entry = tk.Entry(root)



# pack()
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()

# button
shorten_button = tk.Button(root, text="Shorten URL", command=shorten)
shorten_button.pack()


root.mainloop()