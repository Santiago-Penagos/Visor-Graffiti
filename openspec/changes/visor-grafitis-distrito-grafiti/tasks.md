# Tasks

## 1. Datos y backend

- [x] 1.1 Crear `grafitis.json` con 10 grafitis de ejemplo de Distrito Grafiti (coordenadas aproximadas "por verificar") y verificar que el JSON es válido
- [x] 1.2 Implementar en `backend.py` la lectura de `grafitis.json` y la construcción de `enlace_maps` por grafiti; verificar llamando a la función desde consola

## 2. API

- [x] 2.1 Crear `api.py` con Flask y la ruta `GET /api/grafitis` que usa el backend; verificar que devuelve 200 y JSON con 10 grafitis incluyendo `enlace_maps`

## 3. Frontend

- [x] 3.1 Crear la página con Leaflet que pide `GET /api/grafitis` y pinta el mapa con un marcador por grafiti; verificar en el navegador
- [x] 3.2 Mostrar popup con nombre, artista, descripción y enlace; verificar que el enlace abre Google Maps con las coordenadas del grafiti

## 4. Prueba manual

- [x] 4.1 Levantar Flask, abrir la página en el navegador y recorrer: mapa visible, clic en marcador muestra popup, enlace abre Google Maps; ajuste de coordenadas "por verificar" si hace falta
