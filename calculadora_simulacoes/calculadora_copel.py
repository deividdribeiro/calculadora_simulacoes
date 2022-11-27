import pandas as pd
import numpy as np

# cogecom_rge = 0.07
# cogecom_enel_go = 0.07
# cogecom_cpfl_paulista = 0.07
# cogecom_copel_pr = 0.07
# cogecom_celesc_sc = 0.07

def calculadora_copel():

    ''' Distribuidoras: '''
    cotesa_copel = 0.10
    cogecom_copel = 0.07
    sinergi_copel = 0.07


    ''' Tarifas Distribuidora:'''

    'COPEL'

    te_copel = 0.25894
    tusd_copel = 0.31080
    tarifa_sem_impostos_copel = te_copel + tusd_copel

    'TRIBUSTOS'

    pis_copel = 0.02
    cofins_copel = 0.03
    icms_copel = 0.18

    pis_te_copel = pis_copel * (te_copel / (1 - pis_copel - cofins_copel))
    pis_tusd_copel = pis_copel * (tusd_copel / (1 - pis_copel - cofins_copel))

    cofins_te_copel = cofins_copel * (te_copel / (1 - pis_copel - cofins_copel))
    cofins_tusd_copel = cofins_copel * (tusd_copel / (1 - pis_copel - cofins_copel))

    icms_te_copel = icms_copel * (te_copel / (1 - pis_copel - cofins_copel) / (1 - icms_copel))
    icms_tusd_copel = (icms_copel * (tusd_copel / (1 - pis_copel - cofins_copel) / (1 - icms_copel)))

    te_pis_cofins_copel = te_copel / (1 - (pis_copel + cofins_copel))
    tusd_pis_cofins_copel = tusd_copel / (1 - (pis_copel + cofins_copel))

    te_pis_cofins_icms_copel_valor = te_pis_cofins_copel / (1 - icms_copel)
    tusd_pis_cofins_icms_copel_valor = tusd_pis_cofins_copel

    te_pis_cofins_copel_valor = pis_te_copel + cofins_te_copel
    tusd_pis_cofins_copel_valor = pis_tusd_copel + cofins_tusd_copel

    tarifa_cheia_copel_valor = tarifa_sem_impostos_copel + pis_te_copel + pis_tusd_copel + cofins_tusd_copel + cofins_te_copel + icms_tusd_copel + icms_te_copel
    impostos_cobrados_copel_valor = te_pis_cofins_copel_valor + tusd_pis_cofins_copel_valor
    tarifa_aplicacao_copel_valor = (te_pis_cofins_icms_copel_valor + tusd_pis_cofins_icms_copel_valor)*0
    tarifa_aplicacao_cotesa_copel_valor = tarifa_cheia_copel_valor
    tarifa_compensavel_cotesa_copel_valor = tarifa_aplicacao_cotesa_copel_valor
    tarifa_compensavel_copel_valor = tarifa_sem_impostos_copel

    desconto_cogecom_copel_valor = tarifa_compensavel_copel_valor * cogecom_copel
    desconto_cotesa_copel_valor = tarifa_compensavel_cotesa_copel_valor * cotesa_copel
    desconto_sinergi_copel_valor = tarifa_compensavel_copel_valor * sinergi_copel
    tarifa_cogecom_copel_valor = tarifa_compensavel_copel_valor - desconto_cogecom_copel_valor
    tarifa_cotesa_copel_valor = tarifa_compensavel_cotesa_copel_valor - desconto_cotesa_copel_valor
    tarifa_sinergi_copel_valor = tarifa_compensavel_copel_valor - desconto_sinergi_copel_valor

    # tabela_cogecom_copel = {'Itens': ['Tarifa Sem Impostos', 'Tarifa Cheia', 'Tarifa Aplicação', 'Tarifa Compensavel', 'Desconto', 'Tarifa Cogecom'], 'Valores R$':[tarifa_sem_impostos_copel, tarifa_cheia_copel_valor, tarifa_aplicacao_copel_valor, tarifa_compensavel_copel_valor, desconto_cogecom_copel_valor, tarifa_cogecom_copel_valor]}
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

if __name__ == '__main__':
    calculadora_copel()