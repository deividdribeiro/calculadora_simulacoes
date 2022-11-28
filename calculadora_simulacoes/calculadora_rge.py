import pandas as pd
import numpy as np

# cogecom_enel_go = 0.07
# cogecom_cpfl_paulista = 0.07
# cogecom_copel_pr = 0.07
# cogecom_celesc_sc = 0.07

'''Geradores - Produtos: '''
cogecom_rge = 0.07
cotesa_rge = 0.1


''' Tarifas Distribuidora:'''

'COPEL'

te_rge = 0.2616
tusd_rge = 0.4375
tarifa_sem_impostos_rge = te_rge + tusd_rge

'TRIBUSTOS'

pis_rge = 0.02
cofins_rge = 0.03
icms_rge = 0.18

pis_te_rge = pis_rge * (te_rge / (1 - pis_rge - cofins_rge))
pis_tusd_rge = pis_rge * (tusd_rge / (1 - pis_rge - cofins_rge))

cofins_te_rge = cofins_rge * (te_rge / (1 - pis_rge - cofins_rge))
cofins_tusd_rge = cofins_rge * (tusd_rge / (1 - pis_rge - cofins_rge))

icms_te_rge = icms_rge * (te_rge / (1 - pis_rge - cofins_rge) / (1 - icms_rge))
icms_tusd_rge = (icms_rge * (tusd_rge / (1 - pis_rge - cofins_rge) / (1 - icms_rge)))

te_pis_cofins_rge = te_rge / (1 - (pis_rge + cofins_rge))
tusd_pis_cofins_rge = tusd_rge / (1 - (pis_rge + cofins_rge))

te_pis_cofins_icms_rge_valor = te_pis_cofins_rge / (1 - icms_rge)
tusd_pis_cofins_icms_rge_valor = tusd_pis_cofins_rge

te_pis_cofins_rge_valor = pis_te_rge + cofins_te_rge
tusd_pis_cofins_rge_valor = pis_tusd_rge + cofins_tusd_rge

'Tarifa Cheia - Distribuidora'

tarifa_cheia_rge_valor = tarifa_sem_impostos_rge + pis_te_rge + pis_tusd_rge + cofins_tusd_rge + cofins_te_rge + icms_tusd_rge + icms_te_rge
impostos_cobrados_rge_valor = te_pis_cofins_rge_valor + tusd_pis_cofins_rge_valor

tarifa_aplicacao_rge_valor = (te_pis_cofins_icms_rge_valor + tusd_pis_cofins_icms_rge_valor) * 0
tarifa_aplicacao_cotesa_rge_valor = tarifa_cheia_rge_valor
tarifa_compensavel_cotesa_rge_valor = tarifa_aplicacao_cotesa_rge_valor
tarifa_compensavel_rge_valor = tarifa_sem_impostos_rge

desconto_cogecom_rge_valor = tarifa_compensavel_rge_valor * cogecom_rge
desconto_cotesa_rge_valor = tarifa_compensavel_cotesa_rge_valor * cotesa_rge

tarifa_cogecom_rge_valor = tarifa_compensavel_rge_valor - desconto_cogecom_rge_valor
tarifa_cotesa_rge_valor = tarifa_compensavel_cotesa_rge_valor - desconto_cotesa_rge_valor


tabela_cogecom_rge = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cogecom'], 'Valores R$':[tarifa_sem_impostos_rge, tarifa_cheia_rge_valor, tarifa_aplicacao_rge_valor, tarifa_compensavel_rge_valor, desconto_cogecom_rge_valor, tarifa_cogecom_rge_valor]}
pd.options.display.float_format = '{:,.5f}'.format
tabela_cogecom_rge = pd.DataFrame(tabela_cogecom_rge)
print(tabela_cogecom_rge)

tabela_cotesa_rge = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cotesa'], 'Valores R$':[tarifa_sem_impostos_rge, tarifa_cheia_rge_valor, tarifa_aplicacao_cotesa_rge_valor, tarifa_compensavel_cotesa_rge_valor, desconto_cotesa_rge_valor, tarifa_cotesa_rge_valor]}
pd.options.display.float_format = '{:,.5f}'.format
tabela_cotesa_rge = pd.DataFrame(tabela_cotesa_rge)
print(tabela_cotesa_rge)
#
# tabela_sinergi_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Sinergi'], 'Valores R$':[tarifa_sem_impostos_copel, tarifa_cheia_copel_valor, tarifa_aplicacao_copel_valor, tarifa_compensavel_copel_valor, desconto_sinergi_copel_valor, tarifa_sinergi_copel_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_sinergi_copel = pd.DataFrame(tabela_sinergi_copel)
# print(tabela_sinergi_copel)

