from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)           # use board (logical) pin layout
GPIO.setwarnings(False)            # disable warnings

pins = [3, 5, 7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37, 38, 40]
for i in pins:                     # set all (used) pins to output
        GPIO.setup(i, GPIO.OUT)

PAmp = [3, 5, 7, 11, 13, 15]            # Parallel interface for amplifier
PPs = [19, 21, 23, 29, 31, 33, 35, 37]  # Parallel interface for phaseshifter




win=Tk()                           # create window
win.title("Beam-steering")
myfont=tkinter.font.Font(family = 'Helvetica', size = 20, weight = 'bold')
win.geometry('1550x750')           # just wide enough to fit 2 circles

photo1=PhotoImage(file="/home/pi/codes/new pic/photo1.png")
photo1=photo1.subsample(2)
photo2=PhotoImage(file="/home/pi/codes/new pic/photo2.png")
photo2=photo2.subsample(2)
photo3=PhotoImage(file="/home/pi/codes/new pic/photo3.png")
photo3=photo3.subsample(2)
photo4=PhotoImage(file="/home/pi/codes/new pic/photo4.png")
photo4=photo4.subsample(2)
photo5=PhotoImage(file="/home/pi/codes/new pic/photo5.png")
photo5=photo5.subsample(2)
photo6=PhotoImage(file="/home/pi/codes/new pic/photo6.png")
photo6=photo6.subsample(2)
photo7=PhotoImage(file="/home/pi/codes/new pic/photo7.png")
photo7=photo7.subsample(2)
photo8=PhotoImage(file="/home/pi/codes/new pic/photo8.png")
photo8=photo8.subsample(2)
photo9=PhotoImage(file="/home/pi/codes/new pic/photo9.png")
photo9=photo9.subsample(2)
photo10=PhotoImage(file="/home/pi/codes/new pic/photo10.png")
photo10=photo10.subsample(2)
photo11=PhotoImage(file="/home/pi/codes/new pic/photo11.png")
photo11=photo11.subsample(2)
photo12=PhotoImage(file="/home/pi/codes/new pic/photo12.png")
photo12=photo12.subsample(2)
photo13=PhotoImage(file="/home/pi/codes/new pic/photo13.png")
photo13=photo13.subsample(2)
photo14=PhotoImage(file="/home/pi/codes/new pic/photo14.png")
photo14=photo14.subsample(2)
photo15=PhotoImage(file="/home/pi/codes/new pic/photo15.png")
photo15=photo15.subsample(2)
photo16=PhotoImage(file="/home/pi/codes/new pic/photo16.png")
photo16=photo16.subsample(2)

OpenSw=PhotoImage(file="/home/pi/codes/new pic/open2.png")
ClosedSw=PhotoImage(file="/home/pi/codes/new pic/closed2.png")


# Choose ELEVATION angle using Amplifier
def beam1():                         
        onbn = bin(63)
        print(onbn)
        on = PAmp[onbn]       # pins to be turned on
        print(on)                         # no pins to be turned off
        GPIO.output(on,1)                 # turn specified pins on

def beam2():
        onbn = bin(62)
        print(onbn)
        for i in PAmp:
                on[i] = onbn[i+2]
        off = PAmp[0]
        GPIO.output(on,1)
        GPIO.output(off,0)
   
def beam3():
        on = PAmp[1, 2, 3, 4, 5]
        off = PAmp[0]
        GPIO.output(on,1)
        GPIO.output(off,0)

def beam4():
        off = [3, 5, 7, 23, 29, 31, 33, 35, 37, 38, 40]
        on = [11, 13, 15, 19, 21]
        GPIO.output(on,1)
        GPIO.output(off,0)          

def beam5():
        off = [3, 5, 7, 11, 29, 31, 33, 35, 37, 38, 40]
        on = [13, 15, 19, 21, 23]
        GPIO.output(on,1)
        GPIO.output(off,0)  
       
def beam6():
        off = [3, 5, 7, 11, 13, 31, 33, 35, 37, 38, 40]
        on = [15, 19, 21, 23, 29]
        GPIO.output(on,1)
        GPIO.output(off,0)   

def beam7():
        off = [3, 5, 7, 11, 13, 15, 33, 35, 37, 38, 40]
        on = [19, 21, 23, 29, 31]
        GPIO.output(on,1)
        GPIO.output(off,0)

def beam8():
        off = [3, 5, 7, 11, 13, 15, 19, 35, 37, 38, 40]
        on = [21, 23, 29, 31, 33]
        GPIO.output(on,1)
        GPIO.output(off,0)
        
def beam9():
        off = [3, 5, 7, 11, 13, 15, 19, 21, 37, 38, 40]
        on = [23, 29, 31, 33, 35]
        GPIO.output(on,1)
        GPIO.output(off,0) 
        
