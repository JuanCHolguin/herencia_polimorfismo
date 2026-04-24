# CONFIGURACIÓN GLOBAL (solo una vez en la máquina)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# (OPCIONAL) CONFIGURACIÓN LOCAL (solo si este repo necesita identidad distinta)
# Ejemplo: trabajo versus personal
git config --local user.name "Otro Nombre"
git config --local user.email "otro@email.com"

# INICIALIZAR PROYECTO
git init

# AÑADIR ARCHIVOS
git add .

# PRIMER COMMIT
git commit -m "primer commit"

# CONECTAR CON GITHUB
git remote add origin https://github.com/usuario/nombre-repo.git

# PRIMER PUSH
git branch -M master
git push -u origin master

# FLUJO DIARIO (DESPUÉS DE CONFIGURADO)
git add .
git commit -m "cambios realizados"
git push