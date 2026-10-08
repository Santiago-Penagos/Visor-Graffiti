# Spec Delta

## Purpose

Expone los grafitis del catálogo como JSON a través de una API REST, incluyendo el enlace a Google Maps construido por el backend.

## ADDED Requirements

### Requirement: Listar grafitis en JSON
El sistema SHALL responder a GET /api/grafitis con un arreglo JSON de grafitis, cada uno con id, nombre, artista, latitud, longitud, descripción y enlace_maps.

#### Scenario: Petición correcta
- **WHEN** el cliente hace GET /api/grafitis
- **THEN** la respuesta tiene código 200 y un arreglo JSON con los grafitis, cada uno incluyendo enlace_maps

### Requirement: El enlace a Google Maps lo construye el backend
El sistema SHALL incluir en cada grafiti un campo enlace_maps con la URL de Google Maps correspondiente a su latitud y longitud, por ejemplo https://www.google.com/maps?q=<latitud>,<longitud>.

#### Scenario: Formato del enlace
- **WHEN** el backend entrega un grafiti con latitud L y longitud G
- **THEN** el campo enlace_maps es https://www.google.com/maps?q=L,G

### Requirement: El catálogo viene de grafitis.json
El sistema SHALL leer los datos base de un archivo grafitis.json con 10 grafitis de ejemplo de la zona Distrito Grafiti y coordenadas aproximadas marcadas como "por verificar".

#### Scenario: Catálogo disponible
- **WHEN** el backend arranca y sirve GET /api/grafitis
- **THEN** responde con los 10 grafitis del archivo grafitis.json
