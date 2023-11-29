import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agenda de Contatos")

with st.container():
    st.title("Agenda de Contatos")
    st.write('---')
with st.container():
    opc = st.sidebar.selectbox("Outras opções:", ("Buscar contato", "Enviar email",))
    if opc == "Buscar contato":
        st.subheader("Buscar")
        st.text_input("Digite o nome de um contato para buscar:")
with st.container():
    st.subheader("Adicionar novo contato:")
    nome = st.text_input("Nome:")
    numero = st.text_input("Número:", help="(00) 00000-0000")
    categoria = st.selectbox("Categoria:", ["Familiares", "Amigos", "Conhecidos"])
    if st.button("Salvar", help="Clique aqui para salvar"):
        st.write("Contato salvo")
with st.container():
    st.subheader("Remover contato:")
    nome_remove = st.text_input("Nome do contato a ser removido:")
    if st.button('Remover', help="Clique aqui para remover"):
        st.write("Contato removido")


'''
#parteroberth
class contato:
    def __init__(self, nome, numero, categoria):
        self.nome = nome
        self.numero = numero
        self.categoria = categoria
        self.proximo = None
        self.anterior = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserção(self, nome, numero, categoria):
        novo_contato = contato(nome, numero, categoria)
        novo_contato.proximo = self.cabeca
        if self.cabeca:
            self.cabeca.anterior = novo_contato
        else:
            self.cauda = novo_contato
        self.cabeca = novo_contato


    def deletar_final(self):
        if not self.cabeca:
            return
        if not self.cabeca.proximo:
            self.cabeca = None
            self.cauda = None
            return
        self.cauda.anterior.proximo = None
        self.cauda = self.cauda.anterior

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.nome,atual.numero,atual.categoria)
            atual = atual.proximo


# operaçoes
lista = Listacontatos()

#inseçoes
print("quantas inserçoes?")
vezes_inserção = int(input())
for i in range(vezes_inserção):
    nome, numero , categoria = input().split(",")
    numero = int(numero)
    lista.inserção(nome, numero, categoria)

#deleção
print("quantas deleçoes?")
vezes_deleçoes = int(input())
for i in range(vezes_deleçoes):
    lista.deletar_final()

#travessia
print("Travessia após deleções:")
lista.travessia()
'''



#codigo com armazenamento


'''import streamlit as st

class contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.proximo = None
        self.anterior = None

class Listacontatos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_no_final(self, nome, numero):
        novo_no = contato(nome, numero)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

def main():
    st.title("Lista de contatos")

    # Use o cache do Streamlit para persistir a lista dupla entre as chamadas
    @st.cache(allow_output_mutation=True)
    def obter_ou_criar_lista():
        return Listacontatos()

    lista_dupla = obter_ou_criar_lista()

    # Interface para adicionar dados à lista dupla
    novo_nome = st.text_input("Digite um novo nome:")
    novo_numero = st.text_input("Digite um novo numero:")
    if st.button("registrar"):
        lista_dupla.adicionar_no_final(novo_nome, novo_numero)
        st.success(f"({novo_nome}, {novo_numero}) registrado!")

    # Interface para exibir a lista dupla
    st.header("Contatos:")
    no_atual = lista_dupla.cabeca
    while no_atual is not None:
        st.write(f"Nome: {no_atual.nome}, Numero: {no_atual.numero}")
        no_atual = no_atual.proximo

if __name__ == "__main__":
    main()

'''
