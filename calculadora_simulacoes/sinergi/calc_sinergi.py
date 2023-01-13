import pandas as pd

'PRODUTO - GERADOR'

sinergi = 0.07


''' Tarifas Distribuidora:'''

'COPEL'

te_copel = 0.25894
tusd_copel = 0.31080
tarifa_sem_impostos_copel = te_copel + tusd_copel

'TRIBUSTOS'

pis_copel = 0.009161
cofins_copel = 0.042190
icms_copel = 0.18

'CALCULAR PIS'

pis_te_copel = pis_copel * (te_copel / (1 - pis_copel - cofins_copel))
# print(pis_te_copel)
pis_tusd_copel = pis_copel * (tusd_copel / (1 - pis_copel - cofins_copel))
# print(pis_tusd_copel)

'CALCULAR COFINS'

cofins_te_copel = cofins_copel * (te_copel / (1 - pis_copel - cofins_copel))
# print(cofins_te_copel)
cofins_tusd_copel = cofins_copel * (tusd_copel / (1 - pis_copel - cofins_copel))
# print(cofins_tusd_copel)

'CALCULAR ICMS 18% - ISENTA NA TUSD'

icms_te_copel = icms_copel * (te_copel / (1 - pis_copel - cofins_copel) / (1 - icms_copel))
# print(icms_te_copel)
icms_tusd_copel = 0
# print(icms_tusd_copel)

'CALCULAR PISCOFINS'

te_pis_cofins_copel = te_copel / (1 - (pis_copel + cofins_copel))
# print(te_pis_cofins_copel)
tusd_pis_cofins_copel = tusd_copel / (1 - (pis_copel + cofins_copel))
# print(tusd_pis_cofins_copel)

'CALCULAR PISCOFINS + ICMS'

te_pis_cofins_icms_copel_valor = te_pis_cofins_copel / (1 - icms_copel)
# print(te_pis_cofins_icms_copel_valor)
tusd_pis_cofins_icms_copel_valor = tusd_pis_cofins_copel
# print(tusd_pis_cofins_icms_copel_valor)

'CALCULAR TARIFA COM IMPOSTOS'
te_impostos_valor = pis_te_copel + cofins_te_copel + icms_te_copel
# print(te_impostos_valor)
tusd_impostos_valor = pis_tusd_copel + cofins_tusd_copel
# print(tusd_impostos_valor)

'TARIFAS COPEL'

tarifa_cheia_copel_valor = tarifa_sem_impostos_copel + pis_te_copel + pis_tusd_copel + cofins_tusd_copel + cofins_te_copel + icms_tusd_copel + icms_te_copel
# print(tarifa_cheia_copel_valor)
impostos_cobrados_copel_valor = te_impostos_valor + tusd_impostos_valor
# print(impostos_cobrados_copel_valor)
tarifa_compensavel_copel_valor = tarifa_cheia_copel_valor - impostos_cobrados_copel_valor
# print(tarifa_compensavel_copel_valor)

'CALCULO VALOR DO DESCONTO'

desconto_sinergi_copel_valor = tarifa_compensavel_copel_valor * sinergi
# print('Valor do Desconto: R$', desconto_sinergi_copel_valor)

'CALCULO DA TARIFA DO GERADOR'

tarifa_sinergi_copel_valor = tarifa_compensavel_copel_valor - desconto_sinergi_copel_valor
# print('Valor da Tarifa do Gerador: R$', tarifa_sinergi_copel_valor)

tabela_sinergi_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa Sinergi'], 'Valores R$':[tarifa_sem_impostos_copel, tarifa_cheia_copel_valor, tarifa_compensavel_copel_valor, desconto_sinergi_copel_valor, tarifa_sinergi_copel_valor]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_sinergi_copel = pd.DataFrame(tabela_sinergi_copel)
print(tabela_sinergi_copel)
#
# '1º Arquivo: Dados a serem cobrados'
# cobrancas_path = 'arquivos/boletagem_ambar.xlsx'
# cobrancas = pd.read_excel('arquivos/boletagem_ambar.xlsx')
# # print(cobrancas)
#
# 'Renomeia Colunas para coincidir com Salesforce'
#
# cobrancas = cobrancas.rename(
#     columns = {
#         'Numero da Instalação': 'Numero da Instalacao',
#         'Saldo' : 'kWh Saldo',
#         'Energia Injetada' : 'kWh Energia Injetada',
#         'Energia Consumida' : 'kWh Energia Cobrada'
#     }
# )
#
# 'CALCULO VALOR: QUANTO SERIA'
#
# cobrancas['Quanto Seria'] = (
#     cobrancas['kWh Energia Cobrada'] * tarifa_sem_impostos_cpfl_paulista
# )
#
# 'CALCULO VALOR: VALOR DA COBRANÇA'
#
# cobrancas['Valor Cobrança'] = (
#         cobrancas['kWh Energia Cobrada'] * tarifa_sinergi_copel_valor
# )
#
# 'CALCULO VALOR: R$ DESCONTO'
#
# cobrancas['Valor Economia'] = (
#     cobrancas['Quanto Seria'] - cobrancas['Valor Cobrança']
# )
#
# 'CALCULO VALOR: % DESCONTO'
#
# cobrancas['% Desconto'] = (
#     (1 - (cobrancas['Valor Cobrança'] / cobrancas['Quanto Seria']))*100
# )
#
# # 'CALCULO DO VALOR RETIDO: R$ IMPOSTO RETIDO'
# #
# # cobrancas['Valor Retido'] = (
# #     cobrancas['kWh Energia Cobrada'] * impostos_cobrados_cpfl_paulista_valor
# # )
#
# '2º Arquivo: UCs Ambar no Salesforce'
# report_path = 'arquivos/Report-2023-01-08-19-34-56.xlsx'
# report = pd.read_excel('arquivos/Report-2023-01-08-19-34-56.xlsx')
#
# cobrancas['Numero da Instalacao'] = cobrancas['Numero da Instalacao'].astype(str)
# cobrancas = pd.merge(cobrancas, report, how='left', on='Numero da Instalacao')
# print(cobrancas)
#
# # cobrancas.to_csv('arquivos/cobrancas_import_ambar.csv', index=False)
#
