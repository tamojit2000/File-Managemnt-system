from tkinter import Tk,Entry,Label,Button
from tkinter.filedialog import askdirectory
from os import listdir,mkdir
from shutil import move

def extension(x):
    z=''
    for a in range(len(x)-1,-1,-1):
        if x[a]=='.': break
        z+=x[a]
    else:
        return ''
    return (z+'.')[::-1]

    

def Move(a,FOLDER):
    global folder
    
    list_files=listdir(folder)
    if FOLDER not in list_files:
        mkdir(folder+'//'+FOLDER)
    move(folder+'//'+a,folder+'//'+FOLDER)



def organize(event=None):
    try:
        x=L.get()
        #print x
        
        AUDIO={'.aif','.cda','.mid','.mp3','.midi','.mpa','.ogg','.wav','.wma','.wpl'}
        COMPRESSED={'.7z','.arj','.deb','.pkg','.rar','.rpm','.tar','.gz','.z','.zip'}
        DISC={'.bin','.dmg','.iso','.toast','.vcd'}
        DATABASE={'.db','.csv','.dat','.dbf','.log','.mdb','.sav','.sql','.tar','.xml'}
        EXECUTABLE={'.apk','.bat','.bin','.cgi','.com','.exe','.gadget','.jar','.wsf','.msi'}
        VIDEO={'.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'}
        WORD_PDF={'.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wks','.wps','.wpd'}
        FONT={'.fnt','.fon','.otf','.ttf'}
        IMAGE={'.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff','.icns'}
        INTERNET={'.asp','.aspx','.cer','.cfm','.css','.html','.htm','.js','.jsp','.part','.php','.rss','.xhtml'}
        PRESENTATION={'.key','.odp','.pps','.ppt','.pptx'}
        PROGRAMMING={'.pl','.py','.pyw','.pyc','.c','.cpp','.class','.cs','.h','.java','.sh','.swift','.vb'}
        SHEET={'.ods','.xlr','.xls','.xlsx'}
        SYSTEM={'.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.ini','.lnk','.sys','.tmp'}

        l=listdir(x)

        #print l    
        for a in l:
            ex=extension(a)
            #print ex
            if ex in AUDIO: Move(a,'AUDIO')
            elif ex in COMPRESSED: Move(a,'COMPRESSED')
            elif ex in DISC: Move(a,'DISC')
            elif ex in DATABASE: Move(a,'DATABASE')
            elif ex in EXECUTABLE: Move(a,'EXECUTABLE')
            elif ex in VIDEO: Move(a,'VIDEO')
            elif ex in WORD_PDF: Move(a,'PDF_TEXT_WORD')
            elif ex in FONT: Move(a,'FONT')
            elif ex in IMAGE: Move(a,'IMAGE')
            elif ex in INTERNET: Move(a,'INTERNET')
            elif ex in PRESENTATION: Move(a,'PRESENTATION')
            elif ex in PROGRAMMING: Move(a,'PROGRAMMING')
            elif ex in SHEET: Move(a,'SHEET')
            elif ex in SYSTEM: Move(a,'SYSTEM')
            elif ex=='': pass
            else: Move(a,'OTHERS')
            

        ans_label.config(text='Done.')
    except:
        ans_label.config(text='Error.')

def reset(event=None):
    global folder
    L.delete(0,'end')
    ans_label.config(text='')
    folder=''

def browse():
    global folder
    folder=askdirectory()
    L.insert(0,folder)
   
def f():
    pass

def Exit(event=None):
    root.destroy()

root=Tk()
root.geometry('700x150+300+200')
root.config(background='navyblue')
root.overrideredirect(True)


Label(root,text='File Management System',bg='navyblue',fg='white',font=('Algerian')).place(x=220,y=10)


L=Entry(root,width=113)
L.place(x=10,y=50)


Label(root,text='Folder Path:',bg='navyblue',fg='white').place(x=10,y=85)
Button(root,text='Organize',bg='navyblue',fg='white',command=organize,relief='groove').place(x=320,y=85)
Button(root,text='Browse',bg='navyblue',fg='white',command=browse,relief='groove').place(x=640,y=85)


ans_label=Label(root,text='',bg='navyblue',fg='white')
ans_label.place(x=10,y=10)

Label(root,text='@ TD',bg='navyblue',fg='white').place(x=10,y=120)
Label(root,text='v 4.0',bg='navyblue',fg='white').place(x=90,y=120)
Label(root,text='Standard keyboard key included.',bg='navyblue',fg='white').place(x=250,y=120)
Button(root,text='Exit',bg='navyblue',fg='white',command=Exit,relief='groove').place(x=660,y=120)
Button(root,text='Reset',bg='navyblue',fg='white',command=reset,relief='groove').place(x=610,y=120)


root.bind('<Return>',organize)  # press enter to automatiocally clivck balance button
root.bind('<Escape>',Exit)      # to destroy root window 
root.bind('<F5>',reset)         # to reset Entry label and others

folder=''

root.mainloop()

