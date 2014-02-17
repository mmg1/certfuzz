'''
Created on Dec 9, 2013

@author: adh
'''
import os
import shutil

import subprocess

from ..build_base2 import Build

basedir = os.path.dirname(__file__)


class WindowsBuild(Build):
    PLATFORM = 'windows'
    LICENSE_FILE = 'COPYING.txt'

    def package(self):
        '''
        Builds a Windows Installer
        '''
        from .nsis import buildnsi

        # Copy files required by nsis
        for f in ['cert.ico', 'EnvVarUpdate.nsh', 'vmwarning.txt']:
            src = os.path.join(basedir, 'nsis', f)
            shutil.copy(src, self.build_dir)

        nsifile = os.path.join(self.build_dir, 'foe2.nsi')

        # generate the nsi file
        buildnsi.main(version_string="02.01.00.99", outfile=nsifile, build_dir=self.build_dir)

        # invoke makensis on the file we just made
        subprocess.call(['makensis', nsifile])