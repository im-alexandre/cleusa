import requests


def corona_virus():
    r = requests.get("https://pomber.github.io/covid19/timeseries.json")
    data = r.json()
    ultimos_dados = data['Brazil'][-1]
    resposta = f"""
    Até agora, foram registrados, no Brasil:
    {ultimos_dados['confirmed']} casos confirmados,
    {ultimos_dados['deaths']} mortes,
    e {ultimos_dados['recovered']} pessoas se curaram.
    Xandão, é melhor ficar em casa e lavar bem as mãos."""
    return resposta


if __name__ == '__main__':
    print(corona_virus())
