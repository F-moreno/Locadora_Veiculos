import streamlit as st

opcao = st.sidebar.selectbox(
    "Selecione uma ação", ("Adicionar Produto", "Listar Produtos")
)

produtos = []

with open("produtos.txt", "r", encoding="utf-8") as arquivo:
    for lista in arquivo:
        # lista = "id: 1, nome: Produto 1, preco: 19.99"
        # dicionario = {"id": 1, "nome": "Produto 1", "preco": 19.99}"
        produtos.append(dict(lista.split(",")))
        print(lista)


def listar_produto():
    st.subheader("Lista de Produtos")
    for produto in produtos:
        st.write(
            f"ID: {produto['id']}, Nome {produto['nome']}, Preço: {produto['preco']}"
        )


def adicionar_produto():
    st.subheader("Adicionar Produto")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço do Produto")

    if st.button("Adicionar"):
        novo_produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
        produtos.append(novo_produto)

        # Write the new product to the file
        with open("produtos.txt", "a", encoding="utf-8") as arquivo:
            produto_str = f"id: {novo_produto['id']}, nome: {novo_produto['nome']}, preco: {novo_produto['preco']}\n"
            arquivo.write(produto_str)

        st.success("Produto adicionado com sucesso!")


if opcao == "Adicionar Produto":
    adicionar_produto()
elif opcao == "Listar Produtos":
    listar_produto()
