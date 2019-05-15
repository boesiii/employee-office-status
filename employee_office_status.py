
import Tkinter
import tkMessageBox
from Tkinter import *
import time
from os import listdir
from os.path import isfile, join
import datetime
import fileinput
import sys
import platform
import os
from os import startfile
from shutil import copyfile



def emp_info(button_number, name):
    
    with open(emp_info_path + 'emp_info.txt', 'r') as f:
        lines = f.readlines()
        match = 'no'
        for line in lines:
            line = line.replace('\n','')
            line = line.split(',')
            print (line[0])
            if line[0] == str(comp_data[button_number][0]).lower():
                match = 'yes'
                tkMessageBox.showinfo( 'Employee Info', str(comp_data[button_number][0]) + '\n' + 'Ext: ' + line[1] + '\n' + 'Cell #: ' + line[2])
            
                
        if match == 'no':
            tkMessageBox.showinfo( 'Employee Info', 'Sorry I dont have information for that person')
            
                
    

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%I:%M:%S %p")
    
    # Update the timeText Label box with the current time
    timeText.configure(text=current)
    # Call the update_timeText() function after 1 second
    top.after(1000, update_timeText)
    
def dailyHistory():
    tkMessageBox.showinfo( "Dailys History", "This button will bring up a \n text file containing the daily history ")
    
    
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            #line = line.replace(searchExp,replaceExp)
            line = replaceExp
        sys.stdout.write(line)
        
def future():
    
    future_window = Toplevel(top)
    future_window.geometry('500x500')
    future_window.focus_set()
    future_window.grab_set()
    future_date = Entry(future_window, width=12)
    future_date.grid(row=3,column=1, padx=(5,5), pady=(30,30))
    future_desc = Entry(future_window, width=12)
    future_desc.grid(row=3,column=2, padx=(5,5),pady=(30,30))
    
    
    #create close button
    cf_button = Button (future_window, text = "Close", command = future_window.destroy,bg='dark grey')
    # cf_button.grid(row=r,column=2, pady=(3,3))
    cf_button.grid(row=4,column=2)
    future_window.mainloop()
    
#def close_future_window(): 
#    future_window.destroy()

    
        
def write_history (text,button_number):
    with open(history_path + str(comp_data[button_number][0]) + ".txt", "a") as f:
        f.writelines(text + '\n')
    
    with open(init_path + '/' + str(comp_data[button_number][0]) + ".txt", "w") as f:
        f.writelines(text)
        
