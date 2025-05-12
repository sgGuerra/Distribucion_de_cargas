# Calculadora de Campo Eléctrico

Una aplicación Python que calcula y visualiza el campo eléctrico generado por una distribución de carga semicircular.

## Descripción

Esta aplicación calcula el campo eléctrico neto en el centro de una distribución de carga semicircular donde:
- La mitad izquierda del semicírculo tiene una carga positiva (+Q)
- La mitad derecha tiene una carga negativa (-Q)
- El cálculo se realiza en el origen (centro) del semicírculo

## Características

- Interfaz gráfica interactiva construida con Tkinter
- Visualización en tiempo real de la distribución de carga
- Cálculo del campo eléctrico neto
- Gráficos dinámicos con matplotlib
- Validación de entrada y manejo de errores
- Parámetros ajustables de carga (Q) y radio (a)

## Requisitos Previos

- Python >= 3.8
- Paquetes requeridos:
  ```
  numpy==1.24.3
  matplotlib==3.7.1
  scipy==1.10.1
  pytest==7.4.3
  tk==0.1.0
  ```

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/sgGuerra/Distribucion_de_cargas.git  
```

2. Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

3. Instala los paquetes requeridos:
```bash
pip install -r requirements.txt
```

## Uso

Ejecuta la aplicación:
```bash
python carga_electrica.py
```

En la interfaz gráfica:

1. Ingresa la carga Q en microCoulombs (µC)
2. Ingresa el radio a en metros (m)
3. Haz clic en "Calcular" para ver los resultados
4. Usa "Reiniciar" para limpiar las entradas y comenzar de nuevo

## Fundamentos Físicos

La aplicación utiliza los siguientes conceptos:
- Ley de Coulomb
- Densidad lineal de carga
- Integración del campo eléctrico
- Principio de superposición

## Estructura del Código

- `carga_electrica.py`: Archivo principal de la aplicación que contiene:
  - `campo_electrico_neto()`: Calcula el campo eléctrico neto
  - `graficar_distribucion()`: Maneja la visualización
  - `AplicacionCampoElectrico`: Clase principal de la interfaz gráfica

## Contribuir

Siéntete libre de enviar problemas y solicitudes de mejoras.

## Autor

Luis Carlos Guerra Herrera

## Agradecimientos

- Basado en la teoría de campos electromagnéticos
- Utiliza bibliotecas de computación científica (NumPy, SciPy)
- Visualización desarrollada con Matplotlib