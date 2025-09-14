from dados import dados_filmes

# Mapeamento de emojis para gêneros de filmes
emojis_para_genero = {
    '😂': ['Comedy'],
    '❤️': ['Romance', 'Drama'],
    '🚀': ['Sci-Fi', 'Science Fiction'],
    '⚔️': ['Action', 'Adventure', 'Fantasy'],
    '😱': ['Horror', 'Thriller'],
    '🕵️': ['Mystery', 'Crime'],
    '👑': ['History', 'Fantasy'],
    '🎶': ['Music'],
    '🤠': ['Western']
}

def recomendar_filmes_por_emoji(emojis_usuario, df, mapeamento):
    generos_buscados = []
    for emoji in emojis_usuario:
        if emoji in mapeamento:
            generos_buscados.extend(mapeamento[emoji])

    generos_buscados = list(set(generos_buscados))

    if not generos_buscados:
        return ['Nenhum gênero correspondente encontrado!']
    
    filmes_encontrados = df[
        df['genres'].apply(
            lambda x: any(genero in x for genero in generos_buscados)
        )
    ]

    if 'popularity' in filmes_encontrados.columns:
        filmes_encontrados = filmes_encontrados.sort_values(
            by='popularity', ascending=False
        ).head(10)

    if filmes_encontrados.empty:
        return ['Desculpe, não encontramos o filme com o gênero selecionado']
    
    return filmes_encontrados['title'].tolist()