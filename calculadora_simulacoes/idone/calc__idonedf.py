import pandas as pd

''' Produto '''

idone = 0.10

'NEOENERGIA - DF'

te_neo_df = 0.35303
tusd_neo_df = 0.34568
tarifa_sem_impostos_neo_df = te_neo_df + tusd_neo_df
# print(tarifa_sem_impostos_neo_df)

'TRIBUSTOS'

pis_neo_df = 0.015
cofins_neo_df = 0.071
icms_neo_df_18 = 0.18
icms_neo_df_12 = 0.12

'PIS'

pis_te_neo_df = pis_neo_df * (te_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(pis_te_neo_df)
pis_tusd_neo_df = pis_neo_df * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(pis_tusd_neo_df)

'COFINS'

cofins_te_neo_df = cofins_neo_df * (te_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(cofins_te_neo_df)
cofins_tusd_neo_df = cofins_neo_df * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(cofins_tusd_neo_df)

'ICMS 18% - ISENTA ICMS NA TUSD?'

icms_te_neo_df_18 = icms_neo_df_18 * (te_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_18))
# print(icms_te_neo_df_18)
icms_tusd_neo_df_18 = (icms_neo_df_18 * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_18)))
# print(icms_tusd_neo_df_18)


'ICMS 12% - ISENTA ICMS NA TUSD?'

icms_te_neo_df_12 = icms_neo_df_12 * (te_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_12))
# print(icms_te_neo_df_12)
icms_tusd_neo_df_12 = (icms_neo_df_12 * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_12)))
# print(icms_tusd_neo_df_12)

'PISCOFINS'

te_pis_cofins_neo_df = te_neo_df / (1 - (pis_neo_df + cofins_neo_df))
# print(te_pis_cofins_neo_df)
tusd_pis_cofins_neo_df = tusd_neo_df / (1 - (pis_neo_df + cofins_neo_df))
# print(tusd_pis_cofins_neo_df)

'PISCOFINS + ICMS 18%'

te_pis_cofins_icms_neo_df_18_valor = te_pis_cofins_neo_df / (1 - icms_neo_df_18)
# print(te_pis_cofins_icms_neo_df_18_valor)
tusd_pis_cofins_icms_neo_df_18_valor = tusd_pis_cofins_neo_df / (1 - icms_neo_df_18)
# print(tusd_pis_cofins_icms_neo_df_18_valor)

'PISCOFINS + ICMS 12%'

te_pis_cofins_icms_neo_df_12_valor = te_pis_cofins_neo_df / (1 - icms_neo_df_12)
# print(te_pis_cofins_icms_neo_df_12_valor)
tusd_pis_cofins_icms_neo_df_12_valor = tusd_pis_cofins_neo_df / (1 - icms_neo_df_12)
# print(tusd_pis_cofins_icms_neo_df_12_valor)

'TARIFAS NEOENERGIA DF - COM ICMS 18%'

tarifa_cheia_neodf_icms18 = tarifa_sem_impostos_neo_df + pis_te_neo_df + pis_tusd_neo_df + cofins_tusd_neo_df + cofins_te_neo_df + icms_tusd_neo_df_18 + icms_te_neo_df_18
# print(tarifa_cheia_neodf_icms18)
impostos_cobrados_neodf_icms18 = tarifa_cheia_neodf_icms18 - tarifa_sem_impostos_neo_df
# print(impostos_cobrados_neodf_icms18)
tarifa_aplicacao_neodf_icms18 = (te_pis_cofins_icms_neo_df_18_valor + tusd_pis_cofins_icms_neo_df_18_valor)
# print(tarifa_aplicacao_neodf_icms18)
tarifa_compensavel_neodf_icms18 = tarifa_aplicacao_neodf_icms18 - impostos_cobrados_neodf_icms18
# print(tarifa_compensavel_neodf_icms18)

'TARIFAS NEOENERGIA DF - COM ICMS 12%'

tarifa_cheia_neodf_icms12 = tarifa_sem_impostos_neo_df + pis_te_neo_df + pis_tusd_neo_df + cofins_tusd_neo_df + cofins_te_neo_df + icms_tusd_neo_df_12 + icms_te_neo_df_12
# print(tarifa_cheia_neodf_icms12)
impostos_cobrados_neodf_icms12 = tarifa_cheia_neodf_icms12 - tarifa_sem_impostos_neo_df
# print(impostos_cobrados_neodf_icms12)
tarifa_aplicacao_neodf_icms12 = (te_pis_cofins_icms_neo_df_12_valor + tusd_pis_cofins_icms_neo_df_12_valor)
# print(tarifa_aplicacao_neodf_icms12)
tarifa_compensavel_neodf_icms12 = tarifa_aplicacao_neodf_icms12 - impostos_cobrados_neodf_icms12
# print(tarifa_compensavel_neodf_icms12)

'CALCULO VALOR DO DESCONTO - ICMS 18%'

desconto_idone_neodf18 = tarifa_compensavel_neodf_icms18 * idone
# print('Valor do Desconto: R$', desconto_idone_neodf18)

'CALCULO DA TARIFA DO GERADOR - ICMS 18%'

tarifa_idone_neodf18 = tarifa_compensavel_neodf_icms18 - desconto_idone_neodf18
# print('Valor da Tarifa do Gerador: R$', tarifa_idone_neodf)

'CALCULO VALOR DO DESCONTO - ICMS 12%'

desconto_idone_neodf12 = tarifa_compensavel_neodf_icms12 * idone
# print('Valor do Desconto: R$', desconto_idone_neodf12)

'CALCULO DA TARIFA DO GERADOR - ICMS 18%'

tarifa_idone_neodf12 = tarifa_compensavel_neodf_icms12 - desconto_idone_neodf12
# print('Valor da Tarifa do Gerador: R$', tarifa_idone_neodf12)

tabela_idone18 = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia ICMS 18%', 'Tarifa Aplicação ICMS 18%', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa Ambar'], 'Valores R$':[tarifa_sem_impostos_neo_df, tarifa_cheia_neodf_icms18, tarifa_aplicacao_neodf_icms18, tarifa_compensavel_neodf_icms18, desconto_idone_neodf18, tarifa_idone_neodf18]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_ambar_cpfl_paulista = pd.DataFrame(tabela_idone18)
print(tabela_idone18)

tabela_idone12 = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia ICMS 12%', 'Tarifa Aplicação ICMS 12%', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa Ambar'], 'Valores R$':[tarifa_sem_impostos_neo_df, tarifa_cheia_neodf_icms12, tarifa_aplicacao_neodf_icms12, tarifa_compensavel_neodf_icms12, desconto_idone_neodf12, tarifa_idone_neodf12]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_ambar_cpfl_paulista = pd.DataFrame(tabela_idone12)
print(tabela_idone12)

'Dados para Gerar a Cobrança'

kWh_injetado = 100
kWh_consumido_dist = 100
valor_kWh_calc = tarifa_cheia_neodf_icms18 * kWh_consumido_dist
valor_kWh_fatura = 1500
quanto_seria_valor = kWh_injetado * (valor_kWh_fatura/kWh_consumido_dist)

