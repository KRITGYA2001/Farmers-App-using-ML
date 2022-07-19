#!/usr/bin/env python
# coding: utf-8

# # Crop Prediction

# In[1]:


def Crop_Prediction():
    def mainscreen():

        global window
        window = tk.Tk()
        window.geometry("1530x795+0+0")
        window.configure(bg="#FFE4B5")
        window.title("Prediction model")


        head = tk.Label(window, text="\nEnter Details\n", font=("rockwell extra bold",45),fg="dark blue",bg="#FFE4B5").pack()


        def back3() :
            window.destroy()
            
        def calling7():
            window.destroy()
            menu_win()

        def values():

            n=n_tk.get()
            p=p_tk.get()
            k=k_tk.get()
            temp=temp_tk.get()
            humidity=humidity_tk.get()
            ph=ph_tk.get()
            rainfall=rainfall_tk.get()

            def predictfunc(n,p,k,temp,humidity,ph,rainfall):
                #Predicting Model
                model=pickle.load(open('RandomForest.pkl','rb'))
                test_data=[[n,p,k,temp,humidity,ph,rainfall]]
                prediction=str(model.predict(test_data))
                prediction=prediction.lstrip("['")
                prediction=prediction.rstrip("']'")
                output1 = tk.Label(window, text="The prediction is: ",font=("Arial", 20),bg="#FFE4B5").place(x=600, y=570)
                output2 = tk.Label(window, text=prediction, font=("Arial", 20),bg="#FFE4B5").place(x=820, y=570)


            predictfunc(n,p,k,temp,humidity,ph,rainfall)



        n1 = tk.Label(window, text="Ratio of Nitrogen content in soil: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=180)

        n_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        n_tk.place(x=800, y=180)

        p2 = tk.Label(window, text="Ratio of Phosphorous content in soil: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=230)

        p_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        p_tk.place(x=800, y=230)

        k3 = tk.Label(window, text="Ratio of Potassium content in soil: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=280)

        k_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        k_tk.place(x=800, y=280)

        temp4= tk.Label(window, text="Temperature in degree Celsius: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=330)

        temp_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        temp_tk.place(x=800, y=330)

        humidity5= tk.Label(window, text="Relative humidity in %: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=380)

        humidity_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        humidity_tk.place(x=800, y=380)

        ph6= tk.Label(window, text="pH value of the soil: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=430)

        ph_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        ph_tk.place(x=800, y=430)

        rainfall7= tk.Label(window, text="Rainfall in mm: ",font=("Arial", 20),bg="#FFE4B5").place(x=320, y=480)

        rainfall_tk = tk.Entry(window, fg='blue', bg='white',borderwidth=5,font=("Arial", 18), width=30)
        rainfall_tk.place(x=800, y=480)


        back3_button = tk.Button(text="Exit", bg="blue", fg="white", height=1, width=10, borderwidth=8, cursor="hand2",font=("Arial", 12), command=back3)
        back3_button.place(x=330,y=700)

        submit_button = tk.Button(text="Submit", bg="green", fg="white", height=1, width=10, borderwidth=8, cursor="hand2",font=("Arial", 12), command=values)
        submit_button.place(x=730,y=700)
        
        submit_button = tk.Button(text="Main Menu", bg="black", fg="white", height=1, width=10, borderwidth=8, cursor="hand2",font=("Arial", 12), command=calling7)
        submit_button.place(x=1130,y=700)

        # start the GUI
        window.mainloop()

    mainscreen()


# # Fertilizer prediction

# In[17]:


def Fertilizer_Prediction():
    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom

    def back3() :
            top.destroy()
            
    def calling6():
        top.destroy()
        menu_win()


    # from tkinter import tkMessageBox
    top = Tk()
    # top.geometry("1230x795+0+0")
    top.configure(bg="#30BDC2")
    top.title("Fertilizer Prediction")
    # top.attributes("-fullscreen", True)
    app=FullScreenApp(top)

    def entry(*args):
        e1, e2, e3, e4, e5, e6, e7, e8 = args
        temp = e1.get()
        humidity = e2.get()
        moisture = e3.get()
        nitrogen = e4.get()
        phosphorous = e5.get()
        potassium = e6.get()
        soil = e7.cget("text")
        crop = e8.cget("text")
        model = pickle.load(open('classifier.pkl','rb'))
        crop_type_input = {"barley":0,"cotton":1,"ground Nuts":2,"maize":3,"millets":4,"oil seeds":5,"paddy":6,"pulses":7
        ,"sugarcane":8,"tobacco":9,"wheat":10}
        soil_type_input = {"black":1,"clayey":1,"loamy":2,"red":3,"sandy":4}
        ans=model.predict([[temp, humidity, moisture,soil_type_input[soil.lower()],crop_type_input[crop.lower()], nitrogen, potassium, phosphorous]])
        if ans[0] == 0:
            out="10-26-26"
        elif ans[0] ==1:
            out="14-35-14"
        elif ans[0] == 2:
            out="17-17-17"
        elif ans[0] == 3:
            out="20-20"
        elif ans[0] == 4:
            out="28-28"
        elif ans[0] == 5:
            out="DAP"
        else:
            out="Urea"
        fertilizers = {
    "urea" : "1. This fertilizer is primarily used for bloom growth as it can provide only nitrogen and not phosphorus or potassium.\n2.This must be used ahead of time as it takes a long time to come into effect.\n3.Too much use should be avoided.\n\n\n",
    "dap" : "1. This fertilizer is highly rich in both Nitrogen and Phosphorus, hence a great option among farmers.\n2. Highly soluble and dissolves quickly in the soil.\n3. High probability of water pollution. 4. High usage is known to cause water pollution issues.\n\n\n",
    "14-35-14" : "1. 14-35-14 is an ideal choice mainly for crops like rice, groundnut, soyabean and similar crops which require high phosphate amount. 2. This has the highest total nutrient content among all the NPK complex fertilisers.\n3. It is neutral in nature and does not cause any acidity/alkalinity to the soil.\n\n\n",
    "28-28" : "1. 28-28 fertilizer has both Nitrogen and Phosphorus in 28% amount.\n2. It provides instantaneous and prolonged greenness to the crops.\n3. Ammonium Phosphate is coated over Urea prill, due to which the losses from Urea will be minimised.\n\n\n",
    "17-17-17" : "1. It contains Nitrogen, Phosphorus and Potassium in equal proportions.\n2. Ideally suited for vegetable crops.\n3. Preferred grade in South India.\n\n\n",
    "20-20" : "1. The main advantage of this fertilizer is the 15% Sulphur content which supplements the Sulphur requirement of the crops.\n2. Granular in nature and can be easily applied by broadcasting, placement or drilling.\n3. It is highly suitable for Sulphur loving crops such as Oil seeds.\n\n\n",
    "10-26-26" : "1. It contains Phosphorous and Potassium in the ratio of 1:1, the highest among the NPK fertilisers. \n2. Used in basal application in crops like Wheat, Paddy, Maize, Pulses, Sugarcane, Vegetables etc.\n3. It is mostly preferred by farmers for sugarcane, potato and fruits.\n\n\n",
}
        output1 = Label(top, text="The prediction is: ",font=("Arial", 24),bg="#30BDC2").place(x=560, y=550)
        output2 = Label(top, text=out, font=("Arial", 24),bg="#30BDC2").place(x=835, y=550)
        output3 = Label(top, text=fertilizers[out], font=("Arial", 15),bg="#30BDC2").place(x=150, y=590)


    def trigger():
        entry(e1, e2, e3, e4, e5, e6, e7, e8)


    soils = [
        "Loamy",
        "Sandy",
        "Black",
        "Red",
        "Clayey"
    ]

    soildtype = StringVar()
    soildtype.set("Loamy")
    soildrop = OptionMenu(top, soildtype, *soils)
    soildrop["menu"].config(bg="black", fg="white", font=("Arial", 18))


    crops = [
        "Maize",
        "Sugarcane",
        "Cotton",
        "Tobacco",
        "Paddy"
    ]

    cropdtype = StringVar()
    cropdtype.set("Cotton")
    cropdrop = OptionMenu(top, cropdtype, *crops)
    cropdrop["menu"].config(bg="black", fg="white", font=("Arial", 18))    

    name1 = Label(top,text = "Enter the temperature: ", font=("Arial", 18))
    name1.place(relx= 0.12, rely = 0.05)
    name1.config(bg="#30BDC2")
    e1 = Entry(top, font=("Arial", 18), bg="#ADD8E6")
    e1.place(relx=0.52,  rely = 0.05) #temperature
    name2 = Label(top,text = "Enter the humidity: ", font=("Arial", 18))  
    name2.place(relx= 0.12, rely = 0.12)
    name2.config(bg="#30BDC2")
    e2 = Entry(top, font=("Arial", 18), bg="#ADD8E6")
    e2.place(relx= 0.52, rely = 0.12) #humidity
    name3 = Label(top,text = "Enter the moisture: ", font=("Arial", 18))
    name3.place(relx = 0.12, rely = 0.19)
    name3.config(bg="#30BDC2")
    e3 = Entry(top, font=("Arial", 18), bg="#ADD8E6")
    e3.place(relx = 0.52, rely = 0.19) #moisture
    name4 = Label(top,text = "Enter the Nitrogen Content in the soil: ", font=("Arial", 18))
    name4.place(relx = 0.12, rely = 0.26)
    name4.config(bg="#30BDC2")
    e4 = Entry(top, font=("Arial", 18), bg="#ADD8E6")
    e4.place(relx = 0.52, rely = 0.26) #nitrogen
    name5 = Label(top,text = "Enter the Phosphorous Content in the soil: ", font=("Arial", 18))
    name5.place(relx = 0.12, rely = 0.33)  
    name5.config(bg="#30BDC2")
    e5 = Entry(top, font=("Arial", 18), bg="#ADD8E6")
    e5.place(relx = 0.52, rely = 0.33) #phosphorous
    name6 = Label(top,text = "Enter the Potassium Content in the soil: ", font=("Arial", 18))
    name6.place(relx = 0.12, rely = 0.40)
    name6.config(bg="#30BDC2") 
    e6 = Entry(top, font=("Arial", 18), bg="#ADD8E6")
    e6.place(relx = 0.52, rely = 0.40) #potassium

    name7 = Label(top,text = "Select soil type: ", font=("Arial", 18))
    name7.place(relx=0.12, rely=0.47)
    name7.config(bg="#30BDC2") 
    e7 = soildrop
    e7.config(font=("Arial", 18), bg="#30BDC2", activebackground="red") # set the button font
    e7.place(relx=0.52, rely=0.47) #soil

    # helv20 = tkFont.Font(family='Helvetica', size=20)
    # menu = root.nametowidget(e7.menuname)  # Get menu widget.
    # menu.config(font=helv20)  # Set the dropdown menu's font

    name8 = Label(top,text = "Select the crop: ", font=("Arial", 18))
    name8.place(relx=0.12, rely=0.55)
    name8.config(bg="#30BDC2")
    e8 = cropdrop
    e8.config(font=("Arial", 18), bg="#30BDC2", activebackground="blue") # set the button font
    e8.place(relx=0.52, rely=0.55) #crop

    btn = Button(top, text="  Submit  ", command = trigger, font=("Arial", 20), bg="yellow", fg="red")
    btn.place(relx=0.4, rely=0.87)
    btn = Button(top, text="    Exit    ", command =back3 , font=("Arial", 20), bg="yellow", fg="red")
    btn.place(relx=0.2, rely=0.87)
    btn = Button(top, text="    Main Menu   ", command =calling6 , font=("Arial", 20), bg="yellow", fg="red")
    btn.place(relx=0.6, rely=0.87)


    top.mainloop()


# # Main Menu Window

# In[62]:


from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
import tkinter as tk
from tkinter.font import BOLD
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.constants import RIGHT, Y
from tkinter import filedialog
import matplotlib.pyplot as plt


def menu_win():
    def calling2():
        menuwin.destroy()
        Crop_Prediction()
        
    def calling3():
        menuwin.destroy()
        Fertilizer_Prediction()
        
    
    global menuwin
    menuwin=tk.Tk()
    menuwin.geometry('500x500')
    menuwin.configure(background='#71b340')
    tk.Label(menuwin,text=" Welcome to the Farmer's App Project",bg='#71b340',fg="white",font=("Amiri",22)).place(x=28,y=25)
    tk.Button(menuwin,text="       1.  Crop Prediction       ",bg='#c89b7b',fg='white',font=("Arial",14),command=calling2).place(x=120,y=170)
    tk.Button(menuwin,text="       2.  Fertilizer Prediction        ",bg='#c89b7b',font=("Arial",14),fg='white',command=calling3).place(x=104,y=235)
    tk.Button(menuwin,text="       3.  Exit        ",bg='#c89b7b',fg='white',font=("Arial",14),command=menuwin.destroy).place(x=168,y=295)
    tk.mainloop()

    
def main():
    def calling1():
        master.destroy()
        menu_win()
    global master
    master=tk.Tk()
    master.geometry('500x500')
    master.title("Main Window")
    master.configure(background='#3dd397')
    tk.Label(master,text="Farmer's App",bg='#3dd397',font=("Arial", 28)).place(x=140,y=100)
    tk.Label(master,text="_______________________________________"*100,bg='#3dd397',font=("Arial", 15)).place(x=0,y=430)
    tk.Label(master,text="Created by Kanika, Meghraj and Kritgya",bg='#3dd397',font=("Arial", 15)).place(x=60,y=460)
    tk.Button(master,text="  Menu  ",font=("Arial", 20),fg='white',bg='black',command=calling1).place(x=60,y=260)
    tk.Button(master,text="    Exit    ",font=("Arial", 20),fg='white',bg='black',command=master.destroy).place(x=300,y=260)
    tk.mainloop()

if __name__=="__main__":
    main()


# In[ ]:




