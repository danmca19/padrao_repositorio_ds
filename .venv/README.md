# Projeto: Gerenciamento de Ambientes Virtuais em Python

Este projeto demonstra como manter dois ambientes virtuais independentes em Python para projetos diferentes:

- **projeto_legado**: usa `pandas==1.3.5`
- **projeto_novo**: usa `pandas==2.2.3`

## Estrutura de Pastas
```
projetos_python/
│── projeto_legado/
│   ├── venv_legado/
│   ├── analise_legado.py
│   ├── requirements.txt
│   ├── setup_legado.bat
│   ├── setup_legado.sh
│
│── projeto_novo/
│   ├── venv_novo/
│   ├── analise_novo.py
│   ├── requirements.txt
│   ├── setup_novo.bat
│   ├── setup_novo.sh
```

## Como usar os scripts de ambiente
- No Windows, execute o arquivo `.bat` correspondente dentro de cada pasta.
- No Linux/Mac, execute o arquivo `.sh` correspondente.

Isso criará o ambiente virtual e instalará as dependências automaticamente.
