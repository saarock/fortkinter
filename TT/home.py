import tkinter as tk

from PIL import ImageTk, Image
import webbrowser
from tkinter import ttk
from tkinter import Text
from tkinter import font
# from ttk
# import tkhtmlview as tkhv

# Using the tkinter bootstrap
root = tk.Tk()
# Create a style object
style = ttk.Style()
root.geometry("800x600")  # Set the desired window size
root.configure(bg='thistle1')

# Set the overall theme
style.theme_use("clam")  
def navs():
     mainframe = tk.Frame(root,bg='orange2', width=503)
     mainframe.pack(side='left',fill='y')
     label = tk.Label(mainframe, text='Bike Breeze',font='35',width=10, height=3, bg='orange2', fg='white', background='brown3')
     label.pack()
     amainframe = tk.Frame(root,bg='snow', width=503, height=63)
     amainframe.pack(fill='x')

     for_profile = Image.open('a.jpg')
     profile_height = 108
     profile_width = 108
     resize_profile = for_profile.resize((profile_width, profile_height), Image.LANCZOS)
     profileImage = ImageTk.PhotoImage(resize_profile)
     profile_label = tk.Label(mainframe,text='profile', image=profileImage, cursor='hand2', bg='orange', fg='red')
     profile_label.image = profileImage
     profile_label.place(x=53,y=84)
     

     f = font.Font(size=14)

     first_name = tk.Label(mainframe, text='Aayush\nBasnet', font=35,bg='orange', fg='black')
     first_name.place(x=50, y=210)



# Fot services
     services = tk.Label(mainframe, text='Services', bg='orange', fg='white',font=f, width=23,highlightthickness=0,cursor='hand2')
     services.place(x=0, y=334)
     for_services= Image.open('services.png')
     servh = 18
     servw = 18
     resize_service= for_services.resize((servw, servh), Image.LANCZOS)
     services_img = ImageTk.PhotoImage(resize_service)
     services_image = tk.Label(mainframe, image=services_img)
     services_image.image = services_img
     services_image.place(x=49,y=338)
     change_button =tk.Label(mainframe ,text='Change Profie', fg='white', font=('Poppins', 15), bg='orange',highlightbackground='white',highlightthickness=2, border=13,cursor='hand2')
     change_button.place(x=37, y=267)





# For uploads bikes



navs()




def profies():
     look_uploadsmain = tk.Frame(root,height=645, width=1234, bg='lightBlue1')
     look_uploadsmain.place(x=254, y=109)
     look_profile = tk.Frame(look_uploadsmain, height=204,width=554,bg='snow')
     look_profile.place(x=23,y=23)
     label = tk.Label(look_profile, text='My name is')
     label.place(x=1)

     look_money = tk.Frame(look_uploadsmain, height=204,width=554,bg='snow')
     look_money.place(x=603,y=23)
    #  Custum font
     c  = font.Font(size=39)
     label = tk.Label(look_money, text='372K', bg='snow', font=c)
     label.place(x=20, y=20)


     show_all =tk.Frame(look_uploadsmain, width=1128 ,height=64, bg='snow',)
     show_all.place(x=23,y=250)
     show_all1 = tk.Frame(show_all,height=64,width=232, cursor='hand2', bg='orange')
     show_all1.place(x=0)
     show_all1buttom = tk.Frame(show_all1,width=232, height=5,  background='orange',cursor='hand2')
     show_all1buttom.place(x=0, y=60)
     l = tk.Label(show_all, text='ads')
     l.place(x=23)



     show_all2 = tk.Frame(show_all,height=64,width=502, cursor='hand2')
     show_all2.place(x=320)
     show_all1buttom2 = tk.Frame(show_all2,width=502, height=5,  background='red',cursor='hand2')
     show_all1buttom2.place(x=0, y=60)
     l = tk.Label(show_all, text='K XA')
     l.place(x=23)

     show_all3 = tk.Frame(show_all,height=64,width=502, cursor='hand2')
     show_all3.place(x=900)
     show_all1buttom2 = tk.Frame(show_all3,width=502, height=5,  background='blue',cursor='hand2', )
     show_all1buttom2.place(x=0, y=60)
     l = tk.Label(show_all, text='K asdfgA', bg='orange')
     l.place(x=23)





profies()
root.mainloop()
