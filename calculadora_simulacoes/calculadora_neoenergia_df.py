import pandas as pd
import numpy as np


''' Distribuidoras: '''
idone_neoenergia_df = 0.10
cogecom_neoenergia_df = 0.10
crafter1_neoenergia_df = 0.07
crafter2_neoenergia_df = 0.16

''' Tarifas Distribuidora:'''

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

pis_te_neo_df = pis_neo_df * (te_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(pis_te_neo_df)
pis_tusd_neo_df = pis_neo_df * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(pis_tusd_neo_df)

cofins_te_neo_df = cofins_neo_df * (te_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(cofins_te_neo_df)
cofins_tusd_neo_df = cofins_neo_df * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df))
# print(cofins_tusd_neo_df)

icms_te_neo_df_18 = icms_neo_df_18 * (te_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_18))
# print(icms_te_neo_df_18)
icms_te_neo_df_12 = icms_neo_df_12 * (te_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_12))
# print(icms_te_neo_df_12)
icms_tusd_neo_df_18 = (icms_neo_df_18 * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_18)))
# print(icms_tusd_neo_df_18)
icms_tusd_neo_df_12 = (icms_neo_df_12 * (tusd_neo_df / (1 - pis_neo_df - cofins_neo_df) / (1 - icms_neo_df_12)))
# print(icms_tusd_neo_df_12)

te_pis_cofins_neo_df = te_neo_df / (1 - (pis_neo_df + cofins_neo_df))
# print(te_pis_cofins_neo_df)
tusd_pis_cofins_neo_df = tusd_neo_df / (1 - (pis_neo_df + cofins_neo_df))
# print(tusd_pis_cofins_neo_df)

te_pis_cofins_icms_neo_df_18_valor = te_pis_cofins_neo_df / (1 - icms_neo_df_18)
# print(te_pis_cofins_icms_neo_df_18_valor)
tusd_pis_cofins_icms_neo_df_18_valor = tusd_pis_cofins_neo_df / (1 - icms_neo_df_18)
# print(tusd_pis_cofins_icms_neo_df_18_valor)

te_pis_cofins_icms_neo_df_12_valor = te_pis_cofins_neo_df / (1 - icms_neo_df_12)
# print(te_pis_cofins_icms_neo_df_12_valor)
tusd_pis_cofins_icms_neo_df_12_valor = tusd_pis_cofins_neo_df / (1 - icms_neo_df_12)
# print(tusd_pis_cofins_icms_neo_df_12_valor)

te_pis_cofins_neo_df_valor = pis_te_neo_df + cofins_te_neo_df
# print(te_pis_cofins_neo_df_valor)
tusd_pis_cofins_neo_df_valor = pis_tusd_neo_df + cofins_tusd_neo_df
# print(tusd_pis_cofins_neo_df_valor)

tarifa_cheia_neo_df_valor = tarifa_sem_impostos_neo_df + pis_te_neo_df + pis_tusd_neo_df + cofins_tusd_neo_df + cofins_te_neo_df + icms_tusd_neo_df_18 + icms_te_neo_df_18
print(tarifa_cheia_neo_df_valor)
impostos_cobrados_neo_df_valor = te_pis_cofins_icms_neo_df_18_valor + tusd_pis_cofins_icms_neo_df_18_valor
print(impostos_cobrados_neo_df_valor)
tarifa_aplicacao_neo_df_valor = (te_pis_cofins_icms_neo_df_18_valor + tusd_pis_cofins_icms_neo_df_18_valor)
print(tarifa_aplicacao_neo_df_valor)
tarifa_compensavel_neo_df_valor = tarifa_aplicacao_neo_df_valor - impostos_cobrados_neo_df_valor
print(tarifa_compensavel_neo_df_valor)

# desconto_cogecom_copel_valor = tarifa_compensavel_copel_valor * cogecom_copel
# desconto_cotesa_copel_valor = tarifa_compensavel_cotesa_copel_valor * cotesa_copel
# desconto_sinergi_copel_valor = tarifa_compensavel_copel_valor * sinergi_copel
# tarifa_cogecom_copel_valor = tarifa_compensavel_copel_valor - desconto_cogecom_copel_valor
# tarifa_cotesa_copel_valor = tarifa_compensavel_cotesa_copel_valor - desconto_cotesa_copel_valor
# tarifa_sinergi_copel_valor = tarifa_compensavel_copel_valor - desconto_sinergi_copel_valor
#
#
# tabela_cogecom_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cogecom'], 'Valores R$':[tarifa_sem_impostos_neo_df, tarifa_cheia_copel_valor, tarifa_aplicacao_copel_valor, tarifa_compensavel_copel_valor, desconto_cogecom_copel_valor, tarifa_cogecom_copel_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_cogecom_copel = pd.DataFrame(tabela_cogecom_copel)
# print(tabela_cogecom_copel)
#
# tabela_cotesa_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cotesa'], 'Valores R$':[tarifa_sem_impostos_copel, tarifa_cheia_copel_valor, tarifa_aplicacao_cotesa_copel_valor, tarifa_compensavel_cotesa_copel_valor, desconto_cotesa_copel_valor, tarifa_cotesa_copel_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_cotesa_copel = pd.DataFrame(tabela_cotesa_copel)
# print(tabela_cotesa_copel)
#
# tabela_sinergi_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Sinergi'], 'Valores R$':[tarifa_sem_impostos_copel, tarifa_cheia_copel_valor, tarifa_aplicacao_copel_valor, tarifa_compensavel_copel_valor, desconto_sinergi_copel_valor, tarifa_sinergi_copel_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_sinergi_copel = pd.DataFrame(tabela_sinergi_copel)
# print(tabela_sinergi_copel)

