# 🛒 Marketplace API

API de marketplace desenvolvida com Django REST Framework, onde usuários podem cadastrar produtos e realizar pedidos autenticados.

## 🔧 Tecnologias utilizadas

- Python 3.11+
- Django 5.2
- Django REST Framework
- SQLite3 (padrão)

## 📦 Funcionalidades

- Cadastro de produtos por usuários autenticados
- Listagem pública de produtos
- Criação de pedidos (orders) autenticados
- Estoque atualizado automaticamente após cada compra
- Proteção de endpoints com autenticação
- Permissões básicas com `IsAuthenticated`

## 🔐 Regras de negócio

- Apenas usuários logados podem criar produtos ou fazer pedidos
- Estoque (`available_quantity`) é reduzido automaticamente após um pedido
- Pedidos são visíveis apenas para o comprador que os realizou

## 🚀 Como executar localmente

1. Clone o repositório:
git clone [https://github.com/seuusuario/nome-do-repo.git](https://github.com/mathorita/Marketplace-Simple.git)
cd nome-do-repo

Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

Instale as dependências:
pip install -r requirements.txt

Rode as migrações:
python manage.py migrate

Crie um superusuário:
python manage.py createsuperuser

Inicie o servidor:
python manage.py runserver

Acesse:

http://127.0.0.1:8000/products/ — Listagem e criação de produtos

http://127.0.0.1:8000/orders/ — Criação e listagem de pedidos (autenticado)

🔑 Autenticação
Por padrão, a API utiliza Basic Authentication:

Ao acessar endpoints protegidos, o navegador solicitará login e senha

Você pode usar o superusuário criado para testar

📂 Estrutura dos endpoints
Produtos
Método	Endpoint	Ação
GET	/products/	Listar produtos
POST	/products/	Criar produto (autenticado)
PUT	/products/<id>/	Atualizar produto (autenticado)
DELETE	/products/<id>/	Deletar produto (autenticado)

Pedidos
Método	Endpoint	Ação
GET	/orders/	Ver pedidos do usuário
POST	/orders/	Criar pedido (autenticado)

📄 Exemplo de criação de pedido
json
Copy
Edit
POST /orders/
{
  "product_id": 1,
  "quantity": 2
}
📌 Observações
Ao tentar comprar mais itens do que o disponível no estoque, a API retornará um erro de validação.

A listagem de pedidos é restrita ao usuário autenticado.
