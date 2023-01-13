import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)
pd.set_option('max_colwidth', 80)
pd.set_option('display.max_rows', None)

'CPFL PAULISTA - SP'

te_cpfl_paulista = 0.29592
tusd_cpfl_paulista = 0.36599
tarifa_sem_impostos_cpfl_paulista = te_cpfl_paulista + tusd_cpfl_paulista
print('Tarifa Sem Impostos:', tarifa_sem_impostos_cpfl_paulista)

'TRIBUTOS'

pis_cpfl_paulista = 0.008
cofins_cpfl_paulista = 0.0362
icms_cpfl_paulista = 0.18

'GERADOR'
ambar = 0.10

'CALCULOS PIS'

pis_te_cpfl_paulista = pis_cpfl_paulista * (te_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(pis_te_cpfl_paulista)
pis_tusd_cpfl_paulista = pis_cpfl_paulista * (tusd_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(pis_tusd_cpfl_paulista)

'CALCULOS COFINS'

cofins_te_cpfl_paulista = cofins_cpfl_paulista * (te_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(cofins_te_cpfl_paulista)
cofins_tusd_cpfl_paulista = cofins_cpfl_paulista * (tusd_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(cofins_tusd_cpfl_paulista)

'CALCULOS ICMS'

icms_te_cpfl_paulista = icms_cpfl_paulista * (te_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista) / (1 - icms_cpfl_paulista))
# print(icms_te_cpfl_paulista)
icms_tusd_cpfl_paulista = (icms_cpfl_paulista * (tusd_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista) / (1 - icms_cpfl_paulista))) * 0
# print(icms_tusd_cpfl_paulista)

'CALCULOS PIS + COFINS'
te_pis_cofins_cpfl_paulista = te_cpfl_paulista / (1 - (pis_cpfl_paulista + cofins_cpfl_paulista))
# print(te_pis_cofins_cpfl_paulista)
tusd_pis_cofins_cpfl_paulista = tusd_cpfl_paulista / (1 - (pis_cpfl_paulista + cofins_cpfl_paulista))
# print(tusd_pis_cofins_cpfl_paulista)

'CALCULOS PISCOFINS + ICMS (ISENTO NA TUSD)'

te_pis_cofins_icms_cpfl_paulista_valor = te_pis_cofins_cpfl_paulista / (1 - icms_cpfl_paulista)
# print(te_pis_cofins_icms_cpfl_paulista_valor)
tusd_pis_cofins_icms_cpfl_paulista_valor = tusd_pis_cofins_cpfl_paulista
# print(tusd_pis_cofins_icms_cpfl_paulista_valor)

'CALCULOS TARIFAS'

tarifa_cheia_cpfl_paulista_valor = tarifa_sem_impostos_cpfl_paulista + pis_te_cpfl_paulista + pis_tusd_cpfl_paulista + cofins_tusd_cpfl_paulista + cofins_te_cpfl_paulista + icms_tusd_cpfl_paulista + icms_te_cpfl_paulista
# print('Tarifa Com Impostos', tarifa_cheia_cpfl_paulista_valor)
impostos_cobrados_cpfl_paulista_valor = tarifa_cheia_cpfl_paulista_valor - tarifa_sem_impostos_cpfl_paulista
# print('Impostos Cobrados', impostos_cobrados_cpfl_paulista_valor)
tarifa_aplicacao_cpfl_paulista_valor = te_pis_cofins_icms_cpfl_paulista_valor + tusd_pis_cofins_icms_cpfl_paulista_valor
# print(tarifa_aplicacao_cpfl_paulista_valor)
tarifa_compensavel_cpfl_paulista_valor = tarifa_aplicacao_cpfl_paulista_valor - impostos_cobrados_cpfl_paulista_valor
# print(tarifa_compensavel_cpfl_paulista_valor)


'CALCULO VALOR DO DESCONTO'

desconto_ambar_cpfl_paulista_valor = tarifa_compensavel_cpfl_paulista_valor * ambar
# print('Valor do Desconto: R$', desconto_ambar_cpfl_paulista_valor)

'CALCULO DA TARIFA DO GERADOR'

tarifa_ambar_cpfl_paulista_valor = tarifa_compensavel_cpfl_paulista_valor - desconto_ambar_cpfl_paulista_valor
# print('Valor da Tarifa do Gerador: R$', tarifa_ambar_cpfl_paulista_valor)

tabela_ambar_cpfl_paulista = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa Ambar'], 'Valores R$':[tarifa_sem_impostos_cpfl_paulista, tarifa_cheia_cpfl_paulista_valor, tarifa_aplicacao_cpfl_paulista_valor, tarifa_compensavel_cpfl_paulista_valor, desconto_ambar_cpfl_paulista_valor, tarifa_ambar_cpfl_paulista_valor]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_ambar_cpfl_paulista = pd.DataFrame(tabela_ambar_cpfl_paulista)
# print(tabela_ambar_cpfl_paulista)

'1º Arquivo: Dados a serem cobrados'
cobrancas_path = 'arquivos/boletagem_ambar.xlsx'
cobrancas = pd.read_excel('arquivos/boletagem_ambar.xlsx')
# print(cobrancas)

'Renomeia Colunas para coincidir com Salesforce'
#
# cobrancas = cobrancas.rename(
#     columns = {
#         'Numero da Instalação': 'Numero da Instalacao',
#         'Saldo' : 'kWh Saldo',
#         'Energia Injetada' : 'kWh Energia Injetada',
#         'Energia Consumida' : 'kWh Energia Cobrada'
#     }
# )

'CALCULA QUANTIDADE DE kWh NÃO INJETADO'

cobrancas['Diferença kWh'] = (
    cobrancas['kWh Energia Fornecida'] - cobrancas['kWh Energia Cobrada']
)

'CALCULO VALOR: QUANTO SERIA'

cobrancas['Quanto Seria'] = (
    cobrancas['kWh Energia Cobrada'] * tarifa_sem_impostos_cpfl_paulista
)

'CALCULO VALOR: VALOR DA COBRANÇA'

cobrancas['Valor Cobrança'] = (
    cobrancas['kWh Energia Cobrada'] * tarifa_ambar_cpfl_paulista_valor
)

'CALCULO VALOR: R$ DESCONTO'

cobrancas['Valor Economia'] = (
    cobrancas['Quanto Seria'] - cobrancas['Valor Cobrança']
)

'CALCULO VALOR: % DESCONTO'

cobrancas['% Desconto'] = (
    (1 - (cobrancas['Valor Cobrança'] / cobrancas['Quanto Seria']))*100
)

'2º Arquivo: UCs Ambar no Salesforce'
report_path = 'arquivos/Report-2023-01-08-19-34-56.xlsx'
report = pd.read_excel('arquivos/Report-2023-01-08-19-34-56.xlsx')

cobrancas['Numero da Instalacao'] = cobrancas['Numero da Instalacao'].astype(str)
cobrancas = pd.merge(cobrancas, report, how='left', on='Numero da Instalacao')
print(cobrancas)

# cobrancas.to_excel('arquivos/cobrancas_import_ambar.xlsx', index=False)

'''Criar cobrança'''

'custumer'
'billingType' 'Boleto'
'value'
'dueDate' 'yyyy-mm-dd'

