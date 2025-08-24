# Relatório – Gerenciamento de Ambientes Virtuais em Python

## Experiência
O projeto demonstrou a importância de isolar ambientes de desenvolvimento.  
O **projeto legado** funcionou apenas com `pandas==1.3.5`, enquanto o código atualizado rodou corretamente em `pandas==2.2.3`.  

A principal diferença foi que o método `DataFrame.append()` foi removido nas versões mais recentes do pandas, exigindo a adaptação para `pd.concat()`.

## Desafios
- Relembrar como ativar ambientes no **Windows** e no **Linux/Mac**.
- Ajustar o código antigo para compatibilidade com a versão nova do Pandas.
- Garantir que cada ambiente tenha seu próprio `requirements.txt`.

## Conclusão
O uso de ambientes virtuais permite gerenciar diferentes versões de bibliotecas em paralelo sem conflitos, algo essencial em projetos de ciência de dados e desenvolvimento de software.
