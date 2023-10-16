import os
import pandas as pd
from lattes_xml import Extrator, listar_xmls
import csv
from tqdm import tqdm

def process_xml(xml):
    extrair = Extrator(os.path.join(xml))
    dados = extrair.tipo_producao(tipo_producao)
    return pd.DataFrame(dados)

if __name__ == '__main__':
    pasta_xmls = 'batchXML/'
    tipo_producao = 'PRODUCAO-BIBLIOGRAFICA'
    csv_filename = f"{tipo_producao.lower().replace('-', '_')}.csv"

    xmls = listar_xmls(pasta_xmls)

    df_list = []
    for xml in tqdm(xmls, desc="Processando arquivos"):
        df_list.append(process_xml(xml))

    df = pd.concat(df_list, ignore_index=True)

    df.to_csv(csv_filename, index=False, sep='\t', encoding='iso-8859-1', escapechar='\\', quoting=csv.QUOTE_NONE)
