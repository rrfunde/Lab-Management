"""		IMPORT PACKAGES	"""

import MySQLdb
from Tkinter import *
from ttk import *
from datetime import *

""""		LAB CLASS		"""

class Lab(Frame):

	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.Year=""
		self.Class=""
		self.Batch=""
		self.initUI()
		self.parent.geometry("900x400+20+40")
		#self.center()		

		
#"""		CENTEING WINDOW	"""

	
	def center(self):
		w=500
		h=300
		sw=(self.parent.winfo_screenwidth()+200)/2
		sh=(self.parent.winfo_screenheight())/2
		self.parent.geometry('%dx%d+%d+%d'%(w,h,sw,sh))

#"""		INITIALIZING UI	"""

	def initUI(self):
		self.parent.title("Status")
		self.pack(fill=BOTH,expand=1)
		self.style=Style()
		self.style.configure("TFrame",background="#433")		


		WIDGETS	

#****************BUTTONS

		self.button=Button(self,text="GO",command=self.Update)
		self.button1=Button(self,text="Exit",command=self.quit)		
		self.button1.place(x=180,y=250)
		self.button.place(x=90,y=250)

#****************TEXTBOXES

#******validate textbox

		vcmd = (self.register(self.OnValidate), 
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

		vcmd1=(self.register(self.OnValidate1),'%d','%i', '%P', '%s', '%S', '%v', '%V', '%W')
		
		self.tb=Entry(self,validate="key", validatecommand=vcmd,width=13)		
		self.tb.place(x=70,y=40)

	
		self.tb1=Text(self,height=8,width=60)
		self.tb1.place(x=70,y=97)
		



		
		
#******************LABEL

		self.l1=Label(self,text="Roll no")
		self.l1.place(x=10,y=40)

		self.l2=Label(self,text="Status")
		self.l2.place(x=10,y=100)


#****************OPTIONMENU

		self.List=[i for i in range(16)]		

		self.ov=StringVar()
		self.op1=OptionMenu(self,self.ov,"","PL1","PL2")
		self.ov.set("Subject")
		self.op1.place(x=210,y=40)


		self.ov1=StringVar()
		
		self.op1=OptionMenu(self,self.ov1,*self.List)
		self.ov1.set("AssignMent")
		self.op1.place(x=350,y=40)


#****************ONCLICK ACTION


	def Update(self):

#***************ACCEPTING INPUT FROM TEXTBOXES

		self.DRoll=IntVar()
		self.DRoll=int(self.tb.get())
		self.DStatus=self.tb1.get(0.0,END)
		self.DStatus=self.DStatus[0:127]
		self.Subject=self.ov.get()
		print self.Subject

#		FINDING ********YEAR *****CLASS*********BATCH********
		self.Temp=self.DRoll	
		self.F=100		

		a=self.Temp/self.F
		self.y=a/10
		self.c=a%10
		
		self.Temp=self.Temp%self.F
		self.F *=10
		
	
		print self.y,self.c
		
		if(self.y==2):
			
			self.SE()
		
		elif(self.y==3):
			self.TE()


		elif(self.y==4):
			self.BE()

		else:
#self.l3.text("Invalid no")
			exit(0)

		print self.Year,self.Class,self.Batch

#"""   DATABASE CONNECTIVITY            """

		db=MySQLdb.connect("localhost","root","Jhearts","MyDB")
		cursor=db.cursor()
		
		self.Ddate = datetime.now().date() + timedelta(days=1)

		q1=("select * from TE3_L where Roll_no=%s and date1=%s",(self.DRoll,self.Ddate))
		cursor.execute(q1)
		q2=cursor.fetchone()
#		print q2
		query="insert into TE3_L(date1,Roll_no,status,Year,Class,Batch) values('%s','%s','%s','%s','%s','%s')"%(self.Ddate,self.DRoll,self.DStatus,self.Year,self.Class,self.Batch)

		cursor.execute(query)
		db.commit()
		data=cursor.fetchall()
		#print data ,
		cursor.close()
		db.close()

			

		


#		SE***1*********************

	def SE(self):
		
		self.Year="SE"				
		
		
		if(self.c==1):
			self.Class="SE1"
			if(self.Temp<=20 ):
				self.Batch="E1"

			elif(self.Temp<=40):
				self.Batch="F1"

			elif(self.Temp<=60):
				self.Batch="G1"

			elif(self.Temp<=81):
				self.Batch="H1"
			
			else:
				exit(0)	

		elif(self.c==2):
			self.Class="SE2"

			
			if(self.Temp<=20):
				self.Batch="E2"

			elif(self.Temp<=40):
				self.Batch="F2"

			elif(self.Temp<=60):
				self.Batch="G2"

			elif(self.Temp<=80):
				self.Batch="H2"

			else:
				exit(0)	


		elif(self.c==3):
			self.Class="SE3"
			if(self.Temp<=20):
				self.Batch="E3"

			elif(self.Temp<=40):
				self.Batch="F3"

			elif(self.Temp<=60):
				self.Batch="G3"

			elif(self.Temp<=80):
				self.Batch="H3"
			else:
				exit(0)	

		elif(self.c==4):
			self.Class="SE4"
			if(self.Temp<=20):
				self.Batch="E4"

			elif(self.Temp<=40):
				self.Batch="F4"

			elif(self.Temp<=60):
				self.Batch="G4"

			elif(self.Temp<=80):
				self.Batch="H4"

		else:
			exit(0)
#		TE***************************
	def TE(self):
		self.Year="TE"				
		
		
		if(self.c==1):
			self.Class="TE1"
			if(self.Temp<=20):
				self.Batch="K1"

			elif(self.Temp<=40):
				self.Batch="L1"

			elif(self.Temp<=60):
				self.Batch="M1"

			elif(self.Temp<=80):
				self.Batch="N1"
			else:
				exit(0)	



		elif(self.c==2):
			self.Class="TE2"
			if(self.Temp<=20):
				self.Batch="K2"

			elif(self.Temp<=40):
				self.Batch="L2"

			elif(self.Temp<=60):
				self.Batch="M2"

			elif(self.Temp<=80):
				self.Batch="N2"
			else:
				exit(0)	


		elif(self.c==3):
			self.Class="TE3"
			if(self.Temp<=20):
				self.Batch="K3"

			elif(self.Temp<=40):
				self.Batch="L3"

			elif(self.Temp<=60):
				self.Batch="M3"

			elif(self.Temp<=80):
				self.Batch="N3"
			else:
				exit(0)	


		elif(self.c==4):
			self.Class="TE4"
			if(self.Temp<=20):
				self.Batch="K4"

			elif(self.Temp<=40):
				self.Batch="L4"

			elif(self.Temp<=60):
				self.Batch="M4"

			elif(self.Temp<=80):
				self.Batch="N4"


		else:
			exit(0)
#**************BE

	def BE(self):
		self.Year="BE"				
		
		
		if(self.c==1):
			self.Class="BE1"
			if(self.Temp<=20):
				self.Batch="E1"

			elif(self.Temp<=40):
				self.Batch="F1"

			elif(self.Temp<=60):
				self.Batch="G1"

			elif(self.Temp<=80):
				self.Batch="H1"
			else:
				exit(0)	



		elif(self.c==2):
			self.Class="BE2"
			if(self.Temp<=20):
				self.Batch="E2"

			elif(self.Temp<=40):
				self.Batch="F2"

			elif(self.Temp<=60):
				self.Batch="G2"

			elif(self.Temp<=80):
				self.Batch="H2"
			else:
				exit(0)	

		else:
			exit(0)
	
#****************VALIDATION
	def OnValidate(self, d, i, P, s, S, v, V, W):
		if(S<="9" and S>="0" and len(P)<=4):
                        return (S==S)
		else:
		       	return(0)

	def OnValidate1(self, d, i, P, s, S, v, V, W):
		if(i>"126"):
			return(0)

#		MAIN FUNCTION

def main():
	root=Tk()
	ob=Lab(root)
	root.mainloop()

if  __name__=='__main__':
	main()

