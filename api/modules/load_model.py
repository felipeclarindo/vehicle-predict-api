import joblib
from pathlib import Path

def load_model(file_path):
    try:
        if not Path.exists(Path(__file__).resolve().parent.parent.parent / file_path):
            raise FileNotFoundError("Falha ao carregar o modelo. (Arquivo não encontrado)")
        model = joblib.load(file_path)
        return model
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o modelo: {e}")
    return None