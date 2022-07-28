import tkinter as tk
import math
#open a tkinter window
root1 = tk.Tk()
def close_screen():
    root1.destroy()
pass

def braindamage(): #main script that does the math portion
    #get the values from the textboxes
    rstr = rheightstr.get()
    gcstr = gravitatinalconstant.get()
    mstr = massvalue.get()
    #converr the values we got from the text boxes into a float, because they are most likley going to be in scientific notation
    rint = float(rstr)
    mint = float(mstr)
    gcint = float(gcstr)
    velocity = gcint*mint
    print(velocity) #print answer
    velocity = velocity/rint
    print(velocity)
    velocity = math.sqrt(velocity)
    #velocity = sqrt(velocity)
    print(velocity)
    #convert answer to string so we can input it to the text box that displays the answer
    velocitym = str(velocity)
    velocitykm = velocity/1000
    velocitykm = str(velocitykm)
    text2.config(text = velocitym + " meters a second(m/s) or " + velocitykm + " kilometers a second(km/s)")
    #update info so we can fit the textbox in the center
    text2.update()
    textx = text2.winfo_screenwidth()/2
    print(textx)
    text2.place(x = screenx/2 - 480/2, y = 500)
pass
#find middle of screen
screenx = root1.winfo_screenwidth()
#find middle height of screen
screeny = root1.winfo_screenheight()
text1 = tk.Label(root1,text = "first textbox is Gravitanial Constant, secound textbox is radius of object + height of orbit , last textbox is mass of object(MAKE SURE YOU ARE USING THE SAME UNITS!, all answers must be in scientific notaion, and convert km's to m's")
text1.config(width = 200, height = 20)
text1.place(x = screenx/2 -650, y = 200)
root1.title("Orbital Velocity Calculator")
root1.state("zoomed")
#root1.attributes('-fullscreen',True)
button1 = tk.Button(root1,text = "X", background= "red", command = close_screen)
button1.config(width = 5, height = 2)
massvalue = tk.StringVar()
masstextbot = tk.Entry(root1,textvariable = massvalue)
masstextbot.place(x = screenx/2 - 124/2, y = 100)#bottom
gravitatinalconstant = tk.StringVar()
GCtextbox = tk.Entry(root1,textvariable = gravitatinalconstant)
GCtextbox.place(x = screenx/2 - 124/2, y = 50)#first
GCtextbox.update()
rheightstr = tk.StringVar()
rheighttextbox = tk.Entry(root1,textvariable = rheightstr)
rheighttextbox.place(x = screenx/2 - 124/2, y = 75) #secound
rheighttextbox.update()
calculatebutton = tk.Button(root1,text = "solve!", command = braindamage)
calculatebutton.config(width = 20, height = 5)
calculatebutton.place(x = screenx/2 - 150/2, y = 200)
calculatebutton.update()
#print(GCtextbox.winfo_width())
#print(button1.winfo_width())
text2 = tk.Label(root1,text = "answer hasnt been computed yet...")
text2.place(x = screenx/2 - 190/2, y = 500)
print(text2.winfo_width())
#put this at bottom so your code actually works or else it wont open your tkinter window
root1.mainloop()

