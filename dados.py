import pandas as pd
import ast
import os # Importa o módulo 'os'

def dados_filmes():
    """
    Carrega e limpa o DataFrame de filmes de um arquivo local.
    """
    # -----------------------------------------------------------
    #  SOLUÇÃO FINAL: Usa a função os.path.join para construir o caminho
    # -----------------------------------------------------------
    # A pasta onde o arquivo 'data_loader.py' está
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Adiciona a subpasta 'archive' e o nome do arquivo
    caminho_do_arquivo = os.path.join(base_dir, 'archive', 'movies_metadata.csv')

    try:
        df = pd.read_csv(caminho_do_arquivo, low_memory=False)
        # Se você chegar aqui, o arquivo foi encontrado!
        print(f"DEBUG: Arquivo encontrado em: {caminho_do_arquivo}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

    # O restante do código de limpeza permanece o mesmo
    # Certifique-se de que o nome 'genres' e 'overview' estão corretos
    df.dropna(subset=['genres', 'overview', 'title'], inplace=True)
    
    df['genres'] = df['genres'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) else []
    )
    df['genres'] = df['genres'].apply(
        lambda x: [genre['name'] for genre in x]
    )

    df['overview'] = df['overview'].fillna('')
    df['overview'] = df['overview'].str.lower()
    df['overview'] = df['overview'].str.replace('[^\w\s]', '', regex=True)

    return df