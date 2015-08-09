"""		IMPORT PACKAGES	"""

import MySQLdb
from Tkinter import *
from ttk import *
from datetime import *


#			TEACHER CLASS
class Teacher(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent



		
		self.initUI()
		self.parent.geometry("900x400+20+40")
			


#"""		INITIALIZING UI	"""

	def initUI(self):
		self.parent.title("Lab Manager")
		self.pack(fill=BOTH,expand=1)
		self.style=Style()
		self.style.configure("TFrame",background="#433")		


#****************DROP-DOWN LIST


#***NAMES OF OPTIONMENU

		self.ov=StringVar()
		self.ov1=StringVar()
		self.ov2=StringVar()
		self.ov3=StringVar()

#****OPTIONMENU MEMBERS

		self.lo=["SE","TE","BE"]	
		self.lo1=[]
		self.lo2=[]
		self.lo3=[]	
		self.Option=OptionMenu(self,self.ov,*self.lo)
		
		self.Option.place(x=240,y=60,height=22,width=70)


		self.Option1=OptionMenu(self,self.ov1,*self.lo1)

		self.Option1.place(x=440,y=60,height=22,width=70)

		self.Option2=OptionMenu(self,self.ov2,*self.lo2)

		self.Option2.place(x=540,y=60,height=22,width=70)

		self.Option3=OptionMenu(self,self.ov3,*self.lo3)

		self.Option3.place(x=340,y=60,height=22,width=70)



	

#***************LABEL

		self.l1=Label(self,text="Roll no")
		self.l1.place(x=250,y=130)

#****************BUTTONS

		self.button=Button(self,text="GO",command=self.FDisplay)
		self.button.place(x=640,y=60)
	
		self.button1=Button(self,text="GO",command=self.FRoll)
		self.button1.place(x=640,y=130)

		self.button1=Button(self,text="Exit",command=quit)
		self.button1.place(x=800,y=100)

#****************TEXTBOXES

		vcmd = (self.register(self.OnValidate), 
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

		self.tb=Entry(self,validate="key",validatecommand=vcmd)		
		self.tb.place(x=320,y=130)

#******************LABEL

		self.l1=Label(self,text="OR")
		self.l1.place(x=240,y=100)

#*************  Display Choice 

	def FDisplay(self):


		self.db=MySQLdb.connect("localhost","root","Jhearts","MyDB")
		self.cursor=self.db.cursor()

		if(self.ov.get()=="SE"):
			pass		
		query="select * from TE3_L where Year=%s "%year
		
		# ()
		sub1=""
		self.cursor.execute(query)
		self.db.commit()
		data=StringVar()		
		data=self.cursor.fetchall()
		
		self.cursor.close()
		self.db.close()

#****************ROLL NUMBER SEARCH

	def FRoll(self):


		self.db=MySQLdb.connect("localhost","root","Jhearts","MyDB")
		self.cursor=self.db.cursor()
		roll=IntVar()
		roll=self.tb.get()	

		query = "select * from TE3_L where Roll_no=%s" %roll

#group by Subject and order by Assign"

		self.cursor.execute(query)
		self.db.commit()
		self.data1=StringVar()

#****LABEL TO DISPLAY OUTPUT

		l2=Label(self,textvariable=self.data1,relief=RAISED)
		for i in range(self.cursor.rowcount):

			self.data=self.cursor.fetchone()
			print self.data		
			self.data1.set(self.data)

		
		
		
		l2.place(x=50,y=200)

		var = StringVar()

		print self.data1
		self.cursor.close()
		self.db.close()
			
#****************VALIDATION
	def OnValidate(self, d, i, P, s, S, v, V, W):
		if(S<="9" and S>="0" and len(P)<=4):
                        return (S==S)
		else:
		       	return(0)




#		MAIN FUNCTION

def main():
	root=Tk()
	ob=Teacher(root)
	root.mainloop()

if  __name__=='__main__':
	main()
