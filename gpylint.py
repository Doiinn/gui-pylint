'''
PSIT PROJECT - GUI Pylint

Author:
 - Worapong Malaiwong
 - Sirirach Junta 57070112 Section 3

'''
import re
import os
import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
from glob import glob

class Gpylint(object):
    '''
     make variable as Gpylint object 
     Usage:
        gpy = Gpylint()
    '''
    def __init__(self):
        self.filename = None
        self.filepath = ''
        self.data = ''
    def makepath(self, filepath):
        ''' return a path of file '''
        if '\\' not in filepath:
            cwd = os.getcwd()
            return cwd + '\\' + filepath
        else:
            return '\\'.join(filepath.split('\\'))
            
    def add_file(self, filepath):
        ''' add file to be uploaded '''
        chk = re.search('\.py$', filepath)
        filepath = self.makepath(filepath)
        if chk and len(glob(filepath)) == 1:
            self.filename = filepath.split('\\')[-1]
            self.filepath = filepath
            f = open(filepath, 'r')
            self.data = f.read()
            f.close()
            return {'Pass': 'Ok!'}
        else:
            return {'Error':'File type or file path.'}

