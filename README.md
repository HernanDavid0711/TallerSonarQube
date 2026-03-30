# Taller de calidad de software en Python

Este proyecto demuestra una solucion minima para un taller de CI/CD, pruebas unitarias, cobertura y analisis estatico con Sonar.

## Requisitos

- Python 3.12
- Cuenta en GitHub
- Proyecto en SonarCloud o instancia de SonarQube

## Ejecucion local

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

pip install --upgrade pip
pip install -r requirements.txt
flake8 .
pytest --cov=. --cov-report=xml --cov-report=term-missing
```

## Archivos clave

- `main.py`: logica refactorizada
- `test_main.py`: pruebas unitarias
- `.github/workflows/ci.yml`: pipeline para GitHub Actions
- `sonar-project.properties`: configuracion base para Sonar

## Secrets requeridos en GitHub

- `SONAR_TOKEN`
- `SONAR_HOST_URL`

> Si usas SonarCloud, normalmente `SONAR_HOST_URL` es `https://sonarcloud.io`.

## Quality Gate sugerido

- Cobertura minima: 80%
- Vulnerabilidades criticas: 0
- Bugs: 0 en codigo nuevo
- Code smells: 0 bloqueantes en codigo nuevo
