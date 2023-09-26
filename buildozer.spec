[app]
# Nome do pacote (package name)
package.name = camera_app

# Nome do aplicativo (título)
title = CameraApp

# Versão do aplicativo
version = 1.0.0

# (pacotes necessários, se houver)
requirements = kivy

# (ícone do aplicativo, se desejar)
#icon.filename = path/to/your/icon.png

# (arquivo principal do aplicativo)
source.dir = .

# (diretório onde os arquivos serão armazenados no dispositivo Android)
# Você pode querer mudar isso dependendo do seu aplicativo
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests,__pycache__

# (versão mínima do Android a ser suportada)
android.minapi = 21

# (permissões necessárias para acessar a câmera)
android.permissions = CAMERA
