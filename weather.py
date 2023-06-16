import argparse
import json
import sys
from configparser import ConfigParser
from urllib import error, parse, request

URL_BASE_API_CLIMA = "http://api.openweathermap.org/data/2.5/weather"

def ler_argumentos_cli():
    # Lê e processa os argumentos fornecidos na linha de comando
    parser = argparse.ArgumentParser(description="Obtém informações de clima e temperatura para uma cidade")
    parser.add_argument("cidade", nargs="+", type=str, help="Informe o nome da cidade")
    parser.add_argument("-i", "--imperial", action="store_true", help="Exibe a temperatura em unidades imperiais")
    return parser.parse_args()

def construir_query_clima(nome_cidade, imperial=False):
    # Constrói a URL para consultar a API de clima
    chave_api = obter_chave_api()
    nome_cidade_formatado = " ".join(nome_cidade)
    nome_cidade_encoded = parse.quote_plus(nome_cidade_formatado)
    unidades = "imperial" if imperial else "metric"
    url = f"{URL_BASE_API_CLIMA}?q={nome_cidade_encoded}&units={unidades}&appid={chave_api}"
    return url

def obter_chave_api():
    # Obtém a chave da API de clima a partir do arquivo de configuração
    config = ConfigParser()
    config.read("secrets.ini")
    return config.get("openweather", "api_key")

def obter_dados_clima(url_query):
    # Obtém os dados de clima da API
    try:
        resposta = request.urlopen(url_query)
        dados = resposta.read()
        return json.loads(dados)
    except error.HTTPError as e:
        if e.code == 401:
            sys.exit("Acesso negado. Verifique sua chave da API.")
        elif e.code == 404:
            sys.exit("Não é possível encontrar dados de clima para esta cidade.")
        else:
            sys.exit(f"Algo deu errado... ({e.code})")
    except error.URLError:
        sys.exit("Erro: Não foi possível conectar-se à API de clima.")
    except json.JSONDecodeError:
        sys.exit("Não foi possível ler a resposta do servidor.")

def exibir_informacoes_clima(dados_clima, imperial=False):
    # Exibe as informações de clima na saída padrão
    cidade = dados_clima["name"]
    descricao_clima = dados_clima["weather"][0]["description"]
    temperatura = dados_clima["main"]["temp"]

    print(f"{cidade:^20}", end="")
    print(f"\t{descricao_clima.capitalize():^20}", end=" ")
    print(f"({temperatura}°{'F' if imperial else 'C'})")

if __name__ == "__main__":
    args_usuario = ler_argumentos_cli()
    url_query_clima = construir_query_clima(args_usuario.cidade, args_usuario.imperial)
    dados_clima = obter_dados_clima(url_query_clima)
    exibir_informacoes_clima(dados_clima, args_usuario.imperial)
