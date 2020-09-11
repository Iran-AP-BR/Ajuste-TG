# -*- coding: utf-8 -*-

import os
from .base_handler import BaseHandler

class FileHandler(BaseHandler):
    '''Classe para manipulação básica de arquivos'''

    
    def delete(self, filename):
        if os.path.exists(filename):
            os.unlink(filename)

    def rename(self, src, dest):
        if os.path.exists(dest):
            os.unlink(dest)
        os.rename(src, dest)
