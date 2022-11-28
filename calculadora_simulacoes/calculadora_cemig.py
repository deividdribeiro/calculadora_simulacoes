import pandas as pd
import numpy as np

# cogecom_rge = 0.07
# cogecom_enel_go = 0.07
# cogecom_cpfl_paulista = 0.07
# cogecom_copel_pr = 0.07
# cogecom_celesc_sc = 0.07

''' Distribuidoras: '''
edp_cemig = 0.15
solatio_cemig = 0.15
solatio_claro_cemig = 0.10
cogecom_claro_cemig = 0.1
cogecom_cemig = 0.15


''' Tarifas Distribuidora:'''

'CEMIG - MG'

te_cemig = 0.24400
tusd_cemig = 0.40913
tarifa_sem_impostos_cemig = te_cemig + tusd_cemig

'TRIBUSTOS'

pis_cemig = 0.02
cofins_cemig = 0.03
icms_cemig = 0.18

pis_te_cemig = pis_cemig * (te_cemig /(1 - pis_cemig - cofins_cemig))
pis_tusd_cemig = pis_cemig * (tusd_cemig /(1 - pis_cemig - cofins_cemig))

cofins_te_cemig = cofins_cemig * (te_cemig /(1 - pis_cemig - cofins_cemig))
cofins_tusd_cemig = cofins_cemig * (tusd_cemig /(1 - pis_cemig - cofins_cemig))

icms_te_cemig = icms_cemig * (te_cemig / (1 - pis_cemig - cofins_cemig) / (1 - icms_cemig))
icms_tusd_cemig = (icms_cemig * (tusd_cemig / (1 - pis_cemig - cofins_cemig) / (1 - icms_cemig)))

te_pis_cofins_cemig = te_cemig / (1-(pis_cemig+cofins_cemig))
tusd_pis_cofins_cemig = tusd_cemig / (1-(pis_cemig+cofins_cemig))

te_pis_cofins_icms_cemig_valor = te_pis_cofins_cemig / (1-icms_cemig)
tusd_pis_cofins_icms_cemig_valor = tusd_pis_cofins_cemig

te_pis_cofins_cemig_valor = pis_te_cemig + cofins_te_cemig
tusd_pis_cofins_cemig_valor = pis_tusd_cemig + cofins_tusd_cemig

tarifa_cheia_cemig_valor = tarifa_sem_impostos_cemig + pis_te_cemig + pis_tusd_cemig + cofins_tusd_cemig + cofins_te_cemig + icms_tusd_cemig + icms_te_cemig
impostos_cobrados_cemig_valor = te_pis_cofins_cemig_valor + tusd_pis_cofins_cemig_valor
tarifa_aplicacao_cemig_valor = te_pis_cofins_icms_cemig_valor + tusd_pis_cofins_icms_cemig_valor
tarifa_compensavel_cemig_valor = tarifa_aplicacao_cemig_valor - impostos_cobrados_cemig_valor

desconto_cogecom_cemig_valor = tarifa_compensavel_cemig_valor * cogecom_cemig
desconto_cogecom_claro_cemig_valor = tarifa_compensavel_cemig_valor * cogecom_claro_cemig
desconto_edp_cemig_valor = tarifa_compensavel_cemig_valor * edp_cemig
desconto_solatio_cemig_valor = tarifa_compensavel_cemig_valor * solatio_cemig
desconto_solatio_claro_cemig_valor = tarifa_compensavel_cemig_valor * solatio_claro_cemig
tarifa_cogecom_cemig_valor = tarifa_compensavel_cemig_valor - desconto_cogecom_cemig_valor
tarifa_cogecom_claro_cemig_valor = tarifa_compensavel_cemig_valor - desconto_cogecom_claro_cemig_valor
tarifa_edp_cemig_valor = tarifa_compensavel_cemig_valor - desconto_edp_cemig_valor
tarifa_solatio_cemig_valor = tarifa_compensavel_cemig_valor - desconto_solatio_cemig_valor
tarifa_solatio_claro_cemig_valor = tarifa_compensavel_cemig_valor - desconto_solatio_claro_cemig_valor

# tabela_cogecom_cemig = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cogecom'], 'Valores R$':[tarifa_sem_impostos_cemig, tarifa_cheia_cemig_valor, tarifa_aplicacao_cemig_valor, tarifa_compensavel_cemig_valor, desconto_cogecom_cemig_valor, tarifa_cogecom_cemig_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_cogecom_cemig = pd.DataFrame(tabela_cogecom_cemig)
# print(tabela_cogecom_cemig)
#
# tabela_cogecom_claro_cemig = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto Claro', 'Tarifa Cogecom Claro'], 'Valores R$':[tarifa_sem_impostos_cemig, tarifa_cheia_cemig_valor, tarifa_aplicacao_cemig_valor, tarifa_compensavel_cemig_valor, desconto_cogecom_claro_cemig_valor, tarifa_cogecom_claro_cemig_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_cogecom_claro_cemig = pd.DataFrame(tabela_cogecom_claro_cemig)
# print(tabela_cogecom_claro_cemig)
#
# tabela_edp_cemig = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa EDP'], 'Valores R$':[tarifa_sem_impostos_cemig, tarifa_cheia_cemig_valor, tarifa_aplicacao_cemig_valor, tarifa_compensavel_cemig_valor, desconto_edp_cemig_valor, tarifa_edp_cemig_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_edp_cemig = pd.DataFrame(tabela_edp_cemig)
# print(tabela_edp_cemig)
#
# tabela_solatio_cemig = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Solatio'], 'Valores R$':[tarifa_sem_impostos_cemig, tarifa_cheia_cemig_valor, tarifa_aplicacao_cemig_valor, tarifa_compensavel_cemig_valor, desconto_solatio_cemig_valor, tarifa_solatio_cemig_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_solatio_cemig = pd.DataFrame(tabela_solatio_cemig)
# print(tabela_solatio_cemig)
#
# tabela_solatio_claro_cemig = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto Claro', 'Tarifa Solatio Claro'], 'Valores R$':[tarifa_sem_impostos_cemig, tarifa_cheia_cemig_valor, tarifa_aplicacao_cemig_valor, tarifa_compensavel_cemig_valor, desconto_solatio_claro_cemig_valor, tarifa_solatio_claro_cemig_valor]}
# pd.options.display.float_format = '{:,.4f}'.format
# tabela_solatio_claro_cemig = pd.DataFrame(tabela_solatio_claro_cemig)
# print(tabela_solatio_claro_cemig)
