import os
import shutil
import time
from win10toast import ToastNotifier

def Notify(status,txt):
    toaster=ToastNotifier()
    toaster.show_toast(status,txt,
                       icon_path='icon.ico',
                       duration=10,
                       threaded=True)
    while toaster.notification_active(): time.sleep(0.1)

def extension(x):
    return os.path.splitext(x)[1]
    

def Move(file,FOLDER):
    try:
        os.mkdir(FOLDER)
    except:
        pass
    shutil.move(file,FOLDER+'/'+file)        

def Organize(path):
    try:
        
        cur_dir=os.getcwd()
        os.chdir(path)
        
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

        file_list=os.listdir(path)

        #print(file_list)
        
        for file in file_list:
            #print(a)
            ex=extension(file)
            #print (ex)
            if ex in AUDIO: Move(file,'AUDIO')
            elif ex in COMPRESSED: Move(file,'COMPRESSED')
            elif ex in DISC: Move(file,'DISC')
            elif ex in DATABASE: Move(file,'DATABASE')
            elif ex in EXECUTABLE: Move(file,'EXECUTABLE')
            elif ex in VIDEO: Move(file,'VIDEO')
            elif ex in WORD_PDF: Move(file,'PDF_TEXT_WORD')
            elif ex in FONT: Move(file,'FONT')
            elif ex in IMAGE: Move(file,'IMAGE')
            elif ex in INTERNET: Move(file,'INTERNET')
            elif ex in PRESENTATION: Move(file,'PRESENTATION')
            elif ex in PROGRAMMING: Move(file,'PROGRAMMING')
            elif ex in SHEET: Move(file,'SHEET')
            elif ex in SYSTEM: Move(file,'SYSTEM')
            elif ex=='': pass
            else: Move(file,'OTHERS')
            
        os.chdir(cur_dir)   
        #print('Done')
        Notify('Successful','Folder organized')

    except Exception as e:
        os.chdir(cur_dir)
        Notify('Error',str(e))
        


