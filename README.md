# ping-traceroute-cli

## 1. Objetivo
A ferramenta ping-traceroute-cli foi desenvolvida para fornecer uma interface interativa para executar ferramentas de diagnóstico de rede, como Ping e Traceroute. Ele permite que os usuários realizem operações de Ping e Traceroute em um ou vários domínios e exibe a saída correspondente.

## 2. Requisitos
Para executar a ferramenta ping-traceroute-cli, os seguintes requisitos devem ser atendidos:

- **Python:** O código é escrito em Python e requer um interpretador Python compatível instalado no sistema. O código é compatível com Python 2 e Python 3.

- **Pacotes ping e traceroute:** A ferramenta depende que os pacotes ping e traceroute estejam instalados no sistema. Verifique se essas ferramentas estão disponíveis no ambiente de linha de comando do sistema.

## 3. Execução
Para executar o código Ferramentas de Rede, siga estas etapas:

Clone o repositório do código ou copie o código para um diretório local em sua máquina.

`git clone https://github.com/lucasgmarques/ping-traceroute-cli.git`

Abra um terminal ou prompt de comando e navegue até o diretório onde o código está localizado.

Execute o seguinte comando para executar o código:

`$ python3 network_tools.py`

O programa exibirá um menu com as opções disponíveis:

```
Ferramentas de Rede
1 - Ping
2 - Traceroute
0 - Sair
Digite uma opção:
```
- Selecione **1** para _Ping_: Você será solicitado a inserir o(s) domínio(s) para o Ping. Múltiplos domínios podem ser inseridos separados por vírgulas. Cada domínio será validado e processado individualmente.
- Selecione **2** para _Traceroute_: Você será solicitado a inserir o(s) domínio(s) para o Traceroute. Múltiplos domínios podem ser inseridos separados por vírgulas. Cada domínio será validado e processado individualmente.
- Selecione **0** para sair do programa.
Após selecionar uma opção e inserir o(s) domínio(s), o programa realizará a(s) operação(ões) de rede correspondente(s) e exibirá a saída.

Após a conclusão da operação, o menu será exibido novamente, permitindo que você escolha outra opção ou saia do programa.

Observação: Verifique se os domínios inseridos são nomes de domínio válidos no formato adequado (por exemplo, exemplo.com). Domínios inválidos resultarão em uma mensagem de erro.
