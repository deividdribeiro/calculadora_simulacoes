import pandas as pd
import numpy as np

# cogecom_enel_go = 0.07
# cogecom_cpfl_paulista = 0.07
# cogecom_copel_pr = 0.07
# cogecom_celesc_sc = 0.07

'''Geradores - Produtos: '''
bc_energia_10 = 0.10
bc_energia_14 = 0.14
bc_energia_16 = 0.16
bc_energia_18 = 0.18
cogecom_enel_go = 0.07


''' Tarifas Distribuidora:'''

'ENEL GO'

te_enel_go = 0.2616
tusd_enel_go = 0.4375
tarifa_sem_impostos_enel_go = te_enel_go + tusd_enel_go

'TRIBUSTOS'

pis_enel_go = 0.02
cofins_enel_go = 0.03
icms_enel_go = 0.18

pis_te_enel_go = pis_enel_go * (te_enel_go / (1 - pis_enel_go - cofins_enel_go))
pis_tusd_enel_go = pis_enel_go * (tusd_enel_go / (1 - pis_enel_go - cofins_enel_go))

cofins_te_enel_go = cofins_enel_go * (te_enel_go / (1 - pis_enel_go - cofins_enel_go))
cofins_tusd_enel_go = cofins_enel_go * (tusd_enel_go / (1 - pis_enel_go - cofins_enel_go))

icms_te_enel_go = icms_enel_go * (te_enel_go / (1 - pis_enel_go - cofins_enel_go) / (1 - icms_enel_go))
icms_tusd_enel_go = (icms_enel_go * (tusd_enel_go / (1 - pis_enel_go - cofins_enel_go) / (1 - icms_enel_go)))

te_pis_cofins_enel_go = te_enel_go / (1 - (pis_enel_go + cofins_enel_go))
tusd_pis_cofins_enel_go = tusd_enel_go / (1 - (pis_enel_go + cofins_enel_go))

te_pis_cofins_icms_enel_go_valor = te_pis_cofins_enel_go / (1 - icms_enel_go)
tusd_pis_cofins_icms_enel_go_valor = tusd_pis_cofins_enel_go

te_pis_cofins_enel_go_valor = pis_te_enel_go + cofins_te_enel_go
tusd_pis_cofins_enel_go_valor = pis_tusd_enel_go + cofins_tusd_enel_go

'Tarifa Cheia - Distribuidora'

tarifa_cheia_enel_go_valor = tarifa_sem_impostos_enel_go + pis_te_enel_go + pis_tusd_enel_go + cofins_tusd_enel_go + cofins_te_enel_go + icms_tusd_enel_go + icms_te_enel_go
impostos_cobrados_enel_go_valor = te_pis_cofins_enel_go_valor + tusd_pis_cofins_enel_go_valor

tarifa_aplicacao_enel_go_valor = (te_pis_cofins_icms_enel_go_valor + tusd_pis_cofins_icms_enel_go_valor) * 0
tarifa_aplicacao_bc_enel_go_valor = tarifa_cheia_enel_go_valor
tarifa_compensavel_bc_enel_go_valor = tarifa_aplicacao_bc_enel_go_valor
tarifa_compensavel_enel_go_valor = tarifa_sem_impostos_enel_go

# print(tarifa_aplicacao_enel_go_valor)
print(tarifa_aplicacao_bc_enel_go_valor)
# print(tarifa_compensavel_bc_enel_go_valor)
# print(tarifa_compensavel_enel_go_valor)


# desconto_cogecom_rge_valor = tarifa_compensavel_rge_valor * cogecom_rge
# desconto_cotesa_rge_valor = tarifa_compensavel_cotesa_rge_valor * cotesa_rge
#
# tarifa_cogecom_rge_valor = tarifa_compensavel_rge_valor - desconto_cogecom_rge_valor
# tarifa_cotesa_rge_valor = tarifa_compensavel_cotesa_rge_valor - desconto_cotesa_rge_valor
#
# tabela_cogecom_rge = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cogecom'], 'Valores R$':[tarifa_sem_impostos_enel_go, tarifa_cheia_enel_go_valor, tarifa_aplicacao_rge_valor, tarifa_compensavel_rge_valor, desconto_cogecom_rge_valor, tarifa_cogecom_rge_valor]}
# pd.options.display.float_format = '{:,.5f}'.format
# tabela_cogecom_rge = pd.DataFrame(tabela_cogecom_rge)
# print(tabela_cogecom_rge)
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

