import winsound
import tkinter as tk
import keyboard
while True:
    mode = input("What will you be using? \n 1. creating a soundboard \n 2. loading a soundboard \n")
    if mode == "1" or mode == "2":
        break
if mode == "1":
    folder = input("what is the folder where your sound files are stored \n")
    name = input("what would you like to name this soundboard? \n")
        
button_count = 0
buttons = []
button_list = []
if mode == "1":
    root = tk.Tk()
    root.geometry("600x600")
def create_button():
    global button_count,folder
    text = input("what should the button say \n")
    sound = input("what is the name of the sound file \n")
    button_count+=1
    button_list.append(text)
    button_list.append(sound)
    buttons.append(tk.Button(root, text=text,command= lambda: winsound.PlaySound((folder+"//"+sound), winsound.SND_ALIAS)))
    buttons[button_count-1].pack(pady=10)
    #print(button_list)
def save():
    global name
    name = name+".sndboard"
    with open(name,"w") as f:
        f.write(f"{folder}\n")
        index=0
        for i in range(len(buttons)):
            f.write(f"{button_list[index]}\n")
            index+=1
            f.write(f"{button_list[index]}\n")
            index+=1
def load_button(Text,Sound,Folder):
    buttons.append(tk.Button(root, text=Text.rstrip("\n"),command= lambda: winsound.PlaySound((Folder+"//"+Sound.rstrip("\n")), winsound.SND_ALIAS)))
    buttons[-1].pack()
if mode == "2":
    file = input("what is the name of the sndboard file you want to load \n")
    file = file + ".sndboard"
    lines = ""
    with open (file,"r") as f:
        lines = f.readlines()
        folder = lines[0]
        folder = folder.rstrip("\n")
        #print(lines)
        index=1
        root = tk.Tk()
        root.geometry("600x600")
        for i in range(len(lines)-1):
            try:
                load_button(lines[index],lines[index+1],folder)
                index+=2
            except IndexError:
                break

if mode == "1":
    saver = tk.Button(root, text="Save your soundboard",command= lambda: save())
    saver.pack()
    creator = tk.Button(root, text="create a new button",command= lambda: create_button())
    creator.pack(pady=10)
root.title("Soundboard Creator")
root.mainloop()