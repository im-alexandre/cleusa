"""
Autor: Fábio Berbert de Paula <fberbert@gmail.com>
Data : 27/11/2018
"""

def previsao(local=''):
    #pip install requests-html
    from requests_html import HTMLSession
    import re

    session = HTMLSession()

    url = 'https://www.google.com.br/search?q=previsao+do+tempo&oq=previsao+do+tempo&ie=UTF-8'
    if local != '':
        local = local.replace(' ', '+')
        url = url.replace('tempo', 'tempo+' + local)

    #URL resultado da busca no Google por: previsao do tempo
    r = session.get(url)

    #abaixo defino os seletores CSS de cada elemento da pagina
    #e armazeno nas devidas variaveis
    selector_city = '#wob_loc'
    city = r.html.find(selector_city, first=True).text

    selector_date = '#wob_dts'
    date = r.html.find(selector_date, first=True).text

    selector_state = '#wob_dc'
    state = r.html.find(selector_state, first=True).text

    selector_temp = '#wob_tm'
    temp = r.html.find(selector_temp, first=True).text

    #regex para limpar informacoes irrelevantes
    regex = re.compile(r'\nTemperatura.*$', re.DOTALL)
    selector_dtl = 'div.wob-dtl'
    dtl = r.html.find(selector_dtl, first=True).text
    dtl = regex.sub("", dtl)
    dados = {'cidade': city.split(',')[0], 'dia': date, 'temperatura': temp}
    dados.update({x: y for x, y in [i.split(':') for i in dtl.split('\n')]})
    dados['Vento'] = dados['Vento'][:-5]

    string = f"""
    Previsão do Tempo em {dados['cidade']}, {dados['dia']}.
    Temperatura: {dados['temperatura']} °C;
    Probabilidade de chuva: {dados['Chuva']};
    Umidade relativa do ar: {dados['Umidade']};
    Velocidade do vento: {dados['Vento']}
    """
    return string


if __name__ == '__main__':
    # leitura da localidade (parâmetro via linha de comando)
    import sys
    local = ''
    if len(sys.argv) > 0:
        sys.argv.pop(0)
        local = ' '.join(sys.argv)

    print(previsao())
