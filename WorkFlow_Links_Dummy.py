import tkinter as tk
from tkinter import ALL
import webbrowser
from os import path

#root.tite
root =tk.Tk()
root.title('WorkFlow-Links')

#rooticon
root.iconbitmap("icons/icon.ico")

root.geometry("500x450")
root.resizable(False,False)

#def _init_(self)
#links

#mytime
def mytime_click():
    webbrowser.open("https://github.com/Sanklajai")

#imageassist
def imageassist_click():
    webbrowser.open("https://github.com/Sanklajai")

#Workdocx
def Workdocx_click():
    webbrowser.open("https://github.com/Sanklajai")

#3Dwiki
def wiki_click():
    webbrowser.open("https://github.com/Sanklajai")   

#Findasin
def Findasin_click():
    webbrowser.open("https://github.com/Sanklajai")

#NPH/OT
def Nph_click():
    webbrowser.open("https://github.com/Sanklajai")

#ALLSEC
def Allsec_click():
    webbrowser.open("https://github.com/Sanklajai")

#photopath
def photopath_click():
    webbrowser.open("https://github.com/Sanklajai")

#Catoulog Dumper
def CatoulogDumper_click():
    webbrowser.open("https://github.com/Sanklajai")

#Material Library
def MaterialLibrary_click():
    webbrowser.open("https://github.com/Sanklajai")

#KNET
def Knet_click():
    webbrowser.open("https://github.com/Sanklajai")

#JDI
def Jdi_click():
    webbrowser.open("https://github.com/Sanklajai")

#PhoneTool
def PhoneTool_click():
    webbrowser.open("https://github.com/Sanklajai")

#DSP
def Dsp_click():
    webbrowser.open("https://github.com/Sanklajai")

#SIM
def Sim_click():
    webbrowser.open("https://github.com/Sanklajai")

#Serchbot
def Serchbot_click():
    webbrowser.open("https://github.com/Sanklajai")

#GLB
def Gld_click():
    webbrowser.open("https://github.com/Sanklajai")

#Broadcast
def Broadcast_click():
    webbrowser.open("https://github.com/Sanklajai")

#Timeoff
def Timeoff_click():
    webbrowser.open("https://github.com/Sanklajai")

#Trouble ticket
def Troubleticket_click():
    webbrowser.open("https://github.com/Sanklajai")

#woodshopuploadpage
def woodhopup_click():
    webbrowser.open("https://github.com/Sanklajai")


#frame
frame = tk.Frame(root, bg="#283140")
frame.place(relwidth=1, relheight=1)

#iamges
img_amazon = tk.PhotoImage(file="icons/amazon.png")
img_Workflow = tk.PhotoImage(file="icons/Workflow.png")
img_DisLogo = tk.PhotoImage(file="icons/DIS Logo.png")
#image for buttons
img_Findasin = tk.PhotoImage(file="icons/Find Asin.png")
img_Mytime = tk.PhotoImage(file="icons/Mytime.png")
img_Broadcast = tk.PhotoImage(file="icons/Broadcast.png")
img_Photopath = tk.PhotoImage(file="icons/Photopath.png")
img_DSP = tk.PhotoImage(file="icons/DSP.png")
img_3Dwiki = tk.PhotoImage(file="icons/3Dwiki.png")
img_Woodshop_up = tk.PhotoImage(file="icons/Woodshop_up.png")
img_Imageassist = tk.PhotoImage(file="icons/Imageassist.png")
img_CatalogDumper = tk.PhotoImage(file="icons/CatalogDumper.png")
img_Allsec = tk.PhotoImage(file="icons/Allsec.png")
img_TroubleTicket = tk.PhotoImage(file="icons/TroubleTicket.png")
img_Timeoff = tk.PhotoImage(file="icons/Timeoff.png")
img_Searchbot = tk.PhotoImage(file="icons/Searchbot.png")
img_Materiallibrary = tk.PhotoImage(file="icons/Materiallibrary.png")
img_OTNPHrequest = tk.PhotoImage(file="icons/OTNPHrequest.png")
img_SIM = tk.PhotoImage(file="icons/SIM.png")
img_Workdocs = tk.PhotoImage(file="icons/Workdocs.png")
img_Knet = tk.PhotoImage(file="icons/KNET.png")
img_Phonetool = tk.PhotoImage(file="icons/Phonetool.png")
img_Glb = tk.PhotoImage(file="icons/GLB.png")
img_JDI = tk.PhotoImage(file="icons/JDIportal.png")

