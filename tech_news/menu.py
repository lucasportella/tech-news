import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


options = """
    Selecione uma das opções a seguir:
    0 - Popular o banco com notícias;
    1 - Buscar notícias por título;
    2 - Buscar notícias por data;
    3 - Buscar notícias por fonte;
    4 - Buscar notícias por categoria;
    5 - Listar top 5 notícias;
    6 - Listar top 5 categorias;
    7 - Sair.
            """

specific_options = {
    0: "Digite quantas notícias serão buscadas:",
    1: "Digite o título:",
    2: "Digite a data no formato aaaa-mm-dd:",
    3: "Digite a fonte:",
    4: "Digite a categoria:",
}

# lambda with no args
execute = {
    0: lambda: get_tech_news(int(input(specific_options[0]))),
    1: lambda: search_by_title(str(input(specific_options[1]))),
    2: lambda: search_by_date(str(input(specific_options[2]))),
    3: lambda: search_by_source(str(input(specific_options[3]))),
    4: lambda: search_by_category(str(input(specific_options[4]))),
    5: top_5_news,
    6: top_5_categories,
    7: lambda: sys.exit('Encerrando script'),
}


def analyzer_menu():
    try:
        option = int(input(options))
    except ValueError:
        print("Opção inválida")
    else:
        print(execute[option]())