def beam10():
        off = [3, 5, 7, 11, 13, 15, 19, 21, 23, 38, 40]
        on = [29, 31, 33, 35, 37]
        GPIO.output(on,1)
        GPIO.output(off,0) 
                
def beam11():
        off = [3, 5, 7, 11, 13, 15, 19, 21, 23, 29, 40]
        on = [31, 33, 35, 37, 38]
        GPIO.output(on,1)
        GPIO.output(off,0) 
        
def beam12():
        off = [3, 5, 7, 11, 13, 15, 19, 21, 23, 29, 31]
        on = [33, 35, 37, 38, 40]
        GPIO.output(on,1)
        GPIO.output(off,0)  

def beam13():
        off = [5, 7, 11, 13, 15, 19, 21, 23, 29, 31, 33]
        on = [3, 35, 37, 38, 40]
        GPIO.output(on,1)
        GPIO.output(off,0)

def beam14():
        off = [7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35]
        on = [3, 5, 37, 38, 40]
        GPIO.output(on,1)
        GPIO.output(off,0) 

def beam15():
        off = [11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37]
        on = [3, 5, 7, 38, 40]
        GPIO.output(on,1)
        GPIO.output(off,0) 

def beam16():
        off = [13, 15, 19, 21, 23, 29, 31, 33, 35, 37, 38]
        on = [3, 5, 7, 11, 40]
        GPIO.output(on,1)
        GPIO.output(off,0)

# Toggle a specific switch
def switch1():                              
        if GPIO.input(3):                                               # if pin is high
                GPIO.output(3, 0)
                sw1.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 1 (off)')  
        else:
                GPIO.output(3, 1)
                sw1.config(bg='red', activebackground='red', image=OpenSw, text='Switch 1 (on)')
        
def switch2():        
        if GPIO.input(5):
                GPIO.output(5, 0)
                sw2.config(bg='grey', activebackground='grey',image=ClosedSw,text='Switch 2 (off)')
        else:
                GPIO.output(5, 1)
                sw2.config(bg='red', activebackground='red', image=OpenSw, text='Switch 2 (on)')
        
def switch3():
        if GPIO.input(7):
                GPIO.output(7, 0)
                sw3.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 3 (off)')
        else:
                GPIO.output(7, 1)
                sw3.config(bg='red', activebackground='red', image=OpenSw, text='Switch 3 (on)')

def switch4():
        if GPIO.input(11):
                GPIO.output(11, 0)
                sw4.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 4 (off)')
        else:
                GPIO.output(11, 1)
                sw4.config(bg='red', activebackground='red', image=OpenSw, text='Switch 2 (on)')

def switch5():
        if GPIO.input(13):
                GPIO.output(13, 0)
                sw5.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 5 (off)')
        else:
                GPIO.output(13, 1)
                sw5.config(bg='red', activebackground='red', image=OpenSw, text='Switch 5 (on)')

def switch6():
        if GPIO.input(15):
                GPIO.output(15, 0)
                sw6.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 6 (off)')
        else:
                GPIO.output(15, 1)
                sw6.config(bg='red', activebackground='red', image=OpenSw, text='Switch 6 (on)')
        
def switch7():
        if GPIO.input(19):
                GPIO.output(19, 0)
                sw7.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 7 (off)')
        else:
                GPIO.output(19, 1)
                sw7.config(bg='red', activebackground='red', image=OpenSw, text='Switch 7 (on)')

def switch8():
        if GPIO.input(21):
                GPIO.output(21, 0)
                sw8.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 8 (off)')
        else:
                GPIO.output(21, 1)
                sw8.config(bg='red', activebackground='red', image=OpenSw, text='Switch 8 (on)')

def switch9():
        if GPIO.input(23):
                GPIO.output(23, 0)
                sw9.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 9 (off)')
        else:
                GPIO.output(23, 1)
                sw9.config(bg='red', activebackground='red', image=OpenSw, text='Switch 9 (on)')


def closeAll():
        for i in range(0,16):
                GPIO.output(pins[i], 0)
        sw1.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 1 (off)')
        sw2.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 2 (off)')
        sw3.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 3 (off)')
        sw4.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 4 (off)')
        sw5.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 5 (off)')
        sw6.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 6 (off)')
        sw7.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 7 (off)')
        sw8.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 8 (off)')
        sw9.config(bg='grey', activebackground='grey', image=ClosedSw, text='Switch 9 (off)')
        TogAll.config(image=ClosedSw, command=openAll, text='Open all switches', bd=3, bg='grey', activebackground='grey')
        
