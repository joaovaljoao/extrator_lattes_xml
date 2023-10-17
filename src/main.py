import os
import pandas as pd
from lattes_xml import Extrator, listar_xmls
import sqlite3
from tqdm import tqdm

def process_xml(xml):
    extrair = Extrator(os.path.join(xml))
    dados = extrair.tipo_producao(tipo_producao)
    return pd.DataFrame(dados)

if __name__ == '__main__':
    pasta_xmls = 'batchXML/'
    tipo_producao = 'PRODUCAO-BIBLIOGRAFICA'
    db_filename = f"{tipo_producao.lower().replace('-', '_')}.db"  # Nome do arquivo do banco de dados SQLite

    xmls = listar_xmls(pasta_xmls)

    df_list = []
    for xml in tqdm(xmls, desc="Processando arquivos"):
        df_list.append(process_xml(xml))

    df = pd.concat(df_list, ignore_index=True)

    # Conecte-se ao banco de dados SQLite
    conn = sqlite3.connect(db_filename)

    # Salve o DataFrame no banco de dados
    df.to_sql(name=db_filename, con=conn, if_exists='replace', index=False)

    # Feche a conexão com o banco de dados
    conn.close()
