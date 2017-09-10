'''
README

Place this file into the same directory as the folder who's content you want to rename.
Call this file in the terminal with the following arguments: python renamefiles.py

Enter the folder name of the folder you want to rename the contents of.

This pattern, [S]\d{2}[E]\d{2}, searches for the season and episode numbers in the name of the file and will remove
all other bloatware.

Example:

Original = Game.of.Thrones.S07E05.720p.WEB.h264-TBS[rarbg]
What we want = S07E05


'''


import os
import re

splitter = '\n################################################################\n'

pattern = "[sS]\d{2}[eE]\d{2}"
folderPath = raw_input("Please enter the path of the folder which contains the files you want to rename: ")

def renameFiles(rename=False):
   
   print splitter
   
   if (rename):
      print 'We will rename them now.'
   else:
      print 'Please check the proposed changes.'   
      
   print splitter
      
   for file in os.listdir(folderPath):
      print "\n" + "Old filename: " + file
      
      # File format section
      fileSplit = str.split(file, '.')
      fileFormat = fileSplit[-1]
      
      # Reg expression section to find the season and episode.
      match = re.findall(pattern, file)
      if match:
         newFilename = match[0] + '.' + fileFormat
         print "New filename: " + newFilename
         
         old = os.path.join(folderPath, file)
         new =  os.path.join(folderPath, newFilename)
         
         if (rename):
            os.rename(old, new)

            
            
def getUserInput():
   agree = raw_input('\nDo you want to rename all the files in this folder? (y/n)  ')
   if agree == 'y':
      renameFiles(True)
   elif agree == 'n':
      print '\nNo changes made.\n'
   else:
      print "\nType 'y' for yes or 'n' for no"
      getUserInput()

            
renameFiles()
getUserInput()