from pathlib import Path


def check_folder(folder_name: str) -> bool:
    try:
        if Path.exists(Path(__file__).resolve().parent.parent.parent / folder_name):
            return True
        raise FileNotFoundError(
            f"Falha ao carregar o modelo. (Diretório {folder_name} não encontrado)"
        )
    except FileNotFoundError as e:
        print(f"Error: {e}")
    return False


def create_folder(folder_name: str) -> None:
    print(Path(__file__).resolve().parent.parent.parent / folder_name)
    if not Path.exists(Path(__file__).resolve() / folder_name):
        Path.touch(folder_name)
    else:
        raise FileExistsError("Arquivo ja existente!")
