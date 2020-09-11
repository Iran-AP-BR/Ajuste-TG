# -*- coding: utf-8 -*-

from .base_fitter import BaseFitter

class Fitter(BaseFitter):
    '''Classe responsável por realizar os ajustes dos dados ao modelo indicado'''

    
    def fit(self, data):
        self.errMessage = ''
        
        try:
            columns_header = self.model.structure.keys()
            df_model = self.tool.DataFrame(columns=columns_header)
            df_concat = self.tool.concat([df_model, data], sort=False)
            
            if self.model.functions:
                for f in self.model.functions:
                    df_concat = f(df_concat)
            
            df_concat = self.model.drop_columns(df_concat)
            df_concat = self.model.map_headers(df_concat)
            
            df_concat = df_concat.applymap(self.model.clean)
            
        except Exception as e:
            self.errMessage = f'{e}'
            return None

        return df_concat