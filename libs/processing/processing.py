# -*- coding: utf-8 -*-

from .base_processing import BaseProcessing

class Processing(BaseProcessing):
    def run(self, files, output_filename):        
        temp_file = 'output.tmp'
        current_date = None
        max_date = None
        
        self.processing_logger.print_stage_header(f'Quantidade de arquivos ')
        if not files:
            self.processing_logger.print_stage_result('Nenhum arquivo!\n')
            return False

        self.processing_logger.print_stage_result(f' {len(files)} arquivos\n')

        #Percorre cada arquivo
        for index, input_filename in enumerate(files):
            #Lê o arquivo e carrega os dados
            self.processing_logger.print_stage_header(f'Carregando dados do arquivo "{input_filename}" ')
            df_data = self.loader.load(input_filename)
            if df_data is None:
                self.processing_logger.print_stage_result(' FALHOU!\n')
                self.processing_logger.print_stage_result(self.loader.errMessage)
                return False

            #Guarda a data de extração do primeiro arquivo (data em que os dados foram extraídos do SIAFI para o TG)
            #Também elege essa mesma data como a maior data. A maior data será gravada na primeira linha do arquivo de saída.
            if not current_date:
                current_date = self.loader.current_date
                max_date = self.loader.current_date
            
            #Compara a data de extração dos dados do arquivo atual com a data do primeiro arquivo e interrompe
            #o processo em caso de divergência se assim tiver sido indicado na linha de comando
            if self.date_match and self.loader.current_date != current_date:
                self.processing_logger.print_stage_result(' FALHOU!\n')
                self.processing_logger.print_stage_result(f'Datas de extração divergentes. Data esperada é ' \
                            f'{current_date.strftime("%d%m%Y")}, mas foi apresentada ' \
                            f'{self.loader.current_datestrftime("%d%m%Y")}.',
                            dots=False)
                return False

            #Substitui a maior data case encontre uma mais recente
            if self.loader.current_date > max_date:
                max_date = self.loader.current_date

            self.processing_logger.print_stage_result(' successo\n')

            #Tenta adequar os dados carregados ao modelo
            self.processing_logger.print_stage_header('Ajustando ao modelo ')
            df_data = self.fitter.fit(df_data)
            if df_data is None:
                self.processing_logger.print_stage_result(' FALHOU!\n')
                self.processing_logger.print_stage_result(self.fitter.errMessage)
                return False
            
            self.processing_logger.print_stage_result(' successo\n')

            #Grava os dados ajustados em um arquivo temporário
            self.processing_logger.print_stage_header('Gravando dados ajustados ')
            saving_succeeded = self.writer.write(df_data, temp_file, max_date, mode='w' if index==0 else 'a',
                                            header=True if index==0 else False)
            if not saving_succeeded:
                self.processing_logger.print_stage_result(' FALHOU!\n')
                self.processing_logger.print_stage_result(self.writer.errMessage)
                return False
            
            self.processing_logger.print_stage_result(' successo\n')
        
        #Remove duplicatas de linhas, se assim for indicado na linha de comando
        if self.dup_shredder is not None:
            self.processing_logger.print_stage_header(f'Removendo duplicatas ')
            duplicates_removal_succeeded = self.dup_shredder.run(temp_file, output_filename)
            if not duplicates_removal_succeeded:
                self.processing_logger.print_stage_result(' FAILED\n')
                self.processing_logger.print_stage_result(self.dup_shredder.errMessage)
                return False
            
            self.processing_logger.print_stage_result(' successo\n')

        #Finaliza o processamento removendo o arquivo temporário ou renomeando-o, conforme o caso. 
        self.processing_logger.print_stage_header(f'Fechando o arquivo "{output_filename}" ')
        if self.dup_shredder is not None:
            self.file_handler.delete(temp_file)
        else:
            self.file_handler.rename(temp_file, output_filename)
        
        self.processing_logger.print_stage_result(' successo\n')
        
        return True
