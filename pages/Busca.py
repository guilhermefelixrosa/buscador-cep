import streamlit as st

# 1. Cria a "memória" de login se ela ainda não existir
if "logado" not in st.session_state:
    st.session_state.logado = False

# 2. Cria a função que desenha a tela de login
def tela_login():
    st.title("Acesso Restrito")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password") # Oculte o texto digitado
    
    if st.button("Entrar"):
        # Verificação simples (em um app real, você checaria num banco de dados)
        if usuario == "admin" and senha == "123":
            st.session_state.logado = True
            st.rerun() # Recarrega a página para aplicar o login
        else:
            st.error("Usuário ou senha incorretos!")

# 3. Função para sair do sistema
def logout():
    st.session_state.logado = False

# 4. Configuração das suas páginas (seus outros arquivos .py)
pagina_login = st.Page(tela_login, title="Login", icon="🔒")
pagina_busca = st.Page("busca_cep.py", title="Buscar CEP", icon="📍")
pagina_sobre = st.Page("sobre.py", title="Sobre", icon="ℹ️")

# 5. Lógica de Roteamento
if not st.session_state.logado:
    # Se NÃO estiver logado, a única página que existe na navegação é o Login
    pg = st.navigation([pagina_login])
else:
    # Se ESTIVER logado, mostra as páginas reais do app
    st.sidebar.button("Sair da Conta", on_click=logout) # Botão de sair no menu lateral
    pg = st.navigation([pagina_busca, pagina_sobre])

# Executa a navegação
pg.run()