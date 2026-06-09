import streamlit as st
import requests

#st.title("Minha Primeira Aplicação Streamlit 🚀")
#st.write("Bem-vindo! O ambiente está configurado perfeitamente.")

st.title("📍 Buscador de CEP")
st.write("Digite um CEP para encontrar o endereço completo em tempo real.")

st.set_page_config(page_title="Buscador de CEP", page_icon="🎈")

cep_usuario = st.text_input("Digite o CEP (apenas números):", max_chars=8)

if st.button("Buscar Endereço"):

    if len(cep_usuario) == 8 and cep_usuario.isdigit():

        with st.spinner("Buscando informações na API..."):
            try:

                url = f"https://viacep.com.br/ws/{cep_usuario}/json/"
                resposta = requests.get(url)
                dados = resposta.json()

                if "erro" in dados:
                    st.error("CEP não encontrado. Verifique os números.")
                else:
                    st.success("Endereço localizado com sucesso!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(label="Cidade", value=dados.get("localidade"))
                        st.text(f"Logradouro: {dados.get('logradouro')}")
                        st.text(f"Bairro: {dados.get('bairro')}")

                    with col2:
                        st.metric(label="Estado (UF)", value=dados.get("uf"))
                        st.text(f"DDD: {dados.get('ddd')}")
                        st.text(f"Código IBGE: {dados.get('ibge')}")
            
            except Exception as e:
                st.error("Erro ao conectar com o serviço de CEP. Tente novamente mais tarde.")
    else:
        st.warning("Por favor, digite um CEP válido contendo exatamente 8 números.")