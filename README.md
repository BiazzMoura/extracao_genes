
# Extração de Genes Housekeeping

Este projeto contém um script Python desenvolvido para extrair genes housekeeping de arquivos FASTA. O objetivo é identificar e armazenar as sequências de genes específicos em arquivos FASTA separados, facilitando análises posteriores.

## Requisitos

- Python 3.x
- Biopython

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/BiazzMoura/extracao_genes.git
    cd extracao_genes
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install biopython
    ```

## Uso

1. Coloque seus arquivos FASTA no diretório especificado no script (`fasta_files_dir`). Certifique-se de que os arquivos tenham a extensão `.fna`.

2. Execute o script:

    ```bash
    python extract_housekeeping_genes.py
    ```

3. O script lerá todos os arquivos `.fna` no diretório especificado, identificará as sequências dos genes housekeeping e salvará cada conjunto de sequências em arquivos FASTA separados.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.



