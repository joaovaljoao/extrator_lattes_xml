import os
import xml.etree.ElementTree as ET
from typing import List, Dict, Union
import logging
from pathlib import Path

class Extrator:
    """
    Esta classe permite extrair informações de um arquivo XML contendo dados de produção bibliográfica.
    
    Args:
        xml_file (str): O caminho para o arquivo XML de entrada.

    Attributes:
        xml_file (str): O caminho para o arquivo XML de entrada.
        tree (ET.ElementTree): A árvore XML do arquivo.
        root (ET.Element): O elemento raiz da árvore XML.

    Methods:
        tipo_producao(tipo_producao: str) -> List[Dict[str, str]]:
            Extrai informações sobre a produção bibliográfica de um determinado tipo.
        extract_info() -> Dict[str, str]:
            Extrai informações dos elementos 'DADOS-GERAIS' e combina com atributos do 'root'.
    """

    def __init__(self, xml_file: str) -> None:
        """
        Inicializa um objeto Extrator com o caminho do arquivo XML.

        Args:
            xml_file (str): O caminho para o arquivo XML de entrada.
        """
        if not os.path.exists(xml_file):
            raise FileNotFoundError(f"O arquivo XML '{xml_file}' não existe.")
        
        self.xml_file = xml_file
        self.tree: ET.ElementTree = None
        self.root: ET.Element = None
        self._parse_xml()
        # nome da subpasta do xml
        self.tipo_pesquisador = Path(self.xml_file).parent.name
        self.cnpq_id: str = self.root.get("NUMERO-IDENTIFICADOR")
        self.data_atualizacao: str = self.root.get("DATA-ATUALIZACAO")
        self.data_hora: str = self.root.get("DATA-HORA-ATUALIZACAO")
        self.resumo_cv: str = self.root.get("TEXTO-RESUMO-CV-RH")
        

    def _parse_xml(self) -> None:
        try:
            self.tree = ET.parse(self.xml_file)
            self.root = self.tree.getroot()
        except ET.ElementTree.ParseError as e:
            logging.error(f"Erro ao analisar o arquivo XML: {str(e)}")
            raise


    def tipo_producao(self, tipo_producao: str) -> List[Dict[str, str]]:
        """
        Extrai informações sobre a produção bibliográfica de um determinado tipo.

        Args:
            tipo_producao (str): O tipo de produção bibliográfica a ser extraído.

        Returns:
            list: Uma lista de dicionários contendo informações sobre a produção bibliográfica.
        """
        if self.root is None:
            return []  # Retorna uma lista vazia se o arquivo XML não foi analisado com sucesso

        dados = []
        producao_elemento = self.root.find(tipo_producao)
        if producao_elemento is None:
            return dados
        
        for producao_item in producao_elemento:
            for tipo_producao_elemento in producao_item:
                tipo_producao = tipo_producao_elemento.tag
                dados_linha = {
                    'cnpq_id': self.cnpq_id,
                    'tipo_producao': tipo_producao,
                    'tipo_pesquisador': self.tipo_pesquisador,
                }
                for atributos_elemento in tipo_producao_elemento:
                    if atributos_elemento.tag.startswith('DADOS-BASICOS') or atributos_elemento.tag.startswith('DETALHAMENTO'):
                        dados_linha.update(atributos_elemento.attrib)
                dados.append(dados_linha)
        
        return dados


def listar_xmls(path):
    """
    Lista todos os arquivos XML válidos em um diretório e suas subpastas.

    Args:
        path (str): O caminho para o diretório raiz a ser pesquisado.

    Returns:
        list: Uma lista de caminhos completos para arquivos XML válidos encontrados no diretório e subdiretórios.
    """
    arquivos_xml = [os.path.join(pasta_raiz, arquivo)
                    for pasta_raiz, subpastas, arquivos in os.walk(path)
                    for arquivo in arquivos
                    if arquivo.endswith('.xml') and os.path.getsize(os.path.join(pasta_raiz, arquivo)) > 0]
    return arquivos_xml



