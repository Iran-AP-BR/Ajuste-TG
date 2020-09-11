# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseProcessing(ABC):
    def __init__(self, loader, fitter, writer, dup_shredder, file_handler, processing_logger, date_match=False):
        self.loader = loader
        self.fitter = fitter
        self.writer = writer
        self.dup_shredder = dup_shredder
        self.file_handler = file_handler
        self.date_match = date_match
        self.processing_logger = processing_logger

    @abstractmethod
    def run(self, files, output_filename) -> bool:
        pass
