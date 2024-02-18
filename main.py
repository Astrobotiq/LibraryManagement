import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import Library as lib




def AddBook():
    ExitMain()
    BNameVar = tk.StringVar()
    ANameVar = tk.StringVar()
    yearVar = tk.StringVar()
    pageVar = tk.StringVar()
    BNameLabel = tk.Label(window,text="Book Name",font=bigFont,bg="#A3764F")
    ANameLabel = tk.Label(window, text="Author Name",font=bigFont,bg="#A3764F")
    yearLabel = tk.Label(window,text="Release Year",font=bigFont,bg="#A3764F")
    pagesLabel = tk.Label(window, text="Pages",font=bigFont,bg="#A3764F")
    BName = tk.Entry(window,width=35,textvariable=BNameVar)
    author = tk.Entry(window,width=35,textvariable=ANameVar)
    year = tk.Entry(window,width=35,textvariable=yearVar)
    page = tk.Entry(window,width=35,textvariable=pageVar)

    BNameLabel.place(x=85,y=125)
    ANameLabel.place(x=85,y=190)
    yearLabel.place(x=85,y=255)
    pagesLabel.place(x=85,y=320)
    saveBtn = tk.Button(window,text="Save",width=20,command=lambda :save(),font=bigFont,border=10,bg="#A14739")
    MainMenu = tk.Button(window, text="Back to Main", width=20, command=lambda: EnterMainFromAddBook(),font=bigFont,border=10,bg="#66583D")
    BName.place(x=85,y=150)
    author.place(x=85,y=215)
    year.place(x=85,y=280)
    page.place(x=85,y=345)
    saveBtn.place(x=85,y=385)
    MainMenu.place(x=85,y=435)

    def save():
        lib.__init__()
        lib.add_book(BNameVar.get(),ANameVar.get(),pageVar.get(),yearVar.get())
        lib.__del__()


    def EnterMainFromAddBook():
        BNameLabel.place_forget()
        ANameLabel.place_forget()
        yearLabel.place_forget()
        pagesLabel.place_forget()
        BName.place_forget()
        author.place_forget()
        year.place_forget()
        page.place_forget()
        saveBtn.place_forget()
        MainMenu.place_forget()
        EnterMain()

def ListBook():
    ExitMain()
    listFrame = tk.Frame(window,width=400)
    scrollbar = tk.Scrollbar(listFrame)
    list = ttk.Treeview(listFrame,height=20 ,yscrollcommand=scrollbar.set)
    MainMenu = tk.Button(window, text="Back to Main", width=20,height=1 ,command=lambda: EnterMainFromListBook(),border=10,bg="#66583D",font=bigFont)
    list['columns'] = ("Book Name", "Author Name", "Release Year", "Pages")

    list.column("#0", width=0, stretch=False)
    list.column("Book Name", anchor="w", width=130)
    list.column("Author Name", anchor="w", width=130)
    list.column("Release Year", anchor="w", width=75)
    list.column("Pages", anchor="w", width=45)

    list.heading("#0", text="", anchor="w")
    list.heading("Book Name", text="Book Name", anchor="w")
    list.heading("Author Name", text="Author Name", anchor="w")
    list.heading("Release Year", text="Release Year", anchor="w")
    list.heading("Pages", text="Pages", anchor="w")

    list.tag_configure('oddrow',background="#a14739")
    list.tag_configure('evenrow',background="#676769")

    lib.__init__()
    count = 0
    for num in lib.list_books():
        if (count % 2) == 0:
            list.insert("","end",values=(num[0],num[1],num[2],num[3]),tags=('oddrow',))
        else:
            list.insert("", "end", values=(num[0], num[1], num[2], num[3]), tags=('evenrow',))
        count +=1

    lib.__del__()
    listFrame.place(x=0,y=50)
    scrollbar.pack(side="right",fill="y")
    scrollbar.config(command=list.yview)
    list.pack()
    MainMenu.place(x=110,y=650)

    def EnterMainFromListBook():
        listFrame.place_forget()
        scrollbar.pack_forget()
        list.pack_forget()
        MainMenu.place_forget()
        EnterMain()

def RemoveBook():
    ExitMain()
    delNameVar = tk.StringVar()

    messagge = tk.Label(window,text="Please enter book name to be deleted",font=bigFont,bg="#A3764F")
    nameLabel = tk.Label(window,text="Book Name:",font=bigFont,bg="#A3764F")
    name = tk.Entry(window,width=35,textvariable=delNameVar,font=bigFont)
    MainMenu = tk.Button(window, text="Back to Main", width=20, command=lambda: EnterMainFromRemoveBook(),font=bigFont,border=10,bg="#66583D")
    DeleteBTN = tk.Button(window,text="Delete",width=20,command=lambda :remove(),font=bigFont,border=10,bg="#A14739")
    messagge.place(x=65,y=150)
    nameLabel.place(x=65,y=190)
    name.place(x=65,y=220)
    MainMenu.place(x=65,y=310)
    DeleteBTN.place(x=65,y=260)

    def remove():
        lib.__init__()
        lib.remove_book(delNameVar.get())
        lib.__del__()
    def EnterMainFromRemoveBook():
        messagge.place_forget()
        nameLabel.place_forget()
        name.place_forget()
        MainMenu.place_forget()
        DeleteBTN.place_forget()
        EnterMain()

def ExitMain():
    listB.place_forget()
    Add.place_forget()
    Remove.place_forget()



def EnterMain():
    bgLabel.place(x=-10,y=0)
    listB.place(x=55,y=125)
    Add.place(x=55,y=250)
    Remove.place(x=55,y=375)


#Main burada başlasın
#Burası GUI'ın başı
lib = lib.Library()
window = tk.Tk()
window.geometry('400x720')
window.resizable(width=False,height=False)

bigFont = Font(family="Helvetica",size=11,weight="bold",slant="roman")
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background="#676769",rowheight=25,fieldbackground="#676769")
style.map("Treeview",background=[('selected','green')])

#Widgets can be added to here
#Main Menu
bg = tk.PhotoImage(file="library.png")
bgLabel = tk.Label(window,image=bg)
listB = tk.Button(window,text="List Books",width=30,command= lambda :ListBook(),border=10,bg="#a14739",font=bigFont)
Add = tk.Button(window, text="Add Books", width=30,command= lambda :AddBook(),border=10,bg="#676769",font=bigFont)
Remove = tk.Button(window,text="Remove Books",width=30,command= lambda :RemoveBook(),border=10,bg="#a3764f",font=bigFont)

EnterMain()

#Burası GUI'ın sonu sonu
window.mainloop()