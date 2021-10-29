from datetime import datetime as dt, timedelta


class Converter:
    def data_atual_string():
        data_hoje = dt.today()
        return str(data_hoje.strftime('%d/%m/%Y %H:%M:%S'))


    def data_atual_string_txt():
        data_hoje = dt.today()
        return str(data_hoje.strftime('%d-%m-%Y'))