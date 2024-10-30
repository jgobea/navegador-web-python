from modules.historial import HistoryManager
from modules.pestanas import TabManager
from modules.descargas import DownloadManager
from modules.html_viewer import HTMLViewer

class WebBrowser:
    def __init__(self):
        self.html_viewer = HTMLViewer()
        self.history = HistoryManager()
        self.tabs = TabManager()
        self.downloads = DownloadManager()

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return True

        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        # Módulo 1: Historial de Navegación
        if cmd == "ir" and args:
            self.history.visit_url(args[0])
        elif cmd == "atras":
            self.history.go_back()
        elif cmd == "adelante":
            self.history.go_forward()
        elif cmd == "mostrar_historial":
            self.history.show_history()

        # Módulo 2: Pestañas
        elif cmd == "nueva_pestana" and args:
            self.tabs.new_tab(args[0])
        elif cmd == "cerrar_pestana":
            self.tabs.close_tab()
        elif cmd == "cambiar_pestana" and args:
            try:
                self.tabs.switch_tab(int(args[0]))
            except ValueError:
                print("Número de pestaña inválido")
        elif cmd == "mostrar_pestanas":
            self.tabs.show_tabs()

        # Módulo 3: Descargas
        elif cmd == "descargar" and args:
            self.downloads.add_download(args[0])
        elif cmd == "mostrar_descargas":
            self.downloads.show_downloads()
        elif cmd == "cancelar_descarga" and args:
            try:
                self.downloads.cancel_download(int(args[0]))
            except ValueError:
                print("Número de descarga inválido")

        # Módulo 4: Visualización de Páginas
        elif cmd == "listar_paginas":
            self.html_viewer.list_pages()
        elif cmd == "mostrar_contenido" and len(args) >= 2:
            self.html_viewer.show_content(args[0], args[1])

        # Comandos generales
        elif cmd == "ayuda":
            self.show_help()
        elif cmd == "salir":
            return False
        else:
            print("Comando no reconocido. Use 'ayuda' para ver los comandos disponibles.")
        
        return True

    def show_help(self):
        print("""
Comandos disponibles:

1. Historial de Navegación:
   - ir <url o ip>: Visitar una página
   - atras: Volver a la página anterior
   - adelante: Avanzar a la página siguiente
   - mostrar_historial: Mostrar todas las páginas visitadas

2. Gestión de Pestañas:
   - nueva_pestana <url>: Abrir una nueva pestaña
   - cerrar_pestana: Cerrar la pestaña actual
   - cambiar_pestana <n>: Cambiar a la pestaña número n
   - mostrar_pestanas: Mostrar todas las pestañas abiertas

3. Gestión de Descargas:
   - descargar <url>: Iniciar la descarga de un archivo
   - mostrar_descargas: Mostrar el estado de la cola de descargas
   - cancelar_descarga <n>: Cancelar la descarga número n

4. Visualización de Páginas:
   - listar_paginas: Mostrar todas las páginas HTML disponibles
   - mostrar_contenido <url> <modo>: Mostrar el contenido de una página
     Modos disponibles: basico, texto_plano

Comandos Generales:
   - ayuda: Mostrar esta ayuda
   - salir: Cerrar el navegador
        """)

def main():
    browser = WebBrowser()
    print("Bienvenido al Simulador de Navegador Web en Consola")
    print("Escribe 'ayuda' para ver la lista de comandos disponibles")
    
    while True:
        try:
            command = input("> ")
            if not browser.process_command(command):
                break
        except Exception as e:
            print(f"Error: {e}")
            print("Intente de nuevo o escriba 'ayuda' para ver los comandos disponibles")

    print("¡Hasta pronto!")

if __name__ == "__main__":
    main()
