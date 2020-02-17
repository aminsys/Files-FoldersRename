# Author: Amin Y

import os
import copy
import csv
import time
import logging

# Test keywords:
keywords = {'i' : '1', 'p' : 'P', '-' : '#', 'log' : 'Luigi', 'Lall' : 'PUB'}

def renamefiles():

    starttime = time.time()

    # Set logging configuration:
    logging.basicConfig(filename='..\logfile-filename.log', format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

    logging.info(f'==============Program started!==============')
    logging.info(f'Starting directory: {os.getcwd()}\n')

    
    # Counter for file objects:
    c = 0

    try:
        for root, dirs, files in os.walk('.', False):

            # All files need to be renames, even the ones in root folder:

            for f in files:

                # Increment counter:
                c += 1

                logging.debug('Old file:\t' + root + '\\' + f)

                oldfilename = copy.deepcopy(f)
                
                # Get some way to rename files:
                for i in keywords:

                    f = f.replace(i, keywords[i])

                logging.info('New file:\t' + root + '\\' + f + '\n')
                #os.rename(root + '\\' + oldfilename, root + ' \\' + f)

    except:
        logging.critical(f'Program broke apart.\n', exc_info=True)
        logging.error(f'Fault at filename:\t' + root + '\\' + f)

    else:
        logging.debug(f'Program ended successfully.\nTotal files checked: {c}')
