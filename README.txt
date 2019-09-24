Guida all'utilizzo

Requisiti:

-Ubuntu 16.04 o superiore
-GCC 4.9 o superiore
-Python 3.6

Procedura:

-Installare le dipendenze eseguendo il file dependencies/install-deps-ubuntu.sh
-Creare un virtualenv attraverso python 3.6
-Attivare il venv precedentemente creato "source nome-venv/bin/activate"
-Installare nel seguente venv i pacchetti numpy e json: "pip install nome-pacchetto"
-Installare il file .whl corrispondente alla versione modificata di open3D necessaria "pip install open3d-0.7.0.0-cp36-cp36m-linux_x86_64.whl"

Avvio:

Basterà eseguire il file Main.py dopo aver inserito l'indirizzo di una cartella contenente una nuvola di punti convertita precedentemente. Il codice nel file Main.py mostra anche come eseguire la conversione di un file (codice commentato).

