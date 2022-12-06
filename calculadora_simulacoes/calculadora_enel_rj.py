import pandas as pd
import numpy as np

# cogecom_enel_go = 0.07
# cogecom_cpfl_paulista = 0.07
# cogecom_copel_pr = 0.07
# cogecom_celesc_sc = 0.07

'''Geradores - Produtos: '''
enel_x_rj = 0.05


''' Tarifas Distribuidora:'''

'ENEL GO'

te_enel_rj = 0.30485
tusd_enel_rj = 0.49679
tarifa_sem_impostos_enel_rj = te_enel_rj + tusd_enel_rj

'TRIBUSTOS'

pis_enel_rj = 0.008
cofins_enel_rj = 0.0369
icms_enel_rj = 0.18

pis_te_enel_rj = pis_enel_rj * (te_enel_rj / (1 - pis_enel_rj - cofins_enel_rj))
# print(pis_te_enel_rj)
pis_tusd_enel_rj = pis_enel_rj * (tusd_enel_rj / (1 - pis_enel_rj - cofins_enel_rj))
# print(pis_tusd_enel_rj)

cofins_te_enel_rj = cofins_enel_rj * (te_enel_rj / (1 - pis_enel_rj - cofins_enel_rj))
# print(cofins_te_enel_rj)
cofins_tusd_enel_rj = cofins_enel_rj * (tusd_enel_rj / (1 - pis_enel_rj - cofins_enel_rj))
# print(cofins_tusd_enel_rj)
icms_te_enel_rj = icms_enel_rj * (te_enel_rj / (1 - pis_enel_rj - cofins_enel_rj) / (1 - icms_enel_rj))
# print(icms_te_enel_rj)
icms_tusd_enel_rj = (icms_enel_rj * (tusd_enel_rj / (1 - pis_enel_rj - cofins_enel_rj) / (1 - icms_enel_rj)))
# print(icms_tusd_enel_rj)

te_pis_cofins_enel_rj = te_enel_rj / (1 - (pis_enel_rj + cofins_enel_rj))
tusd_pis_cofins_enel_rj = tusd_enel_rj / (1 - (pis_enel_rj + cofins_enel_rj))

te_pis_cofins_icms_enel_rj_valor = te_pis_cofins_enel_rj / (1 - icms_enel_rj)
tusd_pis_cofins_icms_enel_rj_valor = tusd_pis_cofins_enel_rj

te_pis_cofins_enel_rj_valor = pis_te_enel_rj + cofins_te_enel_rj
tusd_pis_cofins_enel_rj_valor = pis_tusd_enel_rj + cofins_tusd_enel_rj

'Tarifa Cheia - Distribuidora'

tarifa_cheia_enel_rj_valor = tarifa_sem_impostos_enel_rj + pis_te_enel_rj + pis_tusd_enel_rj + cofins_tusd_enel_rj + cofins_te_enel_rj + icms_te_enel_rj
# print(tarifa_cheia_enel_rj_valor)
impostos_cobrados_enel_rj_valor = te_pis_cofins_enel_rj_valor + tusd_pis_cofins_enel_rj_valor
# print(impostos_cobrados_enel_rj_valor)

tarifa_aplicacao_enel_rj_valor = (te_pis_cofins_icms_enel_rj_valor + tusd_pis_cofins_icms_enel_rj_valor)
# print(tarifa_aplicacao_enel_rj_valor)
tarifa_compensavel_enel_rj_valor = tarifa_aplicacao_enel_rj_valor
# print(tarifa_compensavel_enel_rj_valor)


desconto_enel_x_rj_valor = tarifa_compensavel_enel_rj_valor * enel_x_rj
print(desconto_enel_x_rj_valor)

tarifa_enel_x_rj_valor = tarifa_compensavel_enel_rj_valor - desconto_enel_x_rj_valor
print(tarifa_enel_x_rj_valor)


tabela_enelx_rj = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Enel X'], 'Valores R$':[tarifa_sem_impostos_enel_rj, tarifa_cheia_enel_rj_valor, tarifa_aplicacao_enel_rj_valor, tarifa_compensavel_enel_rj_valor, desconto_enel_x_rj_valor, tarifa_enel_x_rj_valor]}
pd.options.display.float_format = '{:,.5f}'.format
tabela_enelx_rj = pd.DataFrame(tabela_enelx_rj)
print(tabela_enelx_rj)
#
# tabela_cotesa_rge = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cotesa'], 'Valores R$':[tarifa_sem_impostos_enel_go, tarifa_cheia_enel_go_valor, tarifa_aplicacao_cotesa_rge_valor, tarifa_compensavel_cotesa_rge_valor, desconto_cotesa_rge_valor, tarifa_cotesa_rge_valor]}
# pd.options.display.float_format = '{:,.5f}'.format
# tabela_cotesa_rge = pd.DataFrame(tabela_cotesa_rge)
# print(tabela_cotesa_rge)
#
# tabela_sinergi_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Sinergi'], 'Valores R$':[tarifa_sem_impostos_copel, tarifa_cheia_copel_valor, tarifa_aplicacao_copel_valor, tarifa_compensavel_copel_valor, desconto_sinergi_copel_valor, tarifa_sinergi_copel_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_sinergi_copel = pd.DataFrame(tabela_sinergi_copel)
# print(tabela_sinergi_copel)
