from tkinter import *
#import pdb
import math
#global variabelen
toggle = 1

c = ''

dct = {'a':'','b':''}

lastans = ''
lastans2 = ''
def reset():
	#my_entry.delete(0, 'end')	
	var.set('Version 1.2\nCopyright by MaoTek  ')
	global toggle
	global c
	toggle = 1
	c = ''
	dct['a'] = ''
	dct['b'] = ''
	my_entry.config(state=NORMAL)
	my_entry.delete(0, 'end')

	print(dct)
	print(f'toggle = {toggle}')
	print(f'operator = {c}')

def send(x):
	if toggle == 1:
		dct['a'] = dct['a'] + str(x)
		my_entry.insert(100, x)	
	elif toggle == -1:
		if dct['a'] != '':
			if dct['b'] == '':
				my_entry.delete(0, 'end')
			else:
				pass
			dct['b'] = dct['b'] + str(x)
			my_entry.insert(100, x)
		else:
			pass
			#dct['b'] = dct['b'] + str(x)
			#my_entry.insert(100, x)
	else:
		pass
	
	print(dct)
	print(f'toggle = {toggle}')
	print(f'operator = {c}')

def send2(x):
	global toggle
	global c
	my_entry.delete(0, 'end')

	if toggle == -1:
		if dct['a'] != '' and dct['b']  != '':			
			enter()
			c = x
			toggle = -1
		else:
			my_entry.insert(100, 'EmptyError_#send2')
			my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')						
	else:
		if '..' in dct['a']:
			my_entry.insert(100,'DotError_#Send2')
			my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')


		elif dct['a'] == '' and dct['b']  == '':
			my_entry.insert(100,'EmptyError_#Send2')
			my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')
		else:
			toggle *= -1
			c = x

	print(dct)
	print(f'toggle = {toggle}')
	print(f'operator = {c}')

def send3():
	if toggle == 1:
		if '-' not in dct['a']:
			my_entry.delete(0, 'end')
			dct['a'] = '-'+ dct['a']
			my_entry.insert(100, dct['a'])
		else:
			my_entry.delete(0, 'end')
			dct['a'] = dct['a'][1:]
			my_entry.insert(100, dct['a'])
	elif toggle == -1:
		if '-' not in dct['b']:
			my_entry.delete(0, 'end')
			dct['b'] = '-'+ dct['b']
			my_entry.insert(100, dct['b'])
		else:
			my_entry.delete(0, 'end')
			dct['b'] = dct['b'][1:]
			my_entry.insert(100, dct['b'])
	else:
		pass

	print(dct)
	print(f'toggle = {toggle}')
	print(f'operator = {c}')

def enter():	
	my_entry.delete(0, 'end')	
	global c
	global toggle			
	global lastans
	global lastans2
	x = ''

	try:
		if '..' in dct['a']:
			my_entry.insert(100,'DotError_Error#Enter')
			my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')
		#elif len(dct['a']) > 12:
			#my_entry.insert(100,'Overflow')
			#my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')
		elif '--' in dct['a']:
			my_entry.insert(100,'Minus_Error#Enter')
			my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')
		elif c == 'x':
			if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
				x = float(dct['a'])*float(dct['b'])
			else:
				x = int(dct['a'])*int(dct['b'])

		elif c == '+':
			if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
				x = float(dct['a'])+float(dct['b'])
			else:
				x = int(dct['a'])+int(dct['b'])

		elif c == '-':
			if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
				x = float(dct['a'])-float(dct['b'])
			else:
				x = int(dct['a'])-int(dct['b'])

		elif c == '/':
			if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
				x = float(dct['a'])/float(dct['b'])
			else:
				x = int(dct['a'])/int(dct['b'])
	except:
		try:
			if toggle == 1:
				dct['b'] = lastans
				if '..' in dct['a']:
					my_entry.insert(100,'DotError_Enter')
					my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')
				#elif len(dct['a']) > 12:
					#my_entry.insert(100,'Overflow')
					#my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')
				elif c == 'x':
					if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
						x = float(dct['a'])*float(dct['b'])
					else:
						x = int(dct['a'])*int(dct['b'])

				elif c == '+':
					if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
						x = float(dct['a'])+float(dct['b'])
					else:
						x = int(dct['a'])+int(dct['b'])

				elif c == '-':
					if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
						x = float(dct['a'])-float(dct['b'])
					else:
						x = int(dct['a'])-int(dct['b'])

				elif c == '/':
					if '.' in dct['a'] or '.' in dct['b'] or len(dct['a']) > 10:
						x = float(dct['a'])/float(dct['b'])
					else:
						x = int(dct['a'])/int(dct['b'])

				my_entry.insert(100,x)
			
				dct['a'] = str(x)
				lastans = dct['b']
				#dct['b'] = ''
				toggle = 1	
				lastans2 = dct['a']	
		except:
			my_entry.insert(100,'OverflowError')
			my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')

	else:
		my_entry.insert(100,x)		
		dct['a'] = str(x)
		lastans = dct['b']
		dct['b'] = ''
		toggle = 1	
		lastans2 = dct['a']	
	finally:	
			print(dct)
			print(f'toggle = {toggle}')
			print(f'operator = {c}')

