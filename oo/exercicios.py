class ValorDaAcao():
    def __init__(self, empresa=None,ticker=None,*valor):
        self.empresa=empresa
        self.ticker=ticker
        self.valor=list(valor)

if __name__=='__main__':
    company=ValorDaAcao(empresa='TIM')
    tick=ValorDaAcao(ticker='TIMS3')
    valores = ValorDaAcao()
    acao=ValorDaAcao(company.empresa, tick.ticker,17.24)
    print(acao.empresa)
    print(acao.ticker)
    for valores in acao.valor:
       print(acao.valor)

