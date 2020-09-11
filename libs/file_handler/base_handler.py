# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseHandler():
    @abstractmethod
    def delete(self, filename):
        pass

    @abstractmethod
    def rename(self, src, dest):
        pass