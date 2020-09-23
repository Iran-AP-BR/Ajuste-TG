# -*- coding: utf-8 -*-

from os.path import basename, abspath, dirname, join
from importlib import import_module
from glob import glob
import sys


class ModelsCollection:
    '''Classe auxiliar para fornecer uma lista dos modelos disponíveis. Para adicionar um novo modelo
       deve-se acrescentar um novo módulo (arquivo) dentro de models, contendo uma classe chamada Model
       derivada da classe abstrata BaseModel. O nome do arquivo do novo módulo deve ser 
       model_<qualquer_coisa>.py. Ex: model_exec.py.'''

       
    def model(self, name):
        bundle_dir = getattr(sys, '_MEIPASS', None)
        models_dir = f'{bundle_dir}/models' if bundle_dir else abspath(dirname(__file__))

        for module in [basename(x)[:-3] for x in glob(f'{models_dir}/model_*.py')]:
            m = import_module(f'.{module}', 'models').Model()
            if m.name == name:
                return m
        return None