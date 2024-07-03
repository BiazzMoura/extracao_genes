from Bio import SeqIO
import os

# Defina os IDs ou descrições dos genes housekeeping que você deseja extrair
housekeeping_genes = {
    "recA": "recA",
    "polA": "polA",
    "gyrA": "gyrA",
    "ddrA": "ddrA",
    "ddrB": "ddrB",
    "uvrD": "uvrD",
    "rpoB": "rpoB",
}

# Diretório contendo os arquivos FASTA
fasta_files_dir = "/Users/biamoura/Documents/TCC/"

# Listar todos os arquivos .fna no diretório
fasta_files = [os.path.join(fasta_files_dir, f) for f in os.listdir(fasta_files_dir) if f.endswith('.fna')]

# Dicionário para armazenar as sequências dos genes housekeeping
extracted_sequences = {gene: [] for gene in housekeeping_genes}

# Iterar através dos arquivos FASTA
for fasta_file in fasta_files:
    if not os.path.isfile(fasta_file):
        print(f"Arquivo não encontrado: {fasta_file}")
        continue
    print(f"Lendo arquivo: {fasta_file}")
    for record in SeqIO.parse(fasta_file, "fasta"):
        description = record.description.lower()
        print(f"Analisando sequência: {record.id} - {description}")
        for gene, gene_name in housekeeping_genes.items():
            if gene_name.lower() in description:
                print(f"Encontrado gene {gene_name} em {record.id}")
                # Modificar o ID para incluir o nome do arquivo para diferenciar as linhagens
                record.id = f"{os.path.basename(fasta_file)}_{record.id}"
                extracted_sequences[gene].append(record)

# Salvar as sequências extraídas em arquivos FASTA separados para cada gene
for gene, sequences in extracted_sequences.items():
    if sequences:
        with open(f"{gene}_sequences.fasta", "w") as output_handle:
            SeqIO.write(sequences, output_handle, "fasta")
        print(f"As sequências do gene {gene} foram salvas em {gene}_sequences.fasta")
    else:
        print(f"Nenhuma sequência encontrada para o gene {gene}")

print("Processamento concluído.")
