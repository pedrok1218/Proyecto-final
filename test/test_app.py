import pytest
import logic
import data_manager
import os

# Nombre de la DB para pruebas (debe ser el mismo que en data_manager)
DB_TEST_NAME = 'recursos_educativos.db'

@pytest.fixture(autouse=True)
def setup_teardown_db():
    """Fixture que se ejecuta antes y después de cada prueba para asegurar un estado limpio."""
    if os.path.exists(DB_TEST_NAME):
        os.remove(DB_TEST_NAME)
    logic.inicializar_aplicacion()
    yield
    # Eliminamos el archivo JSON de prueba para mantener limpio el entorno
    if os.path.exists(data_manager.JSON_BACKUP):
        os.remove(data_manager.JSON_BACKUP)
    if os.path.exists(DB_TEST_NAME):
        os.remove(DB_TEST_NAME)

# --- Mínimo 5 Pruebas Unitarias ---

def test_1_db_initialization():
    """Prueba que la DB se crea y está vacía al inicio."""
    recursos = logic.obtener_recursos()
    assert os.path.exists(DB_TEST_NAME)
    assert len(recursos) == 0

def test_2_add_recurso_success():
    """Prueba la funcionalidad de agregar un recurso con datos válidos."""
    titulo = "Algebra Lineal Video"
    tipo = "Video"
    enlace = "http://youtube.com/alglin"
    etiquetas = "matematicas, universidad"
    
    success, message = logic.agregar_recurso(titulo, tipo, enlace, etiquetas)
    assert success is True
    assert "agregado con éxito" in message
    
    recursos = logic.obtener_recursos()
    assert len(recursos) == 1
    assert recursos[0]['titulo'] == titulo

def test_3_add_recurso_failure_no_title():
    """Prueba la validación cuando falta el título."""
    success, message = logic.agregar_recurso("", "Articulo", "http://articulo.com", "programacion")
    assert success is False
    assert "título" in message

def test_4_search_by_title():
    """Prueba la búsqueda de recursos por una palabra en el título."""
    logic.agregar_recurso("Tutorial de Python Básico", "Artículo", "http://py.com/basico", "programacion")
    logic.agregar_recurso("Curso de C++ Avanzado", "Video", "http://cpp.com/avanzado", "programacion")
    
    resultados = logic.buscar_recursos("Python")
    assert len(resultados) == 1
    assert "Python" in resultados[0]['titulo']

def test_5_search_by_tag():
    """Prueba la búsqueda de recursos por una etiqueta."""
    logic.agregar_recurso("Historia Antigua", "Artículo", "http://historia.com/antigua", "sociales, historia")
    logic.agregar_recurso("Química Orgánica", "Simulación", "http://quimica.com/organica", "ciencias, laboratorio")
    
    resultados = logic.buscar_recursos("ciencias")
    assert len(resultados) == 1
    assert "ciencias" in resultados[0]['etiquetas']
    
def test_6_json_export_integrity():
    """Prueba que el backup JSON contenga los datos correctos."""
    logic.agregar_recurso("Recurso A", "Tipo A", "Enlace A", "Tag A")
    
    logic.generar_backup_json()
    
    import json
    with open(data_manager.JSON_BACKUP, 'r', encoding='utf-8') as f:
        data_json = json.load(f)
        
    assert len(data_json) == 1
    assert data_json[0]['titulo'] == "Recurso A"
    assert 'id' in data_json[0] # Verifica que los campos de DB estén presentes