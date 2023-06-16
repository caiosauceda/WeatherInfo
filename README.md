# Obtendo Informações de Clima

Este é um script em Python que utiliza a API do OpenWeatherMap para obter informações meteorológicas para uma cidade específica. Ele permite que você informe o nome da cidade como argumento e escolha exibir a temperatura em unidades imperiais, se desejar.

## Uso

Para utilizar o script, execute-o a partir da linha de comando e forneça o nome da cidade como argumento. Você pode usar a opção `-i` ou `--imperial` para exibir a temperatura em unidades imperiais.

Exemplo:

py weather.py china

Isso exibirá as informações meteorológicas para a cidade de Londres em unidades métricas (Celsius).

py weather.py china -i

Isso exibirá as informações meteorológicas para a cidade de Nova York em unidades imperiais (Fahrenheit).

## Dependências

O script requer as seguintes dependências:

- `argparse`: usado para analisar argumentos da linha de comando.
- `json`: usado para manipular dados JSON.
- `sys`: usado para interagir com o interpretador Python.
- `configparser`: usado para ler a chave da API do arquivo de configuração.
- `urllib` e `request`: usados para realizar requisições HTTP à API.

Certifique-se de instalar essas dependências antes de executar o script.

Além disso, o script espera que um arquivo de configuração chamado `secrets.ini` esteja presente no mesmo diretório, contendo a chave da API do OpenWeatherMap.

Sinta-se à vontade para personalizar e modificar o código de acordo com suas necessidades.
