import data_manager

def inicializar_aplicacion():
    """Inicializa la base de datos al inicio de la app."""
    data_manager.init_db()

def agregar_recurso(titulo, tipo, enlace, etiquetas):
    """Valida y agrega un recurso."""
    if not titulo or not enlace:
        return False, "El título y el enlace son obligatorios."
    # Podrías añadir validación de URL aquí si fuera necesario
    data_manager.add_recurso_db(titulo, tipo, enlace, etiquetas)
    return True, "Recurso agregado con éxito."

def obtener_recursos():
    """Retorna la lista completa de recursos."""
    return data_manager.get_all_recursos_db()

def buscar_recursos(query):
    """Busca recursos basándose en un query."""
    if not query:
        return obtener_recursos()
    return data_manager.search_recursos_db(query)

def generar_backup_json():
    """Ejecuta la exportación a JSON."""
    return data_manager.export_to_json()