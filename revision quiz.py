from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from tkinter import messagebox as mb
import json




def clear():
	userenter.delete(0,END)
	pw.delete(0,END)

def close():
	win.destroy()	


def login():
	if username.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="logins")
			cur = con.cursor()

			cur.execute("select * from logins where username=%s and password = %s",(username.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Logged in!" , parent = win)
				close()
				level_tk()
				
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = win)



def level_tk():

        def easy():
                root.destroy()

                class Quiz:
    
                        def __init__(self):
                
                                self.q_num=0
                
                                self.revisionQuiz_title()
                
                                self.display_question()
                        
                                self.opt_selected=IntVar()
            
                                self.opts=self.radio_buttons()
                        
                                self.display_options()

                                self.feedback=Label(gui, pady=10, font=("ariel", 15, "bold"), bg="azure")
                                self.feedback.place(x=340, y=370)
                        
                                self.buttons()
                        
                                self.data_size=len(question)
                    
                                self.correct=0


                        def display_report(self):
                                
                                wrong_ans = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_ans}"
                                
                                score = int(self.correct / self.data_size * 100)
                                report = f"Score: {score}%"
                               
                                mb.showinfo("Report", f"{report}\n{correct}\n{wrong}")



                        def check_ans(self, q_num):
                                
                                if self.opt_selected.get() == answer[q_num]:
                                        return True

                     
                        def next_btn(self):
                                
                    
                                if self.check_ans(self.q_num):
                                        
                                        self.correct += 1
                                        self.feedback["fg"] = "springgreen"
                                        self.feedback["text"] = 'Correct answer! \U0001F44D'
                                        self.q_num += 1

                                else:
                                        self.feedback['fg'] = 'indianred'
                                        self.feedback['text'] = ('Wrong! \u274E \n'
                                                                 f'The correct answer is {answer[self.q_num]}')
                                        self.q_num += 1
                                                                 
                    
                                if self.q_num==self.data_size:
                                        
 
                                        gui.destroy()

                                        def restart_btn():
                                
                                                window.destroy()
                                                level_tk()


                                        window = Tk()
                                        window.geometry("900x550")
                                        window.title("Revision Quiz")
                                        window.config(background="azure")

                                        choose_opt = Label(window, text="Please choose whether to restart the quiz or show the report and quit",
                                                           font='verdana 15 bold', bg="azure")
                                        choose_opt.place(x=70, y=100)

                                        restart = Button(window, text="Restart", font='verdana 15', command=restart_btn, bg="pink")
                                        restart.place(x=290, y=230)

                                        show_report = Button(window, text="Report", font='verdana 15', bg="#00CDCD", command=self.display_report)
                                        show_report.place(x=390, y=230)

                                        end_btn = Button(window, text="End quiz", font='verdana 15', bg="plum", command=window.destroy)
                                        end_btn.place(x=490, y=230)


                                        window.mainloop()
        

                                              
                                
                                        
                                else:
                                       
                                        self.display_question()
                                        self.display_options()


                    
                        def buttons(self):
                                
                              
                                next_button = Button(gui, text="Next",command=self.next_btn,
                                width=10,bg="pink",fg="white",font=("ariel",16,"bold"))
                                
                                next_button.place(x=350,y=440)
                                
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                width=5,bg="plum", fg="white",font=("ariel",16," bold"))
                            
                                quit_button.place(x=800,y=50)

                


                        def display_options(self):
                                val=0
                                
                                self.opt_selected.set(0)
                             
                                for option in options[self.q_num]:
                                        self.opts[val]['text']=option
                                        val+=1


                        def display_question(self):
                                
                                q_num = Label(gui, text=question[self.q_num], width=80,
                                font=( 'ariel' ,15, 'bold' ),bg="azure", anchor= 'w' )
                                
                                q_num.place(x=70, y=120)


                        def revisionQuiz_title(self):
                                
                                title = Label(gui, text="Revision Quiz",
                                width=50, bg="#00CDCD",fg="white", font=("ariel", 23, "bold"))
                                
                                title.place(x=0, y=2)


                      
                        def radio_buttons(self):
                                
                                q_list = []
                        
                                y_pos = 170
                              
                                while len(q_list) < 4:
                                        
                                        radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
                                        value = len(q_list)+1,font = ("ariel",14), bg="azure")
                                        
                                        q_list.append(radio_btn)
                                        
                                        radio_btn.place(x = 100, y = y_pos)
                                    
                                        y_pos += 40
                                
                                return q_list

                gui = Tk()

                gui.geometry("900x550")

                gui.title("Revision Quiz")

                gui.config(background="azure")

                with open('easy.json') as f:
                        data = json.load(f)

                question =(data['question'])
                options = (data['options'])
                answer = (data[ 'answer'])

                quiz = Quiz()

                gui.mainloop()


        def medium():
                root.destroy()

                class Quiz:
    
                        def __init__(self):
                
                                self.q_num=0
                
                                self.revisionQuiz_title()
                
                                self.display_question()
                        
                                self.opt_selected=IntVar()
            
                                self.opts=self.radio_buttons()
                        
                                self.display_options()

                                self.feedback=Label(gui, pady=10, font=("ariel", 15, "bold"), bg="azure")
                                self.feedback.place(x=340, y=370)
                        
                                self.buttons()
                        
                                self.data_size=len(question)
                    
                                self.correct=0


                        def display_report(self):
                                
                                wrong_ans = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_ans}"
                                
                                score = int(self.correct / self.data_size * 100)
                                report = f"Score: {score}%"
                               
                                mb.showinfo("Report", f"{report}\n{correct}\n{wrong}")



                        def check_ans(self, q_num):
                                
                                if self.opt_selected.get() == answer[q_num]:
                                        return True

                     
                        def next_btn(self):
                                
                    
                                if self.check_ans(self.q_num):
                                        
                                        self.correct += 1
                                        self.feedback["fg"] = "springgreen"
                                        self.feedback["text"] = 'Correct answer! \U0001F44D'
                                        self.q_num += 1

                                else:
                                        self.feedback['fg'] = 'indianred'
                                        self.feedback['text'] = ('Wrong! \u274E \n'
                                                                 f'The correct answer is {answer[self.q_num]}')
                                        self.q_num += 1
                                                                 
                    
                                if self.q_num==self.data_size:
                                        
                                
                                        gui.destroy()

                                        def restart_btn():
                                
                                                window.destroy()
                                                level_tk()



                                        window = Tk()
                                        window.geometry("900x550")
                                        window.title("Revision Quiz")
                                        window.config(background="azure")

                                        choose_opt = Label(window, text="Please choose whether to restart the quiz or show the report and quit",
                                                           font='verdana 15 bold', bg="azure")
                                        choose_opt.place(x=70, y=100)

                                        restart = Button(window, text="Restart", font='verdana 15', command=restart_btn, bg="pink")
                                        restart.place(x=290, y=230)

                                        show_report = Button(window, text="Report", font='verdana 15', bg="#00CDCD", command=self.display_report)
                                        show_report.place(x=390, y=230)

                                        end_btn = Button(window, text="End quiz", font='verdana 15', bg="plum", command=window.destroy)
                                        end_btn.place(x=490, y=230)


                                        window.mainloop()
        

                                              
                                
                                
                                        
                                else:
                                       
                                        self.display_question()
                                        self.display_options()


                    
                        def buttons(self):
                                
                              
                                next_button = Button(gui, text="Next",command=self.next_btn,
                                width=10,bg="pink",fg="white",font=("ariel",16,"bold"))
                                
                                next_button.place(x=350,y=440)
                                
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                width=5,bg="plum", fg="white",font=("ariel",16," bold"))
                            
                                quit_button.place(x=800,y=50)

                


                        def display_options(self):
                                val=0
                                
                                self.opt_selected.set(0)
                             
                                for option in options[self.q_num]:
                                        self.opts[val]['text']=option
                                        val+=1


                        def display_question(self):
                                
                                q_num = Label(gui, text=question[self.q_num], width=80,
                                font=( 'ariel' ,15, 'bold' ),bg="azure", anchor= 'w' )
                                
                                q_num.place(x=70, y=120)


                        def revisionQuiz_title(self):
                                
                                title = Label(gui, text="Revision Quiz",
                                width=50, bg="#00CDCD",fg="white", font=("ariel", 23, "bold"))
                                
                                title.place(x=0, y=2)


                      
                        def radio_buttons(self):
                                
                                q_list = []
                        
                                y_pos = 170
                              
                                while len(q_list) < 4:
                                        
                                        radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
                                        value = len(q_list)+1,font = ("ariel",14), bg="azure")
                                        
                                        q_list.append(radio_btn)
                                        
                                        radio_btn.place(x = 100, y = y_pos)
                                    
                                        y_pos += 40
                                
                                return q_list

                gui = Tk()

                gui.geometry("900x550")

                gui.title("Revision Quiz")

                gui.config(background="azure")

                with open('medium.json') as f:
                        data = json.load(f)

                question =(data['question'])
                options = (data['options'])
                answer = (data[ 'answer'])

                quiz = Quiz()

                gui.mainloop()




        def hard():
                root.destroy()

                class Quiz:
    
                        def __init__(self):
                
                                self.q_num=0
                
                                self.revisionQuiz_title()
                
                                self.display_question()
                        
                                self.opt_selected=IntVar()
            
                                self.opts=self.radio_buttons()
                        
                                self.display_options()

                                self.feedback=Label(gui, pady=10, font=("ariel", 15, "bold"), bg="azure")
                                self.feedback.place(x=340, y=370)
                        
                                self.buttons()
                        
                                self.data_size=len(question)
                    
                                self.correct=0


                        def display_report(self):
                                
                                wrong_ans = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_ans}"
                                
                                score = int(self.correct / self.data_size * 100)
                                report = f"Score: {score}%"
                               
                                mb.showinfo("Report", f"{report}\n{correct}\n{wrong}")



                        def check_ans(self, q_num):
                                
                                if self.opt_selected.get() == answer[q_num]:
                                        return True

                     
                        def next_btn(self):
                                
                    
                                if self.check_ans(self.q_num):
                                        
                                        self.correct += 1
                                        self.feedback["fg"] = "springgreen"
                                        self.feedback["text"] = 'Correct answer! \U0001F44D'
                                        self.q_num += 1

                                else:
                                        self.feedback['fg'] = 'indianred'
                                        self.feedback['text'] = ('Wrong! \u274E \n'
                                                                 f'The correct answer is {answer[self.q_num]}')
                                        self.q_num += 1
                                                                 
                    
                                if self.q_num==self.data_size:
                                        
                                
                                        gui.destroy()

                                        def restart_btn():
                                
                                                window.destroy()
                                                level_tk()



                                        window = Tk()
                                        window.geometry("900x550")
                                        window.title("Revision Quiz")
                                        window.config(background="azure")

                                        choose_opt = Label(window, text="Please choose whether to restart the quiz or show the report and quit",
                                                           font='verdana 15 bold', bg="azure")
                                        choose_opt.place(x=70, y=100)

                                        restart = Button(window, text="Restart", font='verdana 15', command=restart_btn, bg="pink")
                                        restart.place(x=290, y=230)

                                        show_report = Button(window, text="Report", font='verdana 15', bg="#00CDCD", command=self.display_report)
                                        show_report.place(x=390, y=230)

                                        end_btn = Button(window, text="End quiz", font='verdana 15', bg="plum", command=window.destroy)
                                        end_btn.place(x=490, y=230)


                                        window.mainloop()
        

                                              
                                
                                
                                        
                                else:
                                       
                                        self.display_question()
                                        self.display_options()


                    
                        def buttons(self):
                                
                              
                                next_button = Button(gui, text="Next",command=self.next_btn,
                                width=10,bg="pink",fg="white",font=("ariel",16,"bold"))
                                
                                next_button.place(x=350,y=440)
                                
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                width=5,bg="plum", fg="white",font=("ariel",16," bold"))
                            
                                quit_button.place(x=800,y=50)
                

                


                        def display_options(self):
                                val=0
                                
                                self.opt_selected.set(0)
                             
                                for option in options[self.q_num]:
                                        self.opts[val]['text']=option
                                        val+=1


                        def display_question(self):
                                
                                q_num = Label(gui, text=question[self.q_num], width=80,
                                font=( 'ariel' ,15, 'bold' ),bg="azure", anchor= 'w' )
                                
                                q_num.place(x=70, y=120)


                        def revisionQuiz_title(self):
                                
                                title = Label(gui, text="Revision Quiz",
                                width=50, bg="#00CDCD",fg="white", font=("ariel", 23, "bold"))
                                
                                title.place(x=0, y=2)


                      
                        def radio_buttons(self):
                                
                                q_list = []
                        
                                y_pos = 170
                              
                                while len(q_list) < 4:
                                        
                                        radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
                                        value = len(q_list)+1,font = ("ariel",14), bg="azure")
                                        
                                        q_list.append(radio_btn)
                                        
                                        radio_btn.place(x = 100, y = y_pos)
                                    
                                        y_pos += 40
                                
                                return q_list

                gui = Tk()

                gui.geometry("900x550")

                gui.title("Revision Quiz")

                gui.config(background="azure")

                with open('hard.json') as f:
                        data = json.load(f)

                question =(data['question'])
                options = (data['options'])
                answer = (data[ 'answer'])

                quiz = Quiz()

                gui.mainloop()

                



        root = Tk()

        root.geometry("900x550")
        
        root.title("Revision Quiz")
    
        root.config(background="azure")
        

        level_lb = Label(root, text="Please choose a level", font='verdana 15 bold', bg="azure")
        level_lb.place(x=330, y= 100)

        easy_btn =Button(root, text = "Easy", font='verdana 15', command=easy, bg="yellow")
        easy_btn.place(x=290, y=230)

        medium_btn = Button(root, text="Medium", font='verdana 15', bg="orange", command=medium)
        medium_btn.place(x=390, y=230)

        hard_btn = Button(root, text="Hard", font='verdana 15', bg="red", command=hard)
        hard_btn.place(x=520, y=230)

        root.mainloop()





