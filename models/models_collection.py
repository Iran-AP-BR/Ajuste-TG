# -*- coding: utf-8 -*-

from importlib import import_module
from glob import glob
from os.path import basename

class ModelsCollection:
    '''Classe auxiliar para fornecer uma lista dos modelos disponíveis. Para adicionar um novo modelo
       deve-se acrescentar um novo módulo (arquivo) dentro de models, contendo uma classe chamada Model
       derivada da classe abstrata BaseModel. O nome do arquivo do novo módulo deve ser 
       model_<qualquer_coisa>.py. Ex: model_exec.py.'''

       
    def model(self, name):
        modules = [basename(x)[:-3] for x in glob('models/model_*.py')]
        for module in modules:
            m = import_module(f'.{module}', 'models').Model()
            if m.name == name:
                return m
        return None