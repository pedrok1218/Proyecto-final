import sqlite3
import json

DB_NAME = 'recursos_educativos.db'
JSON_BACKUP = 'recursos_backup.json'

def init_db():
    """Inicializa la base de datos y crea la tabla de recursos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # id (PRIMARY KEY), titulo, tipo (e.g., Video, Articulo), enlace, etiquetas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            tipo TEXT,
            enlace TEXT,
            etiquetas TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_recurso_db(titulo, tipo, enlace, etiquetas):
    """Inserta un nuevo recurso en la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recursos (titulo, tipo, enlace, etiquetas) VALUES (?, ?, ?, ?)",
                   (titulo, tipo, enlace, etiquetas))
    conn.commit()
    conn.close()

def get_all_recursos_db():
    """Obtiene todos los recursos de la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, tipo, enlace, etiquetas FROM recursos")
    recursos = [{'id': row[0], 'titulo': row[1], 'tipo': row[2], 'enlace': row[3], 'etiquetas': row[4]} for row in cursor.fetchall()]
    conn.close()
    return recursos

def search_recursos_db(query):
    """Busca recursos por título o etiquetas."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    search_term = f'%{query}%'
    cursor.execute("""
        SELECT id, titulo, tipo, enlace, etiquetas FROM recursos
        WHERE titulo LIKE ? OR etiquetas LIKE ?
    """, (search_term, search_term))
    recursos = [{'id': row[0], 'titulo': row[1], 'tipo': row[2], 'enlace': row[3], 'etiquetas': row[4]} for row in cursor.fetchall()]
    conn.close()
    return recursos

# --- Persistencia JSON simple (adicional) ---

def export_to_json():
    """Exporta todos los datos a un archivo JSON."""
    recursos = get_all_recursos_db()
    with open(JSON_BACKUP, 'w', encoding='utf-8') as f:
        json.dump(recursos, f, ensure_ascii=False, indent=4)
    return f"Datos exportados a {JSON_BACKUP}"