"# Manipulando Arquivos com Python

Este trabalho foi proposto na disciplina de Paradigmas de linguagens de Programação na Universidade Tecnológica Federal do Paraná (UTFPR), com o objetivo de extrair os dados de um arquivo .txt, aplicar formulas matematica (Moda, mediana e média) e apresentar o resultado ao usuário. Vale salientar que foi usado a base da arquitetura MVC para o desenvolvimento do mesmo.

**Importante:** Para executar o programa será necessario a instalação da biblioteca "MatPlotLib", onde você pode encontrar a documentação neste link: https://matplotlib.org/3.1.1/users/installing.html


## Descrição das funções:

**classe principal:**
    1- apresentacaoMenu
        Está função é para apresentar um menu no prompt de comando do usuário para que ele define qual variedade ele deseja observar.
    
    2- analiseDaEntradaMenu
        Pega a entrada digitada pelo o usuário e passa as informações necessaria para a função "apresentaValores".

    3- apresentacaoValores
        Apresentara no prompt os dados de acordo com o que o usuário digitou para visualizar. Depois chama a função "apresentacaoMenuGrafico".

    4- apresentacaoMenuGrafico
        Aqui sera definido qual gráfico o usuário deseja visualizar.

    5- apresentacaoGrafico
        Prepara todas variáveis para inserir no gráfico.

**Classe GeraGrafico**
    - Nesta Classe foi usado a biblioteca matplotlib para definir as propriedades do gráfico (Cor, nomes e etc).

__Duvidas__ sobre o programa, pode-se entrar em contato com os autores por email:
    Jecé Xavier: jece@alunos.utfpr.edu.br
    Matheus Ramos: matheusramos@alunos.utfpr.edu.br
"
