# Spec Delta

## Purpose

Permite al usuario explorar los grafitis del Distrito Grafiti de Bogotá en un mapa interactivo y ver la información de cada uno.

## ADDED Requirements

### Requirement: Mostrar el mapa con marcadores
El sistema SHALL mostrar en la página un mapa centrado en la zona Distrito Grafiti de Bogotá con un marcador por cada grafiti del catálogo.

#### Scenario: Carga inicial del mapa
- **WHEN** el usuario abre la página
- **THEN** se muestra el mapa con un marcador por grafiti

### Requirement: Mostrar información al hacer clic en un marcador
El sistema SHALL mostrar, al hacer clic en un marcador, un popup con el nombre, artista, descripción y el enlace a Google Maps de ese grafiti.

#### Scenario: Clic en un marcador
- **WHEN** el usuario hace clic en un marcador
- **THEN** se muestra un popup con nombre, artista, descripción y enlace a Google Maps

### Requirement: Abrir la ubicación en Google Maps
El sistema SHALL permitir abrir la ubicación del grafiti en Google Maps al pulsar el enlace del popup.

#### Scenario: Abrir el enlace
- **WHEN** el usuario pulsa el enlace del popup
- **THEN** se abre en una nueva pestaña Google Maps mostrando las coordenadas de ese grafiti
