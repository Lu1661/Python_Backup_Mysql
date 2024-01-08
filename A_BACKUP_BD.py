import os
import datetime
import subprocess

def backup_database():
    try:
        # Ruta completa al ejecutable de mysqldump
        mysqldump_path = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\mysqldump"

        # Información de la base de datos
        host = '999.999.999.999'
        database = 'BASEDEDATOS'
        user = 'USUARIO'
        password = f'CONTRASEÑA@'

        # Nombre del archivo de backup
        fecha_actual = datetime.datetime.now().strftime("%Y%m%d")
        backup_file = f"C:\\Ingresa\\TuRuta\\Aqui\\backup_{fecha_actual}.sql"

        # Comando de backup con opción adicional para evitar el error
        command = f'"{mysqldump_path}" --column-statistics=0 -h {host} -u {user} -p"{password}" {database} > "{backup_file}"'

        # Ejecución del comando
        subprocess.run(command, shell=True)
        print("Backup realizado con éxito")

    except Exception as e:
        print("Error al realizar backup: ", e)

if __name__ == "__main__":
    backup_database()