'''This is Terminal Function module which we have used for intrect with Operating System'''
import subprocess 
import os
import speech_recognition as sr
import speak as sp

'''this is list of command which we have followed'''


change_dir= ['change directory to desktop','change directory to downloads','change directory to documents','go back']
create_dir_file=['create a directory','create a file','change permission for directory']
show_dir=['show directory','show list directory']
change_per=['change permission for file']
disk_space_use=['show me free space','show me use space']
Date_calendar=['what is date today','show calendar']
python_module_install=["install Python module"]
remove_dir_file=["remove file","remove directory"]


''' This is Diffrent Different Function which we have been used'''

def func1(command_data):
    
    '''This function used for networking Commands'''

    if command_data == 'go back':
        os.chdir('..')
        subprocess.run('ls',shell=True)
        os.getcwd()
    
    elif command_data == 'what is my IP':
        subprocess.run('ifconfig',shell=True)
    
    elif command_data[:5] == 'route':
        subprocess.run(f'traceroute {command_data[6:]}',shell=True)
    
    elif command_data[:4]=='scan':
        subprocess.run(f'nmap {command_data[5:]}',shell=True)
    
    else:  
        os.chdir(command_data[20:].capitalize())
        subprocess.run('ls',shell=True)
        os.getcwd()


def remove_Dir_File(date):
    
    '''This function used for remove file and Directory '''
    
    if command_data[:11] in remove_dir_file:
        filename=command_data[12:].capitalize()+'.txt'
        subprocess.run(f'rm -r -v {filename}',shell=True)
        # os.remove(filename)
        filename=command_data[12:].capitalize()+'.txt'
        subprocess.run(f'rm -r -v {filename}',shell=True)
    
    else:
        folder=command_data[17:].capitalize()
        subprocess.run(f'rmdir -p -v {folder}',shell=True)
        # os.removedirs(folder)
        folder=command_data[17:].capitalize()
        subprocess.run(f'rmdir -p -v {folder}',shell=True)


def update_install(command_data):
    
    '''this function is used for install package'''

    if command_data[:15].lower() == 'install package':
        subprocess.run(f'sudo apt-get install {command_data[16:]}',shell=True)

    elif command_data[:9].lower()=='update me':
        subprocess.run(f'sudo apt-get update',shell=True) 
    
    else:
        subprocess.run(f'sudo apt-get upgrade',shell=True)

def pymodule(command_data):
    
    '''this function use for downloade pyhton module'''
    
    if command_data[:21] in python_module_install:
        subprocess.run(f'pip install {command_data[22:].lower()}',shell=True)


def diskS_diskU(command_data):
    
    '''this function is run for show how many space available in disk and how many space uses by disk block '''
    
    if command_data[:18] in disk_space_use :
        subprocess.run('df',shell=True)
    
    else:
        subprocess.run('du',shell=True)


def Date_cal(date):
    
    '''this function used for show us today date just tell show me a date'''
    
    if command_data in Date_calendar:
       subprocess.run('date',shell=True)

def command_list():
    print('''
    1) 'change directory to <directoryName>
	

    2) 'go back' <-- it is used to one step back to the directory 


    3) 'create a directory <dirname>',
    4) 'create a file <filename>',
    5) 'change permission for directory <dirname>'
    6) 'change permission for file <filename>'


    6) 'show directory', --> this is a "ls " commands
    7) 'show list directory'


    8) 'show me free space',df
    9) 'show me use space' ,du commands

    10) "install Python module <moduleName>"
 
    11) "What is my ip"
    12) "rout <(www.google.com)>"


    13) "scan <(www.facebook.com)>"


    14) "remove file <filename>",
    15)"remove directory <directoryname>"

    16)"install package <packagename>"
    17)"update me"
    18)"upgrade me"

    19)what is date today


    ''')
def terminal():
    while (True):
        r=sr.Recognizer() 
        
        with sr.Microphone() as source:
            sp.alexis("speek the command")
            print("if you forgot the command please speek <show me a coomand list>")
            audio=r.listen(source)
        
            try:
            
                command_=r.recognize_google(audio)
                print('you said : {}'.format(command_))  
                sp.alexis(command_)
                global command_data
                command_data=command_
            
                if command_data!='quit':   

                    if command_data[:19] == 'change directory to' or command_data=='go back' or command_data[:5]=="route" or command_data == 'what is my IP' or command_data[:4]=='scan':
                        func1(command_data)
                    
                    elif command_data.lower()=='show me a command list':
                        command_list()
                        
                    elif command_data[:14] in show_dir:
                        subprocess.run('ls',shell=True)
                    
                    elif command_data[:19] in show_dir:
                        subprocess.run('ls -la',shell=True)
                    
                    elif command_data[:13] in create_dir_file:
                        filename=command_data[14:].capitalize()+'.txt'
                        os.mknod(filename)
                        #lis.append('change directory to '+filename)
                    
                    elif command_data[:18] in create_dir_file:
                        dirnames=command_data[19:].capitalize()
                        os.mkdir(dirnames)
                        #lis.append('change directory to '+dirnames)
                    
                    elif command_data[:31] in change_per:
                        dirnames=command_data[32:].capitalize()
                        os.chmod(dirnames,0o0777)
                    
                    elif command_data[:26] in change_per:
                        filename=command_data[27:].capitalize()+'.txt'
                        os.chmod(filename,0o0777)
                    
                    elif command_data[:18] in disk_space_use or command_data[:17] in disk_space_use:
                        diskS_diskU(command_data)
                    
                    elif command_data in Date_calendar:
                        Date_cal(command_data)
                    
                    elif command_data[:21] in python_module_install:
                        pymodule(command_data)
                    
                    elif command_data[:11] in remove_dir_file or command_data[:16] in remove_dir_file:
                        remove_Dir_File(command_data)
                
                    elif command_data[:15].lower() == 'install package' or command_data[:9].lower() in ['update me'] or command_data[:10].lower() in ['upgrade me']:
                        update_install(command_data)

                else:
                    break
            
            except:
                print("no")