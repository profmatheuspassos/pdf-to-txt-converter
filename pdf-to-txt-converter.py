import os
import sys
from PyPDF2 import PdfReader
from datetime import datetime

# Limpa a tela do console
os.system('cls' if os.name == 'nt' else 'clear')

def get_pdf_files(directory):
    """ Retorna uma lista de arquivos PDF no diretório especificado. """
    return [file for file in os.listdir(directory) if file.endswith('.pdf')]

def convert_pdf_to_txt(pdf_path, txt_path):
    """ Converte um arquivo PDF em um arquivo TXT, tratando espaços e quebras de linha. """
    reader = PdfReader(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as f:
        for page in reader.pages:
            text = page.extract_text()
            if text:
                cleaned_text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
                f.write(cleaned_text + '\n')

while True:
    directory = input("Por favor, insira o caminho da pasta com os arquivos PDF: ")
    pdf_files = get_pdf_files(directory)
    if not pdf_files:
        print("Não foram encontrados arquivos PDF na pasta especificada.")
        retry = input("Deseja tentar outro diretório? (s/n): ")
        if retry.lower() != 's':
            print("Script finalizado.")
            sys.exit()
    else:
        break

print("Arquivos PDF encontrados:")
for index, file in enumerate(pdf_files, start=1):
    print(f"[{index}] {file}")

choice = input("Deseja converter todos os arquivos? (s/n): ")
if choice.lower() == 'n':
    file_number = int(input("Digite o número do arquivo que deseja converter: "))
    pdf_files = [pdf_files[file_number - 1]]

log_entries = []
log_filename = f"{datetime.now().strftime('%Y-%m-%d - %Hh%M')}-conversion-log.txt"

for pdf_file in pdf_files:
    txt_file = pdf_file.replace('.pdf', '.txt')
    txt_path = os.path.join(directory, txt_file)
    try:
        convert_pdf_to_txt(os.path.join(directory, pdf_file), txt_path)
        log_entries.append(f"{pdf_file} convertido para {txt_file} em {datetime.now().strftime('%Y-%m-%d %Hh%M')}")
    except Exception as e:
        log_entries.append(f"Erro ao converter {pdf_file}: {str(e)}")

with open(os.path.join(directory, log_filename), 'w', encoding='utf-8') as log_file:
    for entry in log_entries:
        log_file.write(entry + '\n')

print("Conversão concluída. Verifique os arquivos TXT e o log para mais detalhes.")