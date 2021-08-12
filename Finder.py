from tkinter import *
root = Tk()
root.title("Finder Offline Browser (BETA)")
root.geometry("500x400")


def finding():
    searchInput = Search.get()
    if searchInput == "Hello":
        result = Label(root, text="Hi!")
        result.grid(row=1)



Title = Label(root, text="Finder Offline", font=("Roboto", 40)).pack(ipady=20)
SearchInfo = Label(root, text="Type here what you need to search in the box below.", font=("Arial", 14)).pack()
SearchBar = Entry(root, font=("Roboto", 14)).pack()
Search = Button(root, text="Search", command="finding").pack()


root.mainloop()
