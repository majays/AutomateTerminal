



# from posixpath import dirname
# import subprocess 
# import os
# while (True):
#     ans = input("y/n => ")
#     if ans=='y':   
#         def func1(data):
#             if data == 'go back':
#                 os.chdir('..')
#                 subprocess.run('ls',shell=True)
#                 os.getcwd()
#             # elif data[20:21] not in alph:
#             #     os.chdir(data[20:])
#             #     subprocess.run('ls',shell=True)
#             #     os.getcwd()
#             else:  
#                 os.chdir(data[20:].capitalize())
#                 subprocess.run('ls',shell=True)
#                 os.getcwd()
            
#         data = input("give a input => ")
#        # alph=['A','B','C','D','E','F','G','H','I','J','K','L','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#         lis = ['change directory to desktop','change directory to downloads','change directory to documents','go back']
#         lis1 =['create a directory','create a file','show directory','show list directory','change permission for directory','change permission for file']

#         if data in lis:
#             func1(data)
#         elif data[:14] in lis1:
#             subprocess.run('ls',shell=True)
#         elif data[:19] in lis1:
#             subprocess.run('ls -la',shell=True)
#         elif data[:13] in lis1:
#             filename=data[14:].capitalize()+'.txt'
#             os.mknod(filename)
#             lis.append('change directory to '+filename)
#         elif data[:18] in lis1:
#             dirnames=data[19:].capitalize()
#             os.mkdir(dirnames)
#             lis.append('change directory to '+dirnames)
#         elif data[:31] in lis1:
#             dirnames=data[32:].capitalize()
#             os.chmod(dirnames,0o0777)
#         elif data[:26] in lis1:
#             filename=data[27:].capitalize()+'.txt'
#             os.chmod(filename,0o0777)
#         # os.getcwd()
#         # print(os.getcwd())
#         # subprocess.run('ls',shell=True)
#     else:
#         break
import speech_recognition as sr
r=sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print("sppek  profunction")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print('you said : {}'.format(text))
        except:
            print("no")
'''This is Terminal Function module which we have used for intrect with Operating System'''
import subprocess 
import os
import speech_recognition as sr




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

def func1(data):
    
    '''This function used for networking Commands'''

    if data == 'go back':
        os.chdir('..')
        subprocess.run('ls',shell=True)
        os.getcwd()
    
    elif data == 'what is my IP':
        subprocess.run('ifconfig',shell=True)
    
    elif data[:5] == 'route':
        subprocess.run(f'traceroute {data[6:]}',shell=True)
    
    elif data[:4]=='scan':
        subprocess.run(f'nmap {data[5:]}',shell=True)
    
    else:  
        os.chdir(data[20:].capitalize())
        subprocess.run('ls',shell=True)
        os.getcwd()


def remove_Dir_File(date):
    
    '''This function used for remove file and Directory '''
    
    if data[:11] in remove_dir_file:
        filename=data[12:].capitalize()+'.txt'
        subprocess.run(f'rm -r -v {filename}',shell=True)
        # os.remove(filename)
        filename=data[12:].capitalize()+'.txt'
        subprocess.run(f'rm -r -v {filename}',shell=True)
    
    else:
        folder=data[17:].capitalize()
        subprocess.run(f'rmdir -p -v {folder}',shell=True)
        # os.removedirs(folder)
        folder=data[17:].capitalize()
        subprocess.run(f'rmdir -p -v {folder}',shell=True)


def update_install(data):
    
    '''this function is used for install package'''

    if data[:15].lower() == 'install package':
        subprocess.run(f'sudo apt-get install {data[16:]}',shell=True)

    elif data[:9].lower()=='update me':
        subprocess.run(f'sudo apt-get update',shell=True) 
    
    else:
        subprocess.run(f'sudo apt-get upgrade',shell=True)

def pymodule(data):
    
    '''this function use for downloade pyhton module'''
    
    if data[:21] in python_module_install:
        subprocess.run(f'pip install {data[22:].lower()}',shell=True)


def diskS_diskU(data):
    
    '''this function is run for show how many space available in disk and how many space uses by disk block '''
    
    if data[:18] in disk_space_use :
        subprocess.run('df',shell=True)
    
    else:
        subprocess.run('du',shell=True)


def Date_cal(date):
    
    '''this function used for show us today date just tell show me a date'''
    
    if data in Date_calendar:
       subprocess.run('date',shell=True)


def terminal():
    while (True):
        r=sr.Recognizer() 
        
        with sr.Microphone() as source:
            print("speek")
            audio=r.listen(source)
            
            try:
            
                text=r.recognize_google(audio)
                print('you said : {}'.format(text))  
                global data
                data=text
            
                if data!='quit':   

                    if data[:19] == 'change directory to' or data=='go back' or data[:5]=="route" or data == 'what is my IP' or data[:4]=='scan':
                        func1(data)
                    
                    elif data[:14] in show_dir:
                        subprocess.run('ls',shell=True)
                    
                    elif data[:19] in show_dir:
                        subprocess.run('ls -la',shell=True)
                    
                    elif data[:13] in create_dir_file:
                        filename=data[14:].capitalize()+'.txt'
                        os.mknod(filename)
                        #lis.append('change directory to '+filename)
                    
                    elif data[:18] in create_dir_file:
                        dirnames=data[19:].capitalize()
                        os.mkdir(dirnames)
                        #lis.append('change directory to '+dirnames)
                    
                    elif data[:31] in change_per:
                        dirnames=data[32:].capitalize()
                        os.chmod(dirnames,0o0777)
                    
                    elif data[:26] in change_per:
                        filename=data[27:].capitalize()+'.txt'
                        os.chmod(filename,0o0777)
                    
                    elif data[:18] in disk_space_use or data[:17] in disk_space_use:
                        diskS_diskU(data)
                    
                    elif data in Date_calendar:
                        Date_cal(data)
                    
                    elif data[:21] in python_module_install:
                        pymodule(data)
                    
                    elif data[:11] in remove_dir_file or data[:16] in remove_dir_file:
                        remove_Dir_File(data)
                
                    elif data[:15].lower() == 'install package' or data[:9].lower() in ['update me'] or data[:10].lower() in ['upgrade me']:
                        update_install(data)

                else:
                    break
            
            except:
                print("no")