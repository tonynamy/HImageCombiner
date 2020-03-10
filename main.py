import sys
import re
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

importFolder = 'testimg'
exportFolder = 'export'
filename_regex = r'(?P<filenum>\d+)-(?P<imagenum>\d+)'

matchFiles = dict()

def setVariable() :

  global importFolder, exportFolder, filename_regex

  print('enter input folder : ', end='')
  importFolder = str(input())

  print('enter output folder : ', end='')
  exportFolder = str(input())
  
  print('enter filename regex : ', end='')
  filename_regex = r''+str(input())

def findMatchingFiles() :

  global importFolder, exportFolder, filename_regex, matchFiles

  print('start findingMatchingFiles')

  files = [f for f in listdir(importFolder) if isfile(join(importFolder, f))]

  for file in files :
    
    regexp = re.compile(filename_regex)
    re_match = regexp.match(file)

    if(re_match is None) : continue

    filenum = re_match.group('filenum')
    imagenum = re_match.group('imagenum')

    if not filenum in matchFiles :
      matchFiles[filenum] = dict()

    matchFiles[filenum][imagenum] = file

    print(str(filenum) + '/' + str(imagenum) + ' found')

  print('end findingMatchingFiles')

def sortMatchingFiles() :

  global importFolder, exportFolder, filename_regex, matchFiles

  print('start sortMatchingFiles')

  tempDict = {k: v for k, v in sorted(matchFiles.items(), key=lambda item: int(item[0]))}

  for fileNum, imageDict in tempDict.items() :
    tempDict[fileNum] = {k: v for k, v in sorted(imageDict.items(), key=lambda item: int(item[0]))}

  print('end sortMatchingFiles')

def combineImages() :

  global importFolder, exportFolder, filename_regex, matchFiles

  print('start combineImages')

  Path(exportFolder).mkdir(parents=True, exist_ok=True)

  for fileNum, imageDict in matchFiles.items() :

    print('processing '+str(fileNum)+'...')

    images = [Image.open( os.path.join(importFolder, x) ) for x in list(imageDict.values()) ]
    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)
    total_height = sum(heights)

    new_im = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    
    for im in images:
      
      new_im.paste(im, (0, y_offset))
      y_offset += im.size[1]
      
    new_im.save(os.path.join(exportFolder, str(fileNum)+'.png'))

  print('end combineImages')

def main() :

  print('start program')

  setVariable()  
  findMatchingFiles()
  sortMatchingFiles()
  combineImages()

  print('end program')

main()
