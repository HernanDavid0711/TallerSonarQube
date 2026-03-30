# Windows
python -m venv uniagustiniana
.\uniagustiniana\Scripts\activate

# Linux/macOS
python3 -m venv uniagustiniana
source uniagustiniana/bin/activate

pip install --upgrade pip
pip install -r requirements.txt 

# Ejecutar pruebas unitarias
pytest

# Ejecutar pruebas con reporte de cobertura para SonarCloud
pytest --cov=. --cov-report=xml