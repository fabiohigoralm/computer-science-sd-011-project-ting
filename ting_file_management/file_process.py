import sys
from ting_file_management import file_management


def process(path_file, instance):
    content = file_management.txt_importer(path_file)
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }
    if file not in instance.data:
        instance.enqueue(file)

    sys.stdout.write(str(file))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')
    else:
        file_removed = instance.dequeue()
        file_name = file_removed['nome_do_arquivo']
        return sys.stdout.write(f'Arquivo {file_name} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(str(file))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
