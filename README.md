#  Gestor de Recursos Educativos Digitales (RED) - v1.0.0

Aplicación de escritorio simple desarrollada en Python con **Tkinter** para catalogar, organizar y buscar materiales de estudio digitales. Aborda la necesidad educativa de centralizar la gestión de la vasta cantidad de recursos disponibles en línea (videos, artículos, simulaciones).

**Etiqueta del Repositorio:** v1.0.0 (Versión inicial de lanzamiento).

## 🚀 Instalación y Ejecución

### 1. Pre-requisitos

* **Python 3.x**
* **Tkinter** (generalmente incluido en las instalaciones estándar de Python).

### 2. Estructura del Proyecto

 los archivos estan organizados de la siguiente manera:
Proyecto-final/ ├── app_ui.py ├── data_manager.py ├── logic.py ├── requirements.txt ├── README.md
 ├── tests/ │ └── test_app.py └── data/

 ### 3. Instalación de Dependencias

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/pedrok1218/Proyecto-final.git](https://github.com/pedrok1218/Proyecto-final.git)
    cd Proyecto-final
    ```

2.  **Crear y activar un entorno virtual** (Recomendado):
    ```bash
    python -m venv venv
    # Linux/macOS:
    source venv/bin/activate
    # Windows (PowerShell):
    .\venv\Scripts\Activate.ps1
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### 4. Ejecución

* **Ejecutar la Interfaz Gráfica:**
    ```bash
    python app_ui.py
    ```
    *(La base de datos, recursos_educativos.db, se creará en la raíz del proyecto al ejecutarse por primera vez).*

* **Ejecutar las Pruebas Unitarias (Pytest):**
    ```bash
    pytest tests/test_app.py
    ```

***

##  Diseño, Hitos y Decisiones de Desarrollo

### 1. Estructura Modular (Separación de Capas)

El diseño se basa en una clara separación de responsabilidades:

| Módulo | Responsabilidad | Persistencia |
| :--- | :--- | :--- |
| **app_ui.py** | **Presentación (UI):** Maneja Tkinter y la interacción. | N/A |
| **logic.py** | **Lógica de Negocio:** Contiene validaciones, búsquedas y coordina las operaciones. | N/A |
| **data_manager.py** | **Datos (Persistencia):** Acceso directo a sqlite3 y manejo de json. | SQLite3 y JSON |

### 2. Hitos de Desarrollo Clave

1.  **Persistencia y CRUD Básico:** Implementación de SQLite3.
2.  **Lógica y Validación:** Desarrollo de logic.py para abstraer la base de datos y validar campos obligatorios.
3.  **Interfaz Funcional:** Creación de la UI con Tkinter, incluyendo el `Treeview` y la integración con la lógica para agregar y listar.
4.  **Búsqueda y Persistencia JSON:** Implementación de la búsqueda flexible y la función de respaldo JSON.
5.  **Pruebas Robustas:** Desarrollo de **6 pruebas unitarias** utilizando *fixtures* de Pytest para asegurar la limpieza del entorno (DB) entre cada test.

### 3. Justificación de Librerías

* **tkinter:** Elegi esta libreria para cumplir el requisito de una interfaz de escritorio **nativa** y **simple** en Python.
* **sqlite3:** Módulo estándar de Python elegido para la **persistencia simple** y sin servidor.
* **json:** Módulo estándar para la funcionalidad de **respaldo/copia de seguridad**.
* **pytest:** Elegi este marco de pruebas por su **legibilidad** y su **potente sistema de *fixtures***, el cual es crucial para lograr el aislamiento en las pruebas unitarias.

***

## Fundamento Didáctico

### Aprendizajes Obtenidos

1.  **Arquitectura Limpia (Separación de Intereses):** El principal aprendizaje para mi fue aplicar el principio de responsabilidad unica, resultando en un código más mantenible. Esto permitió probar la lógica de negocio (logic.py) sin depender de la interfaz (app_ui.py).
2.  **Testing Automático Aislado:** El uso de fixtures en Pytest para eliminar y recrear la base de datos antes de cada prueba fue fundamental para asegurar que todos los tests fueran independientes y confiables.
3.  **Integración de Tecnologías:** Se consolidó la habilidad de integrar múltiples tecnologías (Tkinter, Lógica de Negocio, SQLite, Pruebas) dentro de una estructura de proyecto coherente.

### Desafíos Superados

* **Limpieza de Entorno para Testing:** Lograr que Pytest gestionara la eliminación y creación del archivo de la DB (recursos_educativos.db) para garantizar un estado inicial limpio en cada ejecución de prueba.
* **Sincronización de UI:** Asegurar la **actualización inmediata** de la lista de recursos (el Treeview de Tkinter) tras cualquier operación de guardado o búsqueda.

### Reflexión del Proceso

Creo que el proyecto demuestra la importancia de la **planificación modular**. La inversión inicial en la separación de capas y en las pruebas unitarias con Pytest garantizó la robustez del sistema y facilitó la integración final de la interfaz gráfica.