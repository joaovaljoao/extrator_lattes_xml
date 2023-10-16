# Extrator de Informações de Arquivos XML para Banco de Dados SQLite

Este é um script Python que permite extrair informações de arquivos XML que contêm dados de produção bibliográfica, produção técnica ou outra produção de um pesquisador. As informações extraídas são armazenadas em um banco de dados SQLite para posterior análise e consulta.

## Como Usar

### Requisitos

Certifique-se de que você tenha Python 3.x instalado em seu sistema. Além disso, você precisará das seguintes bibliotecas Python instaladas:

- `xml.etree.ElementTree`
- `pathlib`
- `pandas`
- `tqdm`

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

```
pip install -r requirements.txt
```

### Configuração

1. Coloque seus arquivos XML na pasta `batchXML/` ou especifique o caminho para a pasta desejada no arquivo `main.py`.

2. Defina o tipo de produção que deseja extrair no arquivo `main.py`. Os tipos de produção suportados são:

   - `PRODUCAO-BIBLIOGRAFICA`
   - `PRODUCAO-TECNICA`
   - `OUTRA-PRODUCAO`

### Execução

Execute o script `main.py` no seu ambiente Python:

```
python main.py
```

O script processará os arquivos XML na pasta `batchXML/` e armazenará as informações extraídas em um banco de dados SQLite.

## Estrutura de Diretórios

- `batchXML/`: Coloque seus arquivos XML nesta pasta.

- `main.py`: O script principal que processa os arquivos XML e armazena as informações no banco de dados.

- `lattes_xml.py`: O módulo que contém a classe `Extrator` para extrair informações dos arquivos XML.


## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

