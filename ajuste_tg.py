# -*- coding: utf-8 -*-

import re
import os
import sys
import hashlib
import argparse
import logging
import pandas as pd
from glob import glob
from datetime import datetime
from pathlib import Path
from models import ModelsCollection
from libs.data_loader import Loader
from libs.model_fitter import Fitter
from libs.arguments_parser import Parser
from libs.file_writer import CsvWriter
from libs.file_reader import ExcelReader
from libs.file_handler import FileHandler
from libs.duplicates_shredder import HashDuplicatesShredder
from libs.processing import Processing
from libs.processing_logger import ProcessingLogger


def write_message(message):
    sys.stdout.write(message)
    sys.stdout.flush()

def hash(text):
    return hashlib.md5(text.encode()).digest()


if __name__ == '__main__':

    #Define o nome do programa
    prog_name = Path(sys.argv[0]).stem

    #Instancia o parseador de linha de comando e carrega/valida as opções informadas pelo usuário
    parser = Parser(argparse.ArgumentParser, prog_name, os.path.basename, glob)
    args = parser.parse_arguments()

    #define o nome da pasta de logs e a cria, se necessário
    logs_path = 'logs'
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    #Configura o logging
    logging.basicConfig(filename=f'{logs_path}/{prog_name}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
                        level=logging.INFO, format='%(asctime)-15s %(message)s')
    
    try:
        #Define o nome do arquivo de saída
        output_filename = args.output if args.output else f'output_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

        #Instancia o logger de processamento
        processing_logger = ProcessingLogger(write=write_message, logger=logging.getLogger(__name__))

        #Seleciona o modelo indicado pelo usuário
        processing_logger.print_stage_header(f'Selecionando modelo "{args.model}" ')
        model = ModelsCollection().model(args.model)
        if model:
            processing_logger.print_stage_result(' sucesso\n')

            #Instancia o Leitor de Arquvios, o Carregador de Dados, o Ajustador, 
            # o Gravador, o Eliminador de Duplicatas e o Manipulador de Arquivos
            loader = Loader(model=model, reader=ExcelReader(tool=pd))
            fitter = Fitter(model=model, tool=pd)
            writer = CsvWriter(compression=args.gzip)
            output_filename = writer.output_filename(filename=output_filename)

            file_handler = FileHandler(compressed=args.gzip)
            dup_shredder = HashDuplicatesShredder(hash=hash, file_handler=file_handler) \
                                             if args.remove_duplicates else None
        
            #Instancia o processamento
            processing = Processing(loader=loader, 
                                    fitter=fitter, writer=writer, dup_shredder=dup_shredder,
                                    file_handler=file_handler, processing_logger=processing_logger,
                                    date_match=args.date_match)

            #Executa o processamento
            if processing.run(files=args.files, output_filename=output_filename):
                files_list = '- '+'\n- '.join(args.files)
                processing_logger.print_stage_result('\nProcessamento finalizado com sucesso!\n')
                processing_logger.print_stage_result(f'Lista de arquivos: \n\n{files_list}', to_screen=False)
            else:
                processing_logger.print_stage_result('\nProcessamento falhou!\n')
        
        else:
            processing_logger.print_stage_result(' não encontrado!\n')

    except Exception as e:
        processing_logger.print_stage_result(f'\n{repr(e)}\n')
        processing_logger.print_stage_result('\nProcessamento falhou!\n')
    
    input('\nPressione ENTER para encerrar ...')
    