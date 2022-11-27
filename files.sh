# Arquivos na raiz
touch setup.py
touch {requirements,MANIFEST}.in
touch requirements_dev.txt

# Imagem do banco de dados

# Aplicação
mkdir -p statscli/reader
touch statscli/{__init__,cli,config}.py
touch statscli/reader/{__init__}.py


# Testes
touch test.sh
mkdir tests
touch tests/{__init__,conftest,test_api}.py