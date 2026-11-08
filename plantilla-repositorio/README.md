# Ficha de la aplicación APP-XX

<!-- Sustituid todo lo que aparece entre corchetes y borrad estos comentarios. -->

Programa que muestra, en diez opciones, la ficha técnica de una aplicación móvil antes de
publicarla: identificación, tamaño del APK, ingresos, versionCode, permisos, color del icono y
varias comprobaciones sobre tipos y redondeo.

**Módulo:** IC44 — Fundamentos de programación en Python
**Unidad:** 1 — Estructura de un programa y elementos del lenguaje
**Pareja:** [número]
**Autores:** [usuario] · [usuario]

## Aplicación descrita

| Dato | Valor |
|---|---|
| Código | [APP-XX] |
| Nombre | [nombre] |
| Paquete | [paquete] |
| Versión | [mayor.menor.parche] |
| Tamaño del APK | [bytes] |
| Descargas y precio | [descargas · precio] |

## Ejecución desde Docker Hub

No hace falta descargar el repositorio ni tener Python instalado. Solo Docker.

```bash
docker run --rm [usuario]/ficha-app-xx:1.0.0
```

Página de la imagen: https://hub.docker.com/r/[usuario]/ficha-app-xx

## Ejecución en local

Requiere Python 3.10 o superior.

```bash
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
python ficha_app.py
```

## Construir la imagen

```bash
docker build -t ficha-app-xx .
docker run --rm ficha-app-xx
```

## Integración continua

<!-- Solo si habéis hecho la pipeline opcional (Azure Pipelines, GitHub Actions u otra). Si no, borrad este apartado. -->

[Qué agente usa la pipeline, qué comprueba, cuándo se ejecuta y cuándo publica la imagen.]

## Estructura del proyecto

```
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── ficha_app.py
```