#logo
amazon =tk.Label(frame,image=img_amazon, bg ="#283140",)
amazon.place(x=15,y=10)

Workflow = tk.Label(frame,image=img_Workflow, bg ="#283140",)
Workflow.place(x=11,y=58)

DisLogo = tk.Label(frame,image=img_DisLogo, bg ="#283140",)
DisLogo.place(x=403,y=11)

#buttons
#line 1
Mytime = tk.Button(frame, image = img_Mytime, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= mytime_click)
Mytime.place(x=15,y=100)

Imageassist = tk.Button(frame, image = img_Imageassist, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= imageassist_click)
Imageassist.place(x=15,y=150)

Workdocs = tk.Button(frame, image = img_Workdocs, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Workdocx_click)
Workdocs.place(x=15,y=200)

Wiki3D = tk.Button(frame, image = img_3Dwiki, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= wiki_click)
Wiki3D.place(x=15,y=250)

Findasin = tk.Button(frame, image = img_Findasin, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Findasin_click)
Findasin.place(x=15,y=300)

OTNPHrequest = tk.Button(frame, image = img_OTNPHrequest, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Nph_click)
OTNPHrequest.place(x=15,y=350)

Allsec = tk.Button(frame, image = img_Allsec, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Allsec_click)
Allsec.place(x=15,y=400)

#line 2

Photopath = tk.Button(frame, image = img_Photopath, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= photopath_click)
Photopath.place(x=178,y=100)

CatalogDumper = tk.Button(frame, image = img_CatalogDumper, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= CatoulogDumper_click)
CatalogDumper.place(x=178,y=150)

Materiallibrary = tk.Button(frame, image = img_Materiallibrary, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= MaterialLibrary_click)
Materiallibrary.place(x=178,y=200)

Woodshop_up = tk.Button(frame, image = img_Woodshop_up, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= woodhopup_click)
Woodshop_up.place(x=178,y=250)

Knet = tk.Button(frame, image = img_Knet, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Knet_click)
Knet.place(x=178,y=300)

Jdi = tk.Button(frame, image = img_JDI, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Jdi_click)
Jdi.place(x=178,y=350)

Phonetool = tk.Button(frame, image = img_Phonetool, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= PhoneTool_click)
Phonetool.place(x=178,y=400)


#line 3
Dsp = tk.Button(frame, image = img_DSP, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Dsp_click)
Dsp.place(x=341,y=100)

Sim = tk.Button(frame, image = img_SIM, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Sim_click)
Sim.place(x=341,y=150)

Searchbot = tk.Button(frame, image = img_Searchbot, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Serchbot_click)
Searchbot.place(x=341,y=200)

Glb = tk.Button(frame, image = img_Glb, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Gld_click)
Glb.place(x=341,y=250)

Broadcast = tk.Button(frame, image = img_Broadcast, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Broadcast_click)
Broadcast.place(x=341,y=300)

Timeoff = tk.Button(frame, image = img_Timeoff, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Timeoff_click)
Timeoff.place(x=341,y=350)

TroubleTicket = tk.Button(frame, image = img_TroubleTicket, bg ="#283140", activebackground ="#283140", borderwidth = 0, command= Troubleticket_click)
TroubleTicket.place(x=341,y=400)


root.mainloop()