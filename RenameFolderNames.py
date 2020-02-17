# Author: Amin Yassin

# When False, we get an error
# os.rename(temp, root)
# FileNotFoundError: [WinError 3] The system cannot find the path specified:
# '.\\TvåX\\24 - Copy (3)\\Q71-48ite tr71-48e' -> '.\\TvåX\\24 - CP (3)\\Q71-48ite tr71-48e'

# If true, the function iterates through the folders in the top level

import os
import copy
import csv
import time
import logging

keywords = {'X' : '0', 'Copy' : 'Männi', '-' : '##', 'log' : 'old-log', 'Lall' : 'PUB'}
#keywords = {'0' : 'X', 'Männi' : 'Copy', '##' : ' - ', 'pub' : 'Lall', 'log' : 'old log'}


def renamefolders():
    
    starttime = time.time()

    # Set logging configurations:
    logging.basicConfig(filename='logfile.log', format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

    logging.info(f'==============Program started!==============')
    logging.info(f'Starting directory: {os.getcwd()}\n')
    #logging.critical('Test Critical')
    #logging.debug('Test Debug')
    
    # Some help variables:
    temproot = '' # To save root folder name
    oldfoldername = '' # To save name of folder to be changed
    tempname = '' # Help variable for oldfoldername
    
    """
    # Add the commented part below to the final program: 
    keywords = {}
    with open("TestCSV.csv") as csv_file:
        data = csv.reader(csv_file, delimiter=';')

        for row in data:
            keywords[row[0]] = row[1]
    """
    
    # A counter to skip the first root:
    # A counter for how many folders have been iterated through
    c = 0
    # 1:st for-loop. Each iteration gets root name, directory(s) in root, and filenames:
    try:
        for root, dirs, files in os.walk('.', False):
            logging.info(f'Initial Root: {root}\n')
            #if (c != 0): #No need to skip if os.walk is False:
            if(root != '.'):

                # Copy root name to a temp variable:
                temproot = copy.deepcopy(root)

                # Current folder's name:
                oldfoldername = root.split('\\')[-1]
                logging.info(f'Old Folder Name: {oldfoldername}\n')
                tempname = copy.deepcopy(oldfoldername)

                
                # Check if directory contains keywords:
                for i in keywords:
                    #if the keyword i is in root name, replace it. Can be more than 1, hence, the for-loop:
                    oldfoldername = oldfoldername.replace(i, keywords[i])

                logging.info(f'New Folder Name: {oldfoldername}\n')
            
                root = root.replace(tempname, oldfoldername)
                
                #rename the folder with the new name specified in root
                os.rename(temproot, root)
                #print('Old directory', root, 'New directory', temp)
                logging.info(f'New root: {root}\n')
                
            else:
                logging.info(f'Program finished!')
                break
            c += 1
            
    except:
        logging.critical('Something went wrong and for-loop has broken!', exc_info=True)
        logging.info(f'Execution time {time.time() - starttime} [sec]')
        logging.info(f'Number of iterations: {c}')
        
    else:
        logging.info(f'Program executed successfully!')
        logging.info(f'Execution time {time.time() - starttime} [sec]')
        logging.info(f'Number of iterations: {c}')
        
