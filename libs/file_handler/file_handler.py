# -*- coding: utf-8 -*-

import os
import gzip
from pathlib import Path
from .base_handler import BaseHandler

class FileHandler(BaseHandler):
    '''Classe para manipulação básica de arquivos'''

    def open_file(self, filename, mode):
        if self.compressed:
            return gzip.open(filename=filename, mode=mode)
        
        return open(file=filename, mode=mode, encoding=self.encoding)

    def delete(self, filename):
        if os.path.exists(filename):
            os.unlink(filename)

    def rename(self, src, dest):
        self.delete(dest)
        
        with self.open_file(filename=src, mode="r") as fd_src, \
             self.open_file(filename=dest, mode="w") as fd_dest:
            fd_dest.write(fd_src.read())
        
        self.delete(src)

    def mkdir(self, path, file=False):
        if file:
            path = str(Path(path).parents[0])
        
        if path not in ['.', '..', '\\', '/']:
            Path(path).mkdir(parents=True, exist_ok=True)