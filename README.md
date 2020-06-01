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

### Facilitando
Você pode alterar o arquivo .bashrc no seu Linux para poder utilizar de forma mais 
conveniente a aplicação. Para isso siga os passos:

- Cetifique-se de que está na sua home usando o comando pwd:
```
$ pwd
/home/seu_nome_de_usuario
```
- Na home, digite o seguinte comando:
```
$ sudo vim .bashrc
```
- Será pedido a sua senha de permissão, digite-a para permitir a edição do arquivo.

- Após o passo acima, procure a parte do arquivo que contém algo semelhante a:

```
# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
```
- Logo abaixo de 
```
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
```
adicione 
```
alias header='~/<caminho do diretório do repositório clonado>/./header.py'
```

- Pressiona :wq para salvar as alterações e fechar o arquivo

- Digite no terminal a mesma linha que você adicionou no arquivo

- Agora você pode chamar o Header de qualquer lugar da sua máquina pelo comando 
```
header
```

## Comandos

_Considerando que você alterou o arquivo .bashrc, utilizaremos apenas header para chamar a aplicação, caso você não o tenha feito, assegure que está no diretório do repositório clonado e rode a aplicação utilizando_ ```python3 header.py``` _ou_ ```./header.py```

- Importar qualquer arquivo:
```
header w < caminho_do_cabeçalho > < caminho_do_arquivo >
```
- Salvar um arquivo de cabeçalho na sua biblioteca de cabeçalhos:
```
header s < caminho_do_cabeçalho >
```
- Criar um arquivo de cabeçalho direto na sua biblioteca de cabeçalhos:
```
header c nome_do_arquivo.txt
```
- Importar um cabeçalho de sua biblioteca em um arquivo:
```
header ws nome_do_cabecalho_.txt < caminho_do_arquivo >
```
- Listar os arquivos salvos em sua biblioteca:
```
header list
```
- Editar um arquivo salvo em sua biblioteca:
```
header e nome_do_arquivo.txt
```
- Excluir um ou mais arquivos salvos em sua biblioteca (você pode passar vários argumentos nessa funcionalidade):
```
header d nome_do_arquivo.txt
```
- Obter ajuda:
```
header help
```
### Algumas coisas sobre o funcionamento da ferramenta

- O editor padão utilizado para editar os arquivos abertos pela ferramenta é o VIM. A escolha pelo uso desse editor é simples: facilidade. Caso você não seja muito familiarizado com esse editor, você pode acessar este [link](https://medium.com/tableless/comandos-b%C3%A1sicos-do-vim-para-ningu%C3%A9m-ficar-preso-no-servidor-93f0d21d5508) e aprender mais sobre seu funcionamento. Em uma atualização futura, pode-se adicionar uma opção de mudança de configuração para isto.

- É provável que o arquivo header.py já esteja com uma permissão de execução, então ao invés de executar a ferramenta utilizando ``` python3 header.py ```, você poderá substituir o comando anterior por ``` ./header.py ```.
