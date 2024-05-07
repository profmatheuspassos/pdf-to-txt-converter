# pdf-to-txt-converter

## Visão Geral
O `pdf-to-txt-converter` é um script Python projetado para converter arquivos PDF em documentos de texto (TXT), facilitando a leitura e manipulação de conteúdo textual de arquivos PDF em um formato mais acessível.

## Funcionalidades
- Conversão de arquivos PDF para TXT.
- Opção para converter todos os arquivos PDF em um diretório ou um arquivo específico selecionado pelo usuário.
- Limpeza de texto para remover espaços em branco indesejados e alinhar o texto à esquerda.
- Criação de um log de conversão, registrando tanto as conversões bem-sucedidas quanto os erros.

## Requisitos
- Python 3.6 ou superior
- Biblioteca PyPDF2

## Instalação

Para instalar este projeto, você tem algumas opções:

1. **Download Direto:**
   - Acesse o repositório no GitHub.
   - Clique no botão verde "Code" e então clique em "Download ZIP".
   - Descompacte o arquivo em sua máquina local.

2. **Usando Git:**
   - Abra o terminal e execute o seguinte comando para clonar o repositório:
     ```bash
     git clone https://github.com/profmatheuspassos/pdf-to-txt-converter.git
     cd pdf-to-txt-converter
     ```

3. **GitHub Desktop:**
   - Clique no botão verde "Code" e selecione "Open with GitHub Desktop".
   - Siga as instruções para clonar o repositório com o GitHub Desktop.

Após obter o código, instale as dependências necessárias:

```bash
pip install PyPDF2
```

## Uso

Para usar o script, execute o seguinte comando no terminal:

```bash
python pdf_to_txt_converter.py
```

Siga as instruções na tela para selecionar o diretório dos PDFs e escolher entre converter um arquivo específico ou todos os arquivos no diretório.

## Contribuições

Contribuições são bem-vindas! Se você tem melhorias ou correções, por favor, faça um fork do repositório e envie um pull request, ou abra uma issue com os detalhes do que gostaria de mudar.

## Observações

- O script foi testado em ambientes Windows e Linux.
- A qualidade da conversão pode variar dependendo da complexidade do layout do PDF.

## Isenção de responsabilidade

Este software é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita. Os desenvolvedores não serão responsáveis por quaisquer danos resultantes do uso deste software. Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.