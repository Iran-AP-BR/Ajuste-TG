# -*- coding: utf-8 -*-

from .base_processing_logger import BaseProcessingLogger

class ProcessingLogger(BaseProcessingLogger):
    '''Classe para escrever mensagens na tela e no arquivo de log'''


    def __print__(self, message, dots=False, to_screen=True):
        if to_screen:
            screen_message = message 
            if dots:
                screen_message += '.'*(80-len(message))
            self.write(screen_message)

        if self.logger:
            if message[0] == '\n':
                message = message[1:]
            
            if message[-1] == '\n':
                message = message[:-1]

            self.logger.info(message.strip())

    def print_stage_header(self, message, to_screen=True):
        self.__print__(message, dots=True, to_screen=to_screen)

    def print_stage_result(self, message, to_screen=True):
        self.__print__(message, to_screen=to_screen)
