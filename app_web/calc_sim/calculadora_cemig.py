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
cegecom_cemig = 0.1


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

desconto_cemig_valor = tarifa_compensavel_cemig_valor * cegecom_cemig
tarifa_gerador_cemig_valor = tarifa_compensavel_cemig_valor - desconto_cemig_valor

tabela_cemig = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Gerador'], 'Valores R$':[tarifa_sem_impostos_cemig, tarifa_cheia_cemig_valor, tarifa_aplicacao_cemig_valor, tarifa_compensavel_cemig_valor, desconto_cemig_valor, tarifa_gerador_cemig_valor]}
pd.options.display.float_format = '{:,.4f}'.format
tabela_cemig = pd.DataFrame(tabela_cemig)
print(tabela_cemig)