def inOffice(button_number):
    rsp_act_time_in = ent_act_time_in[button_number].get()
    if rsp_act_time_in is '':
        rsp_act_time_in = datetime.datetime.now().strftime("%I:%M %p")
        
    
    inbutton[button_number].configure(bg = "green")
    outbutton[button_number].configure(bg = "light grey")
    ent_dest[button_number].delete(0, 'end')
    ent_proj_num[button_number].delete(0, 'end')
    ent_time_out[button_number].delete(0, 'end')
    ent_exp_time_in[button_number].delete(0, 'end')
    ent_act_time_in[button_number].delete(0, 'end')
    ent_act_time_in[button_number].insert(0, rsp_act_time_in)
    #tkMessageBox.showinfo( "In Button", "This button will turn green when pressed" + "\n" + "and will grab the value from the arrival time")
    write_line = str(datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')) + '\t' + 'in' + '\t' + rsp_act_time_in + '\n'
    #print comp_data[button_number][0]
    write_history (write_line,button_number)
        
def outOffice(button_number):
    outbutton[button_number].configure(bg = "orange")
    inbutton[button_number].configure(bg = "light grey")
    rsp_dest = ent_dest[button_number].get()
    rsp_proj_num = ent_proj_num[button_number].get()
    rsp_time_out = ent_time_out[button_number].get()
    ent_time_out[button_number].delete(0, 'end')
    if rsp_time_out is '':
        rsp_time_out = datetime.datetime.now().strftime("%I:%M %p")
    ent_time_out[button_number].insert(0, rsp_time_out)
    rsp_exp_time_in = ent_exp_time_in[button_number].get()
    ent_act_time_in[button_number].delete(0, 'end')
    #tkMessageBox.showinfo( "Out of Office", "This button will process the values and send them to history" + "\n" + rsp_dest + " -- " + rsp_time_out)
    write_line = str(datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')) + '\t' + 'out' + '\t' + rsp_dest + '\t' + rsp_proj_num + '\t' + rsp_time_out + '\t' + rsp_exp_time_in +"\n"
    #print comp_data[button_number][0]
    write_history (write_line,button_number)
        
       
def getHistory(button_number):
    #tkMessageBox.showinfo( "Get History", "A text file for individual history will be displayed")
    dhist_file_path = history_path + str(comp_data[button_number][0]) + ".txt"
    temp_file_path = os.getenv('LOCALAPPDATA') + '\\temp\\siso'+ str(comp_data[button_number][0]) + '.txt'
    #print temp_file_path
    #os.getenv('APPDATA')
    copyfile(dhist_file_path, temp_file_path)
    os.startfile(temp_file_path)
    
def close_window(): 
    top.destroy()
    
def restart_program():
    #python = sys.executable
    python = 'c:/python27/pythonw.exe'
    os.execl(python, python, * sys.argv)
    

    
def match_computer_name (pc):
    #print pc
    for entry in pc_match_list:
        if entry['pc_name'] == pc:
            #print 'Match Found: ' + entry['pc_name']
            nm = entry['fname']
            return nm


# this function was used to place the window on a certain screen            
def set_window_geom (name):
    sw,sh = top.winfo_screenwidth(),top.winfo_screenheight()
    w,h = 1100,900
    #a,b = (sw-w)/2,(sh-h)/2
    second_monitors = ['person1','person2']
    if computer_name in second_monitors:
        a,b = sw,0
    elif computer_name == 'person1':
        a,b = -1200,0
    else:
        a,b = 0,0
    
    return w,h,a,b
    
    


#initialize variables                

headings = ["Name", "In", "Out", "Destination / Reason", "Project #", "Time Out", 
            "Expected Time In", "Actual Time In"]

pc_match_list = [ {'fname' : 'first-name', 'pc_name' : 'computer-name'},
                {'fname' : 'first-name2', 'pc_name' : 'computer-name'},
                                
                ]


r=0
c=0
comp_data = []

#get computer name
computer_name = platform.node()

#setup main window
top = Tkinter.Tk()
top.geometry('%sx%s+%s+%s'%(set_window_geom(computer_name)))
top.wm_title("Sign In Sign Out")

#folder locations
history_path = "emp\\"
init_path = 'init'
emp_info_path = 'emp\\'

#get list of files
files = [f for f in listdir(init_path) if isfile(join(init_path, f))]

#process data in each employee file
for file in files:
    emp_data = []
    #print file
    emp_name = file.replace('.txt', '')
    emp_data.append(emp_name)
    #print emp_name
    #file = open(init_path + "/" + file , 'r')
    with open(init_path + "/" + file , 'r') as f:
        line = f.readline()
        line = line.replace('\n','')
    #print line
    
    line = line.split('\t')
    
    emp_data.extend(line)
    #find computer name
    computer_real_name = match_computer_name(computer_name)
    #print 'computer real name -- ' + str(computer_real_name)
    if computer_real_name == emp_name:
        comp_data.insert(0,emp_data)
    else:
        comp_data.append(emp_data)

#create label for instructions 
label_inst = Label(top, text="Fill in boxes, then click In or Out Buttons, then Close")
label_inst.grid (row=r, column=0, columnspan=3)

#create label for time and update 
label_time = Label(top, text="Time:")
label_time.grid (row=r,column=3)
timeText = Label(top, text="")
timeText.grid(row=r,column=4)
update_timeText()


#create future button
# future_button = Button (top, text = "Future", command = future)
# future_button.grid(row=r,column=5, pady=(3,3))

#create close button
close_button = Button (top, text = "Close", command = close_window,bg='dark grey')
close_button.grid(row=r,column=6, pady=(3,3))

restart_button = Button (top, text = "Refresh", command = restart_program, bg='yellow')
restart_button.grid(row=r,column=7, pady=(3,3))

r = r + 1

#setup headings
for heading in headings:
    h = Label(top, text=heading)
    h.grid(row=r,column=c, padx=(5,5), pady=(1,1))
    c = c + 1

#setup buttons
inbutton = {}
outbutton = {}
ent_dest = {}
ent_time_out = {}
ent_exp_time_in = {}
ent_act_time_in = {}
ent_proj_num = {}
a = {}

r = r + 1
for i in range(len(comp_data)):
    emp = comp_data[i][0]
    resp_io = comp_data[i][2]
    
    #create emp name label
    #a[i] = Label(top, text=emp, width=13, anchor='w')
    a[i] = Button(top, pady= 0, width=13, text=emp, anchor='w', command=lambda i=i: emp_info(i,emp),bg="light grey")
    a[i].grid(row=r,column=0, padx=(5,5), pady=(1,1))
    
    #create in button
    if resp_io == "in":
        inbutton[i] = Button(top, pady= 0, width=4, text="In", command=lambda i=i: inOffice(i),bg="green")
        inbutton[i].grid(row=r,column=1, padx=(5,5), pady=(1,1))
    else:
        inbutton[i] = Button(top, width=4, text="In", command=lambda i=i: inOffice(i),bg="light grey")
        inbutton[i].grid(row=r,column=1, padx=(5,5), pady=(1,1))
    
    
    #create out button
    if resp_io == "out":
        outbutton[i] = Button(top, width=4, text="Out", command=lambda i=i: outOffice(i),bg="orange")
        outbutton[i].grid(row=r,column=2, padx=(5,5), pady=(1,1))
        
        #create destination entry
        ent_dest[i] = Entry(top, width=60)
        #ent_dest[i] = Text(top, height=3, width=20)
        ent_dest[i].grid(row=r,column=3, padx=(5,5), pady=(1,1))
        if len(comp_data[i]) > 3:
            ent_dest[i].insert(0, comp_data[i][3])
        
        #create project number entry
        ent_proj_num[i] = Entry(top,width=12)
        ent_proj_num[i].grid(row=r,column=4, padx=(5,5), pady=(1,1))
        #print comp_data[i]
        #print len(comp_data[i])
        if len(comp_data[i]) > 4:
            ent_proj_num[i].insert(0, comp_data[i][4])
        
        #create time out entry
        ent_time_out[i] = Entry(top, width=12)
        ent_time_out[i].grid(row=r,column=5, padx=(5,5), pady=(1,1))
        if len(comp_data[i]) > 5:
            ent_time_out[i].insert(0, comp_data[i][5])
                
        #create expected time in
        ent_exp_time_in[i] = Entry(top, width=12)
        ent_exp_time_in[i].grid(row=r,column=6, padx=(5,5), pady=(1,1))
        if len(comp_data[i]) > 6:
            ent_exp_time_in[i].insert(0, comp_data[i][6])
        
    else:
        outbutton[i] = Button(top, width= 4,text="Out", command=lambda i=i: outOffice(i),bg="light grey")
        outbutton[i].grid(row=r,column=2, padx=(5,5), pady=(1,1))
        
        #where entry box
        ent_dest[i] = Entry(top, width=60)
        #ent_dest[i] = Text(top, height=3, width=20)
        ent_dest[i].grid(row=r,column=3, padx=(5,5), pady=(1,1))
        
        #project number entry
        ent_proj_num[i] = Entry(top, width=12)
        ent_proj_num[i].grid(row=r,column=4, padx=(5,5), pady=(1,1))
        
        #time out entry
        ent_time_out[i] = Entry(top, width=12)
        ent_time_out[i].grid(row=r,column=5, padx=(5,5), pady=(1,1))
        
        #expected time in
        ent_exp_time_in[i] = Entry(top, width=12)
        ent_exp_time_in[i].grid(row=r,column=6, padx=(5,5), pady=(1,1))
        
    
    #axpected time in
    ent_act_time_in[i] = Entry(top, width=12)
    ent_act_time_in[i].grid(row=r,column=7, padx=(5,5), pady=(1,1))
    
    if resp_io == "in":
        if len(comp_data[i]) > 3:
            ent_act_time_in[i].insert(0, comp_data[i][3])
        
    #history button
    f = Button(top, text ="History", command=lambda i=i: getHistory(i))
    f.grid(row=r,column=8, padx=(5,5), pady=(1,1))
    
    r = r + 1
    if i == 0:
        separator = Frame(top, height=2, width=1000, bd=5, bg='dark grey')
        separator.grid(row=r, column=0, columnspan=9, pady=(10,10))
        r = r + 1
    #if i == 0:
    #    separator = Frame(top, height=2, bd=5, bg='red')
    #    separator.grid(row=r, column=0, columnspan=7)
    #    print separator
    
#scrollbar = Scrollbar(top)
#scrollbar.pack(side=RIGHT, fill=Y)
#scrollbar.config()

top.mainloop()
