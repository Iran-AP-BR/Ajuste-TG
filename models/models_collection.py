# -*- coding: utf-8 -*-

from .model_exec import ModelExec

class ModelsCollection:
    '''Classe auxiliar para fornecer uma lista dos modelos disponíveis. Para adicionar um novo modelo
       deve-se acrescentar uma instância de sua classe à lista "modules".'''

       
    def model(self, name):
        modules = [ModelExec()]
        m = list(filter(lambda item: item.name == name, modules))
        return m[0] if m else None