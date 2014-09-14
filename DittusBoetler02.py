#!/usr/local/bin/python
from Tkinter import *
import math


#class DittusBoetler:
#print 'Dittus2'
        #units = fields
def calc(entries):
           # period rate:
           #P = (float(entries['Annual Rate'].get())
           #print("P", P)
           # principal loan:
           P = float(entries['Static Pressure'].get())
           T =  float(entries['Static Temperature'].get())
           M = float(entries['Mass Flow Rate'].get())
           D = float(entries['Hydraulic Diameter'].get())
           #Pr = float(entries['Molecular Pr'].get())
           #convert units to SI:
           if Punits.get() == "bar":
                P = P*100000
                print 'P=',P,'Pa'
           elif Punits.get() == "psi":
                P = P*6894.757
                print 'P=',P,'Pa'
           elif Punits.get() == "Pa":
                P = P
                print 'P=',P,'Pa'
           if Tunits.get() == "C":
                T = T + 273.15
                print 'T=',T,'K'
           elif Tunits.get() == "F":
                T = (T - 32)*5/9 + 273
                print 'T=',T,'K'
           elif Tunits.get() == "R":
                T = T*0.5556
                print 'T=',T,'K'
           elif Tunits.get() == "K":
                T = T
                print 'T=',T,'K'
           if Munits.get() == "lbm/s":
                M = M*0.4535924
                print 'mdot=',M,'kg/s'
           elif Munits.get() == "kg/s":
                M = M
                print 'mdot=',M,'kg/s'
           if Dunits.get() == "in":
                D = D*0.0254
                print 'D=',D,'m'
           elif Dunits.get() == "cm":
                D = D*0.01
                print 'D=',D,'m'
           elif Dunits.get() == "m":
                D = D
                print 'D=',D,'m'
           if heating.get() == "Yes":
               n = 0.4
           elif heating.get() == "No":
               n =0.3
            #that was fun.  Now lets do some calculations
           print 'Dittus - Boelter'
           rho = P/(8314.34/28.96*T)   # [kg/m^3], density from ideal gas law
           print 'rho=',rho,'kg/m^3'
           mu = 0.0000171*pow((T/273),0.7)    # [kg/(ms)], viscosity from Power law
           Re = 4*M/(math.pi*D*mu)
           print 'Re=',Re
           Pr = -9.1127E-21*pow(T,6) - 2.9674E-17*pow(T,5) + 5.0926E-13*pow(T,4) - 1.6135E-9*pow(T,3) + 2.0551E-6*pow(T,2) - 1.0695E-3*T + 8.7844E-1
           print 'Pr=',Pr
           Nu = 0.023*pow(Re,0.8)*pow(Pr,n)
           print 'Nu=',Nu
           k = 1.3819E-20*pow(T,6)-9.1506E-17*pow(T,5)+2.2342E-13*pow(T,4)-2.2872E-10*pow(T,3) + 6.8867E-8*pow(T,2) + 8.0128E-5*T - 7.6694E-4
           h = Nu*k/D
           if hunits.get() == "BTU/(hr-ft^2-R)":
               h = h*0.176756
               print 'h=',h,'BTU/(hr-ft^2-R)'
           else:
               print 'h=',h,'W/(m^2K)'
           rho = ("%8.2f" % rho).strip()
           entries['Density'].delete(0,END)
           entries['Density'].insert(0, rho )
           Re = ("%8.1f" % Re).strip()
           entries['Reynolds Number'].delete(0,END)
           entries['Reynolds Number'].insert(0, Re )
           #print("Remaining Loan: %f" % remaining)
           Nu = ("%8.1f" % Nu).strip()
           entries['Nu'].delete(0,END)
           entries['Nu'].insert(0, Nu )
           h = ("%8.1f" % h).strip()
           entries['h'].delete(0,END)
           entries['h'].insert(0, h )

def makeform(root, fields):
           entries = {}
           uni = {}
           i = 1;
           #title = Label(master,text = "Input is blue, output is red")
           #title.grid(row = 0, column = 1)
           for field in fields:
              row = Frame(root)
              if i < 6:
                  color = "blue"
              else:
                  color = "red"
              lab = Label(row, width=22, text=field+": ", anchor='w', fg = color)
              lab.pack(side=LEFT)
              if i == 5: #heating question
                    v = StringVar()
                    v.set('Y')
