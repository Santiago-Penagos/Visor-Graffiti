# Proposal

## Why

Bogotá tiene una escena de grafiti urbano reconocida, y la zona del Distrito Grafiti concentra gran parte de esas obras. Hoy no existe una forma sencilla de explorar esos puntos: se quiere una página web que muestre el mapa de la zona con marcadores y la información básica de cada grafiti, pensada como proyecto académico del curso de POO.

## What Changes

- Nuevo catálogo de datos `grafitis.json` con 10 grafitis de ejemplo de la zona Distrito Grafiti (coordenadas aproximadas, marcadas como "por verificar").
- Backend en Python + Flask que lee el catálogo y construye el enlace a Google Maps para cada grafiti.
- API REST con el endpoint `GET /api/grafitis` que responde JSON.
- Frontend con Leaflet + OpenStreetMap que muestra el mapa, marcadores y un popup por grafiti con nombre, artista, descripción y enlace a Google Maps.
- Sin login, sin subida de fotos, sin edición desde la web, sin otras zonas, sin tests automáticos ni despliegue.

## Capabilities

### New Capabilities

- `mapa-grafitis`: el usuario ve el mapa de la zona Distrito Grafiti con un marcador por grafiti y puede abrir la información de cada uno.
- `api-grafitis`: la API expone los grafitis en JSON, incluyendo el enlace a Google Maps construido por el backend.

### Modified Capabilities

- Ninguna.

## Impact

- Proyecto nuevo (directorio vacío salvo `openspec/`).
- Dependencias: Python, Flask, Leaflet (CDN, sin API key).
- Corre en local; sin despliegue ni servicios externos de pago.
