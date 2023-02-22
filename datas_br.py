from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
         return self.data_cadastro()

    def mes_cadastro(self):
        meses_do_ano = [
            'Janeiro', 'Fevereiro', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def semana_cadastro(self):
        dias_da_semana = ['Segunda', 'Terça', 'Quarta',
                          'Quinta', 'Sexta', 'Sábado',
                          'Domingo']
        semana_cadastro = self.momento_cadastro.weekday()
        return dias_da_semana[semana_cadastro]

    def data_cadastro(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada