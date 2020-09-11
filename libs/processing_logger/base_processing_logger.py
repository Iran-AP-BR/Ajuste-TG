# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseProcessingLogger(ABC):
    def __init__(self, write, logger=None):
        self.write = write
        self.logger = logger

    @abstractmethod
    def print_stage_header(self, msg):
        pass

    @abstractmethod
    def print_stage_result(self, msg):
        pass
