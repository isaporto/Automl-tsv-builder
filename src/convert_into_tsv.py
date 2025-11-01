import csv
import os
from colorist import Color


# Função para ler o conteúdo de um arquivo txt e retornar uma lista com as linhas
def read_txt_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


# Função para reescrever o arquivo txt excluindo as linhas já processadas
def write_remaining_lines(file_path, remaining_lines):
    with open(file_path, "w", encoding="utf-8") as f:
        for line in remaining_lines:
            f.write(line + "\n")


# Função para converter os arquivos txt em tsv com interação no terminal
def txt_to_tsv_interactive(filename):
    original_documents_path = "data/documents/extracted"
    output_file = f"data/text_chunks/{filename}.tsv"
    txt_filepath = os.path.join(original_documents_path, filename)
    txt_files = os.listdir(txt_filepath)
    print(f"Checando arquivos da pasta {filename}\n")
    if len(txt_files) != 2:
        print("Essa pasta não tem dois arquivos para montar o tsv.\n")
        return

    filepath_1 = os.path.join(txt_filepath, txt_files[0])
    filepath_2 = os.path.join(txt_filepath, txt_files[1])

    # Lendo os dois arquivos

    # Escrevendo o arquivo .tsv
    with open(output_file, "a", newline="", encoding="utf-8") as tsvfile:
        writer = csv.writer(tsvfile, delimiter="\t")

        file_1 = read_txt_file(filepath_1)
        file_2 = read_txt_file(filepath_2)

        # Iterando sobre cada linha
        i = 0
        while i < max(len(file_1), len(file_2)):
            os.system("clear")
            print("File length remaining: ", max(len(file_1), len(file_2)))
            col1 = file_1[i]
            col2 = file_2[i]

            while True:
                # Exibe no terminal as colunas lado a lado
                print(
                    f"Linha {i+1}:\nColuna 1: {Color.GREEN}{col1}{Color.OFF}\nColuna 2: {Color.YELLOW}{col2}{Color.OFF}"
                )

                # Solicita confirmação do usuário
                user_input = (
                    input(
                        "Aperte ENTER para salvar esta linha no .tsv ou 'stop' para interromper o script: \n"
                    )
                    .strip()
                    .lower()
                )

                if user_input == "":
                    # Escreve a linha no arquivo tsv
                    writer.writerow([col1, col2])

                    # Remove a linha gravada dos arquivos txt
                    file_1.pop(i)
                    file_2.pop(i)

                    # Reescrevendo os arquivos txt com as linhas restantes
                    write_remaining_lines(filepath_1, file_1)
                    write_remaining_lines(filepath_2, file_2)

                    break

                elif user_input == "stop":
                    os.system("clear")
                    print("Interrompendo o script...")
                    return
                else:
                    print("Entrada inválida. Tente novamente.")

    print(f"Arquivo {output_file} criado com sucesso!")


txt_to_tsv_interactive("UTGITB_Shell")
