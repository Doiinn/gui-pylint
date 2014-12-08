'''
PSIT PROJECT - GUI Pylint

Author:
 - Worapong Malaiwong
 - Sirirach Junta 57070112 Section 3 w

'''
import unittest
import re
import os
import itertools
import mimetools
import mimetypes
import urllib2
from cStringIO import StringIO
from glob import glob

class Gpylint(unittest.TestCase):
    '''
     make variable as Gpylint object 
     Usage:
        gpy = Gpylint()
    '''
    def __init__(self):
        ''' initialize local variable '''
        self.filename = None
        self.filepath = ''
        self.boundary = mimetools.choose_boundary()
        self.data = ''
        self.filetype = ''
        self.body = ''
        self.returned = ''
        return

    def get_content_type(self):
        ''' return type of content '''
        return 'multipart/form-data; boundary=%s' % self.boundary

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
            self.data = StringIO(f.read()).read()
            self.filetype = mimetypes.guess_type(self.filename)[0]
            f.close()
            return {'Pass': {'Status' : 'Ok!'}}
        else:
            return {'Error' : {'Status' : 'File type or file path.'}}
    def encoded(self):
        ''' return encoded multipart'''
        flat = list(itertools.chain(['--'+self.boundary, 'Content-Disposition: file; name="uploadedfile"; filename="%s"' % \
        self.filename, 'Content-Type: %s' % self.filetype, '\r\n' + self.data]))
        flat.append('--' + self.boundary + '--')
        flat.append('')
        self.body = '\r\n'.join(flat)
        return

    def analysis(self, filepath=None):
        ''' make upload '''
        filepath = self.filepath if filepath == None else filepath
        addfile = self.add_file(filepath)
        if 'Error' in addfile:
            self.returned = addfile
            return addfile
        else:
            self.encoded()
            request = urllib2.Request('http://antares.sip.ucm.es/cesar/pylint/evaluation.php')
            request.add_header('User-agent', 'madooding v.0.0.1')
            request.add_header('Content-type', self.get_content_type())
            request.add_header('Content-length', len(self.body))
            request.add_data(self.body)
            try:
                self.returned = {'Pass' : {'Status': 'Ok!', 'Data' : self.split(urllib2.urlopen(request).read())}}    
            except:
                self.returned = {'Error' : {'Status': 'Could\'t connect to server.'}}
            return
    def split(self, rawdata):
        ''' Split raw data and return a list '''
        rawdata, spl, count = rawdata.split('\n'), [], 0
        for i in xrange(14, len(rawdata)):
            if rawdata[i] == 'Report' or rawdata[i] == '':
                break
            temp, slist = rawdata[i], []
            if temp[0] == ' ':
                ttt = spl.pop()
                ttt[2] += '\n' + temp[4:]
                spl.append(ttt)
                continue
            while len(slist) < 2:
                slist.append(temp[:temp.find(':')])
                temp = temp[temp.find(':')+1:].strip()
            slist.append(temp.strip())
            spl += [slist]
        return spl[:-2]
    def read(self):
        ''' return html result '''
        return self.returned

def main():
    ''' this is a main function '''
    obj = Gpylint()
    obj.analysis(raw_input('Path of file ex:(%s\\a.py): ' % os.getcwd()))
    print obj.read()

main()
