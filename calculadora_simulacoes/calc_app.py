import streamlit as st


from calculadora_cemig import tarifa_cogecom_claro_cemig_valor, tarifa_solatio_cemig_valor
from calculadora_copel import tarifa_sinergi_copel_valor, tarifa_cogecom_copel_valor

st.title('Simulador de Desconto APP v.1')
st.write('---')

copel = tarifa_cogecom_copel_valor
cemig_claro = tarifa_cogecom_claro_cemig_valor
cemig = tarifa_solatio_cemig_valor



kWh = st.number_input(label="Insira o kWh consumido na fatura da DISTRIBUIDORA")

st.write('Distribuidoras:')

distribuidora = st.radio("Escolha uma distribuidora:", ('COPEL-PR', 'CEMIG-MG', 'CEMIG-MG (CLARO)'))

ans = 0

def calculadora():
    if distribuidora == 'COPEL-PR':
        ans = kWh * copel
    elif distribuidora == 'CEMIG-MG':
        ans = kWh * cemig
    elif distribuidora == 'CEMIG-MG (CLARO)':
        ans = kWh * cemig_claro

    st.success(f'Valor do Boleto: {ans}')

if st.button('Calcular desconto'):
    calculadora()
