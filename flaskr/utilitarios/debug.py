import os.path
from flaskr.utilitarios.converter import Converter


class Debug:
    '''
    Parâmetros:
        texto: conteudo do debug
        nome:  nome que o arquivo será salvo, padrão 'debug'
        tipo:  'texto' ou 'query'
        adicionais: parâmetros da query, em caso do tipo ser 'query'
    '''
    def __init__(self, texto:str, nome:str='debug', tipo:str='texto', adicionais:list=[]):
        nome     = self._nome_arquivo(nome)
        arquivo  = self._abrir_arquivo(nome)
        conteudo = self._conteudo_arquivo(texto, tipo, adicionais)
        self._fechar_arquivo(conteudo, arquivo)


    def _conteudo_arquivo(self, texto:str, tipo:str, adicionais:list):
        conteudo = Converter.data_atual_string() + ': '
        if tipo == 'query':
            for item in adicionais:
                parametro = "'"+str(item)+"'" if type(item) is str else str(item)
                if type(item) is str:
                    item = "'"+str(parametro)+"'"
                texto = texto.replace('%s', parametro, 1)
        return conteudo + str(texto) +'\n'


    def _nome_arquivo(self, nome:str) -> str:
        data = Converter.data_atual_string_txt()
        return 'debug/'+str(nome)+str('-')+str(data)+'.txt'


    def _abrir_arquivo(self, nome:str):
        if os.path.exists(nome):
            return open(nome, 'a')
        return open(nome, 'w')


    def _fechar_arquivo(self, conteudo:str, arquivo):
        arquivo.write(conteudo)
        arquivo.close()