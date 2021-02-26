# -*- coding: utf-8 -*-

from .base_duplicates_shredder import BaseDuplicatesShredder

class HashDuplicatesShredder(BaseDuplicatesShredder):
    '''Classe para eliminar duplicadas de linhas em arquivos de texto plano por meio da técnica de hash.'''

    
    def __init__(self, hash=None, encoding='utf-8', file_handler=None, newline='\n'):
        super().__init__(encoding=encoding, file_handler=file_handler)
        self.hash = hash
        self.newline = newline

    def run(self, original_file=None, final_file=None):
        assert original_file is not None
        assert final_file is not None

        self.errMessage = ''
        file_created = False
        try:
            with self.file_handler.open_file(filename=original_file, mode="r") as fd_original, \
                 self.file_handler.open_file(filename=final_file, mode="w") as fd_final:
                hashes = set()
                for line in fd_original:
                    line_hash = hash(line)
                    if line_hash not in hashes:
                        hashes.add(line_hash)
                        fd_final.write(line)
                        file_created = True
            
            if not file_created:
                self.errMessage = 'Empty file!'
                return False

            return True

        except Exception as e:
            self.errMessage = f'{e}'
            return False
