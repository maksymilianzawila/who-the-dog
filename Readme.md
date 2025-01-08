# Who The Dog? 🐾

## Opis
Aplikacja `Who The Dog?` to narzędzie do rozpoznawania ras psów na podstawie przesłanych zdjęć. Użytkownik może przesłać zdjęcie swojego psa, a aplikacja zidentyfikuje jego rasę oraz wyświetli poziom pewności predykcji.

## Wymagania
- Python 3.9+
- Streamlit
- TensorFlow
- Pandas
- Pillow
- Altair

## Instalacja
1. Sklonuj repozytorium:
    ```sh
    git clone https://github.com/maksymilianzawila/who-the-dog.git
    cd who-the-dog
    ```

2. Utwórz i aktywuj wirtualne środowisko:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Na Windows: .venv\Scripts\activate
    ```

3. Zainstaluj wymagane pakiety:
    ```sh
    pip install -r requirements.txt
    ```

## Uruchomienie
1. Upewnij się, że masz plik modelu `dog_breed.h5` w katalogu głównym projektu.
2. Upewnij się, że masz plik `labels.csv` zawierający nazwy ras psów.
3. Uruchom aplikację Streamlit:
    ```sh
    streamlit run main.py
    ```

## Użycie
1. Otwórz przeglądarkę i przejdź do `http://localhost:8501`.
2. Prześlij zdjęcie swojego psa w formacie JPEG lub PNG.
3. Aplikacja wyświetli przewidywaną rasę psa oraz poziom pewności predykcji.

## Struktura projektu
- `main.py`: Główny plik aplikacji Streamlit.
- `dog_breed.h5`: Plik modelu do rozpoznawania ras psów.
- `labels.csv`: Plik CSV zawierający nazwy ras psów.

## Licencja
Ten projekt jest licencjonowany na warunkach licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.