import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import logic

class AppRED(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Recursos Educativos Digitales")
        self.geometry("800x600")
        
        logic.inicializar_aplicacion() # Inicializa la DB
        
        self.create_widgets()
        self.load_recursos()

    def create_widgets(self):
        # Notebook para pestañas de Agregar y Listar/Buscar
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # Pestaña 1: Agregar Recurso
        frame_add = ttk.Frame(self.notebook)
        self.notebook.add(frame_add, text="➕ Agregar Recurso")
        self.setup_add_frame(frame_add)

        # Pestaña 2: Listar y Buscar
        frame_list = ttk.Frame(self.notebook)
        self.notebook.add(frame_list, text="🔍 Recursos")
        self.setup_list_frame(frame_list)
        
        # Botón de exportar JSON
        btn_export = ttk.Button(self, text="💾 Exportar a JSON", command=self.export_json_action)
        btn_export.pack(pady=5)

    def setup_add_frame(self, frame):
        # --- Variables de control para los campos de entrada ---
        self.var_titulo = tk.StringVar()
        self.var_tipo = tk.StringVar(value="Video")
        self.var_enlace = tk.StringVar()
        self.var_etiquetas = tk.StringVar()
        
        # Título
        ttk.Label(frame, text="Título:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        self.entry_titulo = ttk.Entry(frame, textvariable=self.var_titulo, width=60)
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=10)

        # Tipo (Combobox)
        ttk.Label(frame, text="Tipo:").grid(row=1, column=0, padx=5, pady=10, sticky="w")
        tipos = ["Video", "Artículo", "Simulación", "PDF", "Otro"]
        self.combo_tipo = ttk.Combobox(frame, textvariable=self.var_tipo, values=tipos, state="readonly", width=57)
        self.combo_tipo.grid(row=1, column=1, padx=5, pady=10)

        # Enlace
        ttk.Label(frame, text="Enlace (URL):").grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.entry_enlace = ttk.Entry(frame, textvariable=self.var_enlace, width=60)
        self.entry_enlace.grid(row=2, column=1, padx=5, pady=10)

        # Etiquetas
        ttk.Label(frame, text="Etiquetas (separadas por coma):").grid(row=3, column=0, padx=5, pady=10, sticky="w")
        self.entry_etiquetas = ttk.Entry(frame, textvariable=self.var_etiquetas, width=60)
        self.entry_etiquetas.grid(row=3, column=1, padx=5, pady=10)

        # Botón de Guardar
        ttk.Button(frame, text="Guardar Recurso", command=self.add_recurso_action).grid(row=4, column=1, pady=20, sticky="e")

    def setup_list_frame(self, frame):
        # Frame para la búsqueda
        search_frame = ttk.Frame(frame)
        search_frame.pack(pady=5, padx=10, fill="x")
        
        # Caja de búsqueda
        self.search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_var, width=50).pack(pady=5, padx=10, side="left", fill="x", expand=True)
        ttk.Button(search_frame, text="Buscar", command=self.search_recursos_action).pack(pady=5, padx=5, side="left")
        ttk.Button(search_frame, text="Mostrar Todo", command=self.load_recursos).pack(pady=5, padx=5, side="left")

        # Treeview para mostrar la lista de recursos
        columns = ("Titulo", "Tipo", "Enlace", "Etiquetas")
        self.tree = ttk.Treeview(frame, columns=columns, show='headings')
        self.tree.heading("Titulo", text="Título")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Enlace", text="Enlace")
        self.tree.heading("Etiquetas", text="Etiquetas")
        
        # Configuración de anchos de columna (opcional)
        self.tree.column("Titulo", width=250, anchor=tk.W)
        self.tree.column("Tipo", width=80, anchor=tk.CENTER)
        self.tree.column("Enlace", width=250, anchor=tk.W)
        self.tree.column("Etiquetas", width=150, anchor=tk.W)
        
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def add_recurso_action(self):
        # Obtener valores de las variables de control
        titulo = self.var_titulo.get()
        tipo = self.var_tipo.get()
        enlace = self.var_enlace.get()
        etiquetas = self.var_etiquetas.get()
        
        success, message = logic.agregar_recurso(titulo, tipo, enlace, etiquetas)
        if success:
            messagebox.showinfo("Éxito", message)
            
            # Limpiar campos
            self.var_titulo.set("")
            self.var_enlace.set("")
            self.var_etiquetas.set("")
            
            self.load_recursos() # Recargar la lista
        else:
            messagebox.showerror("Error de Validación", message)
            
    def load_recursos(self, recursos=None):
        """Carga o recarga los recursos en el Treeview."""
        if recursos is None:
            recursos = logic.obtener_recursos()
        
        # Limpiar Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
            
        # Insertar nuevos datos
        for rec in recursos:
            # Insertamos solo los datos visibles (quitando el ID)
            self.tree.insert('', tk.END, values=(rec['titulo'], rec['tipo'], rec['enlace'], rec['etiquetas']))

    def search_recursos_action(self):
        query = self.search_var.get()
        recursos_encontrados = logic.buscar_recursos(query)
        self.load_recursos(recursos_encontrados)

    def export_json_action(self):
        try:
            message = logic.generar_backup_json()
            messagebox.showinfo("Exportación JSON", message)
        except Exception as e:
            messagebox.showerror("Error de Exportación", f"Ocurrió un error: {e}")

if __name__ == '__main__':
    app = AppRED()
    app.mainloop()