def kwadraat():
	global c
	dct['b'] = dct['a']
	c = 'x'
	#try:
		#dct['a'] =  str(int(dct['a'])**2)
	#except:
		#dct['a'] =  str(float(dct['a'])**float(dct['a']))
	#my_entry.insert(100,dct['a'])
	enter()

def wortel():
	my_entry.delete(0, 'end')
	try:
		dct['a'] = str(int(dct['a']) ** 0.5)
	except:
		dct['a'] = str(float(dct['a']) ** 0.5)
	my_entry.insert(100,dct['a'])


def ans():
	global lastans2
	if toggle == 1:
		my_entry.delete(0, 'end')
		dct['a'] = lastans2
		my_entry.insert(100,dct['a'])
	elif toggle == -1:
		my_entry.delete(0, 'end')
		dct['b'] = lastans2
		my_entry.insert(100,dct['b'])



def easter():
	my_entry.delete(0, 'end')
	my_entry.insert(100, 'CHINA #1')
	var.set('     Fornite is cool!      \n      Minecraft is gay!     ')
	my_entry.config(state=DISABLED,disabledbackground="red",disabledforeground='yellow')

if __name__ == '__main__':	

	root = Tk()
	root.geometry('280x595')

	frame = Frame(root,cursor='cross',bg='black')
	frame.pack()
	frame2 = Frame(root,cursor='cross')
	frame2.pack()
	frame3 = Frame(root,cursor='cross')
	frame3.pack()
	frame4 = Frame(root,cursor='cross')
	frame4.pack()
	frame5 = Frame(root,cursor='cross')
	frame5.pack()
	frame7 = Frame(root,cursor='cross')
	frame7.pack()
	frame6 = Frame(root,cursor='cross',bg='black')
	frame6.pack()

	var = StringVar()
	var.set('Version 1.2\nCopyright by MaoTek  ')

	canvas = Canvas(frame,bd=0, highlightthickness=0, width = 275,height = 150,bg='black')
	file = PhotoImage(file = 'cn2.png')
	image = canvas.create_image(137.5,93, image=file)
	canvas.pack()

	my_entry = Entry(frame, width = 24, selectforeground = 'red',bg='red',fg='yellow',font = 'Arial 13', bd = 3, relief = 'ridge')
	my_entry.insert(10, '')
	my_entry.pack(padx = 1,pady =3, ipady = 6,side=LEFT,fill=X)

	button = Button(frame, text = 'CE',command = reset,width = 4,bg='red',fg='yellow',font=' Arial 13',bd=3,relief='ridge')
	button.pack(side=LEFT,padx=0,ipady=3,ipadx=1)

	button = Button(frame2, text = 7,command = lambda: send(7),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame2, text = 8,command = lambda: send(8),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame2, text = 9,command = lambda: send(9),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame2, text = '+',command = lambda: send2('+'),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=9)

	button = Button(frame3, text = 4,command = lambda: send(4),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame3, text = 5,command = lambda: send(5),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame3, text = 6,command = lambda: send(6),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame3, text = '-',command = lambda: send2('-'),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=9)

	button = Button(frame4, text = 1,command = lambda: send(1),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame4, text = 2,command = lambda: send(2),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame4, text = 3,command = lambda: send(3),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame4, text = 'x',command = lambda: send2('x'),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=9)

	button = Button(frame5, text = 0,command = lambda: send('0'),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame5, text = '.',command = lambda: send('.'),height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame5, text = '/',command = lambda: send2('/'),height=1,width = 2,fg='yellow',bg='red',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=4)
	button = Button(frame5, text = '=',command = enter,height=1,width = 2,bg='red',fg='yellow',font='Arial 30',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=9)

	button = Button(frame7, text = 'π',command = lambda: send(math.pi),height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=8)
	button = Button(frame7, text = 'x²',command = kwadraat,height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=8)
	button = Button(frame7, text = '√x',command = wortel,height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=8)
	button = Button(frame7, text = 'ans',command = ans,height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=8)
	button = Button(frame7, text = '-/+',command = send3,height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	button.pack(side=LEFT,ipadx=20)





	#button = Button(frame6, text= 'π',command = lambda: send(math.pi),height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	#button.pack(side=LEFT,padx=3,ipadx = 4)

	label = Label(frame6, textvariable = var,fg='yellow',bg='black')
	label.pack(side=LEFT)

	#button = Button(frame6, text= '-/+',command = send3,height=1,width = 2,bg='red',fg='yellow',font='Arial 15',bd=3,relief='ridge')
	#button.pack(side=LEFT,padx=3,ipadx = 4)

	root.configure(bg='black')
	root.resizable(False,False)
	root.title('MaoTek Calculator')
	root.iconbitmap('logo.ico')
	root.mainloop()
