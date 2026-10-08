# Design

## Context

Proyecto nuevo, sin código todavía. See proposal.md for motivation. Los datos son un catálogo fijo pequeño y la app corre en local.

## Goals / Non-Goals

**Goals:**
- Mapa con marcadores de grafitis de Distrito Grafiti y popup con info + enlace a Google Maps.
- 3 capas separadas en archivos distintos, cada una con una sola responsabilidad.
- Código simple, con nombres claros, funciones pequeñas y comentarios, explicable en clase.

**Non-Goals:**
- Login, fotos, edición desde la web, otras zonas, búsqueda/filtros, tests automáticos, despliegue.

## Decisions

- **Python + Flask** → alternativa: FastAPI; se elige Flask por ser lo más simple y suficiente para un endpoint GET.
- **JSON como almacenamiento** (`grafitis.json`) → alternativa: SQLite/CSV; JSON evita dependencias y es directo para datos fijos y pocos.
- **Leaflet + OpenStreetMap** → alternativa: Google Maps JS; Leaflet no necesita API key ni cuenta de facturación.
- **Enlace a Google Maps construido por el backend** → el frontend solo pinta; mantiene la lógica de negocio fuera de la vista. URL sin API key: `https://www.google.com/maps?q=<latitud>,<longitud>`.
- **Estructura de carpetas por capa:**
  ```
  Proyecto predeterminado/
  +-- grafitis.json          (datos crudos: id, nombre, artista, latitud, longitud, descripcion)
  +-- backend.py             (leer JSON, construir enlace_maps)
  +-- api.py                 (Flask, ruta GET /api/grafitis)
  +-- static/ o templates/   (index.html con Leaflet)
  ```
- **Endpoint mínimo:** `GET /api/grafitis` → arreglo JSON; cada objeto incluye `enlace_maps`.

## Risks / Trade-offs

- Coordenadas de ejemplo aproximadas → se marcan "por verificar" en el catálogo; el usuario las corrige luego.
- Depender de CDN de Leaflet → requiere internet al abrir la página en local; alternativa futura sería vendorizar el JS.
- JSON en archivo → no escala a muchos usuarios/escrituras concurrentes; aceptable para el alcance del curso.
