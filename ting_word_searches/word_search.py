def exists_word(word, instance):
    results = []
    for data in instance.data:
        for item, line in enumerate(data["linhas_do_arquivo"]):
            if word in line:
                results.append(
                    {
                        "palavra": word,
                        "arquivo": data["nome_do_arquivo"],
                        "ocorrencias": [
                            {"linha": item + 1},
                        ],
                    }
                )

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