def openAll():
        for i in range(0,16):
                GPIO.output(pins[i], 1)
        sw1.config(bg='red', activebackground='red', image=OpenSw, text='Switch 1 (on)')
        sw2.config(bg='red', activebackground='red', image=OpenSw, text='Switch 2 (on)')
        sw3.config(bg='red', activebackground='red', image=OpenSw, text='Switch 3 (on)')
        sw4.config(bg='red', activebackground='red', image=OpenSw, text='Switch 4 (on)')
        sw5.config(bg='red', activebackground='red', image=OpenSw, text='Switch 5 (on)')
        sw6.config(bg='red', activebackground='red', image=OpenSw, text='Switch 6 (on)')
        sw7.config(bg='red', activebackground='red', image=OpenSw, text='Switch 7 (on)')
        sw8.config(bg='red', activebackground='red', image=OpenSw, text='Switch 8 (on)')
        sw9.config(bg='red', activebackground='red', image=OpenSw, text='Switch 9 (on)')        
        TogAll.config(image=OpenSw, command=closeAll, text='Close all switches', bd=3, bg='red', activebackground='red')


def exitprog():                                                 # Close GUI
        win.quit()
        GPIO.cleanup()                                          # Turn off all pins
        win.destroy()

# Beam buttons
b=Button(win, image=photo1, compound=TOP,  text='0 deg', command=beam15, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=640, y=280)
b=Button(win, image=photo2, compound=TOP,  text='22.5 deg', command=beam16, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=605, y=175)
b=Button(win, image=photo3, compound=TOP,  text='45 deg', command=beam16, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=535, y=70)
b=Button(win, image=photo4, compound=TOP,  text='67.5 deg', command=beam2, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=430, y=30)
b=Button(win, image=photo5, compound=TOP,  text='90 deg', command=beam3, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=325, y=10)
b=Button(win, image=photo6, compound=TOP,  text='112.5 deg', command=beam4, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=220, y=30)
b=Button(win, image=photo7, compound=TOP,  text='135 deg', command=beam5, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=115, y=70)
b=Button(win, image=photo8, compound=TOP,  text='157.5 deg', command=beam6, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=45, y=175)
b=Button(win, image=photo9, compound=TOP,  text='180 deg', command=beam7, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=10, y=280)
b=Button(win, image=photo10, compound=TOP,  text='202.5 deg', command=beam8, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=45, y=385)
b=Button(win, image=photo11, compound=TOP,  text='225 deg', command=beam9, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=115, y=490)
b=Button(win, image=photo12, compound=TOP,  text='247.5 deg', command=beam10, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=220, y=550)
b=Button(win, image=photo13, compound=TOP,  text='270 deg', command=beam11, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=325, y=570)
b=Button(win, image=photo14, compound=TOP,  text='292.5 deg', command=beam12, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=430, y=550)
b=Button(win, image=photo15, compound=TOP,  text='315 deg', command=beam13, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=535, y=490)
b=Button(win, image=photo16, compound=TOP, text='337.5 deg', command=beam14, bd=3, bg='white', activebackground='white', activeforeground='grey', height=80, width=70)
b.place(x=605, y=385)

# Switch buttons
sw1=Button(win, image=ClosedSw, compound=TOP, command=switch1, text='Switch 1 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw1.place(x=1430,y=280)
sw2=Button(win, image=ClosedSw, compound=TOP, command=switch2, text='Switch 2 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw2.place(x=1400,y=175)
sw3=Button(win, image=ClosedSw, compound=TOP, command=switch3, text='Switch 3 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw3.place(x=1350, y=70)
sw4=Button(win, image=ClosedSw, compound=TOP, command=switch4, text='Switch 4 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw4.place(x=1230, y=30)
sw5=Button(win, image=ClosedSw, compound=TOP, command=switch5, text='Switch 5 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw5.place(x=1110, y=10)
sw6=Button(win, image=ClosedSw, compound=TOP, command=switch6, text='Switch 6 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw6.place(x=990, y=30)
sw7=Button(win, image=ClosedSw, compound=TOP, command=switch7, text='Switch 7 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw7.place(x=870, y=70)
sw8=Button(win, image=ClosedSw, compound=TOP, command=switch8, text='Switch 8 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw8.place(x=820, y=175)
sw9=Button(win, image=ClosedSw, compound=TOP, command=switch9, text='Switch 9 (on)', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=80, width=70)
sw9.place(x=780, y=280)


TogAll=Button(win, image=ClosedSw, compound=TOP, command=openAll, text='Open all switches', bd=3, bg='red', activebackground='red', fg='white', activeforeground='black', height=50, width=100)
TogAll.place(x=1100, y=200)

label=Label(win, text='Choose Azimuth Direction (Phaseshifter)', font='Verdana 14 bold').pack(padx=160, pady=100, side=LEFT)

label=Label(win, text='Choose Elevation Angle (Amplifier)', font='Verdana 14 bold').pack(padx=180, pady=100, side=RIGHT)

 
exitButton=Button(win, text='exit', font=myfont, command=exitprog, bd=3, bg='cyan', height=1, width=6)
exitButton.place(x=770, y=650)



mainloop()