def signup():
	
	def action():
		if firstname.get()=="" or lastname.get()=="" or username.get()=="" or password.get()=="" or verify.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = signup_win)
		elif password.get() != verify.get():
			messagebox.showerror("Error" , "Password & Verify Password should be same" , parent = signup_win)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="logins")
				cur = con.cursor()
				cur.execute("select * from logins where username=%s",username.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = signup_win)
				else:
					cur.execute("insert into logins(firstname,lastname,username,password) values(%s,%s,%s,%s)",
						(
						firstname.get(),
						lastname.get(),
						username.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Sign up Successful!" , parent = signup_win)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = signup_win)

			
	def switch():
		signup_win.destroy()


	def clear():
		firstname.delete(0,END)
		lastname.delete(0,END)
		username.delete(0,END)
		password.delete(0,END)
		verify.delete(0,END)



	signup_win = Tk()
	signup_win.title("Signup")
	signup_win.geometry("900x550")
	signup_win.config(background="azure")

	heading = Label(signup_win , text = "Signup" , font = 'Verdana 20 bold', bg="azure")
	heading.place(x=400 , y=90)

	firstname = Label(signup_win, text= "First Name :" , font='Verdana 10 bold',  bg="azure")
	firstname.place(x=200,y=160)

	lastname = Label(signup_win, text= "Last Name :" , font='Verdana 10 bold',  bg="azure")
	lastname.place(x=200,y=200)

	username = Label(signup_win, text= "User Name :" , font='Verdana 10 bold',  bg="azure")
	username.place(x=200,y=240)
	
	password = Label(signup_win, text= "Password :" , font='Verdana 10 bold',  bg="azure")
	password.place(x=200,y=280)

	verify = Label(signup_win, text= "Verify Password:" , font='Verdana 10 bold',  bg="azure")
	verify.place(x=200,y=320)


	firstname = StringVar()
	lastname = StringVar()
	username = StringVar()
	password = StringVar()
	very_pass = StringVar()


	firstname = Entry(signup_win, width=40 , textvariable = firstname)
	firstname.place(x=340 , y=163)


	
	lastname = Entry(signup_win, width=40 , textvariable = lastname)
	lastname.place(x=340 , y=200)

	
	username = Entry(signup_win, width=40,textvariable = username)
	username.place(x=340 , y=240)

	
	password = Entry(signup_win, width=40, textvariable = password)
	password.place(x=340 , y=280)

	
	verify= Entry(signup_win, width=40 ,show="*" , textvariable = verify)
	verify.place(x=340 , y=320)

	signUp = Button(signup_win, text = "Signup" ,font='Verdana 12 bold', command = action,  bg="pink", fg="white")
	signUp.place(x=380, y=360)


	clear_button = Button(signup_win, text = "Clear" ,font='Verdana 12 bold' , command = clear,  bg="plum", fg="white")
	clear_button.place(x=480, y=360)


	switch_btn = Button(signup_win , text="Switch To Login" , font='verdana 14 bold', command = switch,  bg="#00CDCD", fg="white" )
	switch_btn.place(x=380 , y =440)


	signup_win.mainloop()



win = Tk()

win.title("Logins")

win.geometry("900x550")
win.config(background="azure")


heading = Label(win , text = "Login" , font = 'ariel 25 bold', bg="azure")
heading.place(x=400 , y=100)

user_name = Label(win, text= "User Name :" , font='ariel 15', bg="azure")
user_name.place(x=200,y=200)

password_lb = Label(win, text= "Password :" , font='ariel 15', bg="azure")
password_lb.place(x=200,y=240)


username = StringVar()
password = StringVar()
	
userenter = Entry(win, width=40, textvariable = username)
userenter.focus()
userenter.place(x=350 , y=203)

pw = Entry(win, width=40, show="*" ,textvariable = password)
pw.place(x=350 , y=240)


login_btn = Button(win, text = "Login" ,font='verdana 13 bold',command = login, bg="pink", fg="white")
login_btn.place(x=360, y=293)


clear_btn = Button(win, text = "Clear" ,font='verdana 13 bold', command = clear, bg="plum", fg="white")
clear_btn.place(x=460, y=293)


signup_btn = Button(win , text="Sign up an account" , font=' verdana 14 bold', command = signup, bg="#00CDCD", fg="white" )
signup_btn.place(x=350 , y =380)



win.mainloop()




        