##                    b = Radiobutton(text='Y',variable=v)
##                    b.pack(side=RIGHT)
              else:
                  ent = Entry(row)
                  ent.insert(0,'0')  #inserts default text
              row.pack(side=TOP, fill=X, padx=5, pady=5)

              if i == 1:
                  global Punits
                  Punits = Spinbox(row,values = ("bar", "psi", "Pa"))
                  Punits.pack(side=RIGHT,expand = NO, fill = X)
                  #ent.insert(0,'1')
              elif i == 2:
                  global Tunits
                  Tunits = Spinbox(row,values = ("C", "F", "R", "K"))
                  Tunits.pack(side=RIGHT,expand = NO, fill = X)
              elif i == 3:
                  global Munits
                  Munits = Spinbox(row,values = ("kg/s","lbm/s"))
                  Munits.pack(side=RIGHT,expand = NO, fill = X)
              elif i == 4:
                  global Dunits
                  Dunits = Spinbox(row,values = ("in","m","cm"))
                  Dunits.pack(side=RIGHT,expand = NO, fill = X)
              elif i == 5:
                  global heating
                  heating = Spinbox(row,values = ("No","Yes"))
                  heating.pack(side=LEFT,expand = NO, fill = X)
              elif i == 6:
                  units = Spinbox(row,values = ("kg/m^3"))
                  units.pack(side=RIGHT,expand = NO, fill = X)
              elif i == 7:
                  units = Spinbox(row,values = ("-"))
                  units.pack(side=RIGHT,expand = NO, fill = X)
              elif i == 8:
                  units = Spinbox(row,values = ("-"))
                  units.pack(side=RIGHT,expand = NO, fill = X)
              elif i == 9:
                  global hunits
                  hunits = Spinbox(row,values = ("W/(m^2K)","BTU/(hr-ft^2-R)"))
                  hunits.pack(side=RIGHT,expand = NO, fill = X)

              ent.pack(side=RIGHT, expand=NO, fill=X)
              entries[field] = ent
              i = i + 1
           return entries
def quit2():
        root.destroy()

def aboutDB():
   def quit2():
       root.destroy()
    #if __name__ == '__main__':
   root = Tk()
   #print units.get()
   lab1 = Label(root, text = 'Nu = 0.023 Re^{4/5}Pr^n, where n = 0.4 for heating (Twall > Tgas) and n = 0.3 for cooling (Twall<Tgas)')
   lab1.pack(side = TOP)
   lab2 = Label(root, text = 'Re > 10 000, 0.7 < Pr < 160 and L/D > 10, ~25% Error')
   lab2.pack(side = TOP)
   lab3 = Label(root, text = 'Not appropriate for large property variations.')
   lab3.pack(side = TOP)
   #print ents
   b3 = Button(root, text='Quit', command=quit2)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()


#if __name__ == '__main__':
#def __init__(self,parent):
   #self.master= parent
   #top = Frame(parent)
root = Tk()
fields = ('Static Pressure', 'Static Temperature', 'Mass Flow Rate', 'Hydraulic Diameter','Twall > Tgas','Density', 'Reynolds Number', 'Nu', 'h')
ents = makeform(root, fields)
#print units.get()
root.bind('<Return>', (lambda event, e=ents: fetch(e)))
lab1 = Label(root, text = 'Nu_d = 0.023 Re^{4/5}_d Pr^{n}')
lab1.pack(side = TOP)
lab2 = Label(root, text = 'Blue is input', fg = "blue")
lab2.pack(side = TOP)
lab3 = Label(root, text = 'Red is output', fg = "red")
lab3.pack(side = TOP)
#print ents
b1 = Button(root, text='Calculate',
      command=(lambda e=ents: calc(e)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='About', command=aboutDB)
b2.pack(side=LEFT, padx=5, pady=5)
b3 = Button(root, text='Quit', command=quit2)
b3.pack(side=LEFT, padx=5, pady=5)
#print 'trying'
root.mainloop()


#DB = DittusBoetler(root)


##root = Tk()
##DB = DittusBoetler(root)
##root.mainloop()

