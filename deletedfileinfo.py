import os
import optparse
from winreg import *

def sid2user(sid):
    try:
        
        key = OpenKey(HKEY_LOCAL_MACHINE,
            " SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" 
            + '\\' + sid)
        (vlaue, type) = QueryValueEx(key, 'ProfileImagePath')
        user= value.split('\\')[-1]
        return user
    
    except:
        return sid

def returnDir():
    dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
        return None

def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files=os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print('\n[*] Listing Files For User: ' , user)
        for file in files:
            print('[+] Found Files: ' , file)

def main():
    recycleDir = returnDir()
    findRecycled(recycleDir)

if __name__ == '__main__':
    main()

