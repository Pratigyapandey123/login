from tkinter import *
from PIL import ImageTk

# functionality part


def hide():
    openEye.config(file='closeye2.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openEye.config(file='openeye1.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

# def button_click(event):


#gui part

login_window = Tk()

login_window.geometry('1030x515+50+50')
login_window.resizable(0,0)
# login_window.attributes('-alpha',0.5)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='finall.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 22, 'bold'), bg= 'cyan4',fg='black',width=14)
heading.place(x=20,y=70)



usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='cyan4')
usernameEntry.place(x=33, y=130)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
Frame(login_window, width=226, height=2, bg='cyan4').place(x=33, y=152)


passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='cyan4')
passwordEntry.place(x=33, y=170)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
Frame(login_window, width=226, height=2, bg='cyan4').place(x=33, y=192)


openEye = PhotoImage(file='openeye1.png')
eyeButton = Button(login_window, image=openEye, bd=0, bg='white', activebackground='white', cursor='hand2',command=hide)
eyeButton.place(x=238, y=170)

forgetButton = Button(login_window, text='Forgot Password?', font=('Microsoft Yahei UI Light', 9, 'bold'), bd=0, bg='white', fg='cyan4', activebackground='white', cursor='hand2', activeforeground='cyan4')
forgetButton.place(x=139, y=205)

loginButton = Button(login_window, text='Login', bd=0, fg='black', font=('Open Sans',16,'bold'), bg='cyan4', activeforeground='black', activebackground='cyan4', cursor='hand2', width=17)
loginButton.place(x=33, y=242)

orLabel = Label(login_window, text='--------------OR--------------', fg='cyan4', bg='white', bd=0, font=('Open Sans', 15))
orLabel.place(x=33, y=292)

fb_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=fb_logo, bg='white')
fbLabel.place(x=82, y=330)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=119, y=330)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=156, y=330)

signupLabel = Label(login_window, text="Don't have an account?", fg='darkred', bg='white', bd=0, font=('Open Sans', 9,'bold'))
signupLabel.place(x=33, y=385)

newaccountButton = Button(login_window, text='Create new one', bd=0, fg='cyan4', font=('Open Sans', 9, 'bold underline'), activeforeground='cyan4', activebackground='white', cursor='hand2')
newaccountButton.place(x=170, y=385)


login_window.mainloop()