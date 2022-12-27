import pandas as pd
import numpy as np

# cogecom_rge = 0.07
# cogecom_enel_go = 0.07
# cogecom_cpfl_paulista = 0.07
# cogecom_copel_pr = 0.07
# cogecom_celesc_sc = 0.07

''' Distribuidoras: '''
ambar = 0.10
gd_solar = 0.10
gd_solar_p = 0.15



''' Tarifas Distribuidora:'''

'CPFL PAULISTA - SP'

te_cpfl_paulista = 0.29592
tusd_cpfl_paulista = 0.36599
tarifa_sem_impostos_cpfl_paulista = te_cpfl_paulista + tusd_cpfl_paulista
# print(tarifa_sem_impostos_cpfl_paulista)

'TRIBUSTOS'

pis_cpfl_paulista = 0.015
cofins_cpfl_paulista = 0.0435
icms_cpfl_paulista = 0.18

pis_te_cpfl_paulista = pis_cpfl_paulista * (te_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(pis_te_cpfl_paulista)
pis_tusd_cpfl_paulista = pis_cpfl_paulista * (tusd_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(pis_tusd_cpfl_paulista)

cofins_te_cpfl_paulista = cofins_cpfl_paulista * (te_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(cofins_te_cpfl_paulista)
cofins_tusd_cpfl_paulista = cofins_cpfl_paulista * (tusd_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista))
# print(cofins_tusd_cpfl_paulista)

icms_te_cpfl_paulista = icms_cpfl_paulista * (te_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista) / (1 - icms_cpfl_paulista))
# print(icms_te_cpfl_paulista)
icms_tusd_cpfl_paulista = (icms_cpfl_paulista * (tusd_cpfl_paulista / (1 - pis_cpfl_paulista - cofins_cpfl_paulista) / (1 - icms_cpfl_paulista))) * 0
# print(icms_tusd_cpfl_paulista)
te_pis_cofins_cpfl_paulista = te_cpfl_paulista / (1 - (pis_cpfl_paulista + cofins_cpfl_paulista))
# print(te_pis_cofins_cpfl_paulista)
tusd_pis_cofins_cpfl_paulista = tusd_cpfl_paulista / (1 - (pis_cpfl_paulista + cofins_cpfl_paulista))
# print(tusd_pis_cofins_cpfl_paulista)

te_pis_cofins_icms_cpfl_paulista_valor = te_pis_cofins_cpfl_paulista / (1 - icms_cpfl_paulista)
# print(te_pis_cofins_icms_cpfl_paulista_valor)
tusd_pis_cofins_icms_cpfl_paulista_valor = tusd_pis_cofins_cpfl_paulista
# print(tusd_pis_cofins_icms_cpfl_paulista_valor)

# te_pis_cofins_cpfl_paulista_valor = pis_te_cpfl_paulista + cofins_te_cpfl_paulista
# tusd_pis_cofins_cpfl_paulista_valor = pis_tusd_cpfl_paulista + cofins_tusd_cpfl_paulista

tarifa_cheia_cpfl_paulista_valor = tarifa_sem_impostos_cpfl_paulista + pis_te_cpfl_paulista + pis_tusd_cpfl_paulista + cofins_tusd_cpfl_paulista + cofins_te_cpfl_paulista + icms_tusd_cpfl_paulista + icms_te_cpfl_paulista
# print(tarifa_cheia_cpfl_paulista_valor)
impostos_cobrados_cpfl_paulista_valor = tarifa_cheia_cpfl_paulista_valor - tarifa_sem_impostos_cpfl_paulista
# print(impostos_cobrados_cpfl_paulista_valor)
tarifa_aplicacao_cpfl_paulista_valor = te_pis_cofins_icms_cpfl_paulista_valor + tusd_pis_cofins_icms_cpfl_paulista_valor
# print(tarifa_aplicacao_cpfl_paulista_valor)
tarifa_compensavel_cpfl_paulista_valor = tarifa_aplicacao_cpfl_paulista_valor - impostos_cobrados_cpfl_paulista_valor
tarifa_compensavel_gd_solar_cpfl_paulista_valor = tarifa_cheia_cpfl_paulista_valor
# print(tarifa_compensavel_cpfl_paulista_valor)

desconto_ambar_cpfl_paulista_valor = tarifa_compensavel_cpfl_paulista_valor * ambar
desconto_gd_solar_cpfl_paulista_valor = tarifa_compensavel_gd_solar_cpfl_paulista_valor * gd_solar
desconto_gd_solar_p_cpfl_paulista_valor = tarifa_compensavel_gd_solar_cpfl_paulista_valor * gd_solar_p

tarifa_ambar_cpfl_paulista_valor = tarifa_compensavel_cpfl_paulista_valor - desconto_ambar_cpfl_paulista_valor
tarifa_gd_solar_cpfl_paulista_valor = tarifa_compensavel_gd_solar_cpfl_paulista_valor - desconto_gd_solar_cpfl_paulista_valor
tarifa_gd_solar_p_cpfl_paulista_valor = tarifa_compensavel_gd_solar_cpfl_paulista_valor - desconto_gd_solar_p_cpfl_paulista_valor

tabela_ambar_cpfl_paulista = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa Ambar'], 'Valores R$':[tarifa_sem_impostos_cpfl_paulista, tarifa_cheia_cpfl_paulista_valor, tarifa_aplicacao_cpfl_paulista_valor, tarifa_compensavel_cpfl_paulista_valor, desconto_ambar_cpfl_paulista_valor, tarifa_ambar_cpfl_paulista_valor]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_ambar_cpfl_paulista = pd.DataFrame(tabela_ambar_cpfl_paulista)
print(tabela_ambar_cpfl_paulista)

tabela_gd_solar_cpfl_paulista = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa GD Solar'], 'Valores R$':[tarifa_sem_impostos_cpfl_paulista, tarifa_cheia_cpfl_paulista_valor, tarifa_aplicacao_cpfl_paulista_valor, tarifa_compensavel_gd_solar_cpfl_paulista_valor, desconto_gd_solar_cpfl_paulista_valor, tarifa_gd_solar_cpfl_paulista_valor]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_gd_solar_cpfl_paulista = pd.DataFrame(tabela_gd_solar_cpfl_paulista)
print(tabela_gd_solar_cpfl_paulista)

tabela_gd_solar_p_cpfl_paulista = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto Efetivo', 'Tarifa GD Solar Posto'], 'Valores R$':[tarifa_sem_impostos_cpfl_paulista, tarifa_cheia_cpfl_paulista_valor, tarifa_aplicacao_cpfl_paulista_valor, tarifa_compensavel_gd_solar_cpfl_paulista_valor, desconto_gd_solar_p_cpfl_paulista_valor, tarifa_gd_solar_p_cpfl_paulista_valor]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_gd_solar_p_cpfl_paulista = pd.DataFrame(tabela_gd_solar_p_cpfl_paulista)
print(tabela_gd_solar_p_cpfl_paulista)
