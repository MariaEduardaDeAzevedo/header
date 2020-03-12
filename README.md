# Header

## O Header é uma aplicação desenvolvida em Python para ser utilizada na linha de comando. Sua finalidade é importar um cabeçalho, previamente salvo em um arquivo .txt, em um arquivo de destino.

## Esta aplicação foi pensada para facilitar a escrita de cabeçalhos padronizados em programas ou até em outros arquivos.

### Iniciando no Header.
- Para utilizar esta ferramenta, clone este repositório!
- Após isso, vá até o diretório clonado no seu computador e execute o arquivo header.py:
```
python header.py 
```
- Se você acabou de iniciar verá a seguinte mensagem:
```
Olá! Bem-vindo ao Header!
Status do Header: não iniciado
Comando para importar um cabeçalho em um arquivo:
python header.py w < caminho_do_cabeçalho > < caminho_do_arquivo >
```
- Então execute o comando: 
```
python header.py init
```
- Pronto! O Header está pronto para ser utilizado!

## Comandos
- Importar qualquer arquivo:
```
python header.py w < caminho_do_cabeçalho > < caminho_do_arquivo >
```
- Salvar um arquivo de cabeçalho na sua biblioteca de cabeçalhos:
```
python header.py s < caminho_do_cabeçalho >
```
- Criar um arquivo de cabeçalho direto na sua biblioteca de cabeçalhos:
```
python header.py c nome_do_arquivo.txt
```
- Importar um cabeçalho de sua biblioteca em um arquivo:
```
python header.py ws nome_do_cabecalho_.txt < caminho_do_arquivo >
```
