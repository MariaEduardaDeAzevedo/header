# Header

## O Header é uma aplicação desenvolvida em Python para ser utilizada na linha de comando. Sua finalidade é importar um cabeçalho, previamente salvo em um arquivo, em um outro arquivo de destino.

## Esta aplicação foi pensada para facilitar a escrita de cabeçalhos padronizados em programas ou até em outros arquivos. Nos comandos abaixo, os arquivos estão dados como .txt, mas podem ser outras extensões desejadas.

### Iniciando no Header.
- Para utilizar esta ferramenta, clone este repositório!
- Após isso, vá até o diretório clonado no seu computador e execute o arquivo header.py:
```
python3 header.py 
```
- Se você acabou de iniciar verá a seguinte mensagem:
```
Olá! Bem-vindo ao Header!
Status do Header: não iniciado
Para obter ajuda no uso da ferramenta, digite:
python3 header.py help
```
- Então execute o comando: 
```
python3 header.py init
```
- Pronto! O Header está pronto para ser utilizado!

## Comandos
- Importar qualquer arquivo:
```
python3 header.py w < caminho_do_cabeçalho > < caminho_do_arquivo >
```
- Salvar um arquivo de cabeçalho na sua biblioteca de cabeçalhos:
```
python3 header.py s < caminho_do_cabeçalho >
```
- Criar um arquivo de cabeçalho direto na sua biblioteca de cabeçalhos:
```
python3 header.py c nome_do_arquivo.txt
```
- Importar um cabeçalho de sua biblioteca em um arquivo:
```
python header.py ws nome_do_cabecalho_.txt < caminho_do_arquivo >
```
- Listar os arquivos salvos em sua biblioteca:
```
python3 header.py list
```
- Editar um arquivo salvo em sua biblioteca:
```
python3 header.py e nome_do_arquivo.txt
```
- Obter ajuda:
```
python3 header.py help
```
### Algumas coisas sobre o funcionamento da ferramenta

- O editor padão utilizado para editar os arquivos abertos pela ferramenta é o VIM. A escolha pelo uso desse editor é simples: facilidade. Caso você não seja muito familiarizado com esse editor, você pode acessar este [link](https://medium.com/tableless/comandos-b%C3%A1sicos-do-vim-para-ningu%C3%A9m-ficar-preso-no-servidor-93f0d21d5508) e aprender mais sobre seu funcionamento. Em uma atualização futura, pode-se adicionar uma opção de mudança de configuração para isto.

- É provável que o arquivo header.py já esteja com uma permissão de execução, então ao invés de executar a ferramenta utilizando ``` python3 header.py ```, você poderá substituir o comando anterior por ``` ./header.py ```:
