import os
import sys
import subprocess
import time
import platform
import signal
import pkg_resources

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
VENV_DIR = os.path.join(BACKEND_DIR, "agrigest")

def is_running_in_venv():
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path and os.path.normcase(os.path.abspath(venv_path)) == os.path.normcase(os.path.abspath(VENV_DIR)):
        return True
    if os.path.normcase(os.path.abspath(sys.prefix)) == os.path.normcase(os.path.abspath(VENV_DIR)):
        return True
    return False

def create_venv():
    if is_running_in_venv():
        print("Já está rodando dentro do ambiente virtual 'agrigest'.")
        return

    if not os.path.exists(VENV_DIR):
        print("Criando ambiente virtual 'agrigest' no backend...")
        subprocess.check_call([sys.executable, "-m", "venv", "agrigest"], cwd=BACKEND_DIR)
    else:
        print("Ambiente virtual 'agrigest' já existe. Use o Python do venv para rodar o backend.")

def get_installed_packages():
    installed = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return installed

def install_backend_deps():
    print("Instalando dependências Python do backend...")
    if platform.system() == "Windows":
        pip_exec = os.path.join(VENV_DIR, "Scripts", "pip.exe")
    else:
        pip_exec = os.path.join(VENV_DIR, "bin", "pip")

    requirements_path = os.path.join(BASE_DIR, "requirements.txt")
    with open(requirements_path, "r") as f:
        req_lines = f.read().splitlines()

    installed = get_installed_packages()
    to_install = []

    for line in req_lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        pkg_name = line.split("==")[0].lower()
        if pkg_name not in installed:
            to_install.append(line)

    if to_install:
        print(f"Pacotes faltantes detectados: {to_install}")
        subprocess.check_call([pip_exec, "install"] + to_install)
    else:
        print("Todas as dependências Python já estão instaladas.")

def install_frontend_deps():
    node_modules_dir = os.path.join(FRONTEND_DIR, "node_modules")
    env = os.environ.copy()
    env["PATH"] = r"C:\Program Files\nodejs;" + env.get("PATH", "")
    if not os.path.exists(node_modules_dir):
        print("Instalando dependências npm do frontend...")
        subprocess.check_call(["npm.cmd", "install"], cwd=FRONTEND_DIR, env=env)
    else:
        print("Dependências npm já instaladas.")

    # Garante que react-scripts está instalado
    try:
        subprocess.check_call(["npm.cmd", "list", "react-scripts"], cwd=FRONTEND_DIR, env=env)
    except subprocess.CalledProcessError:
        print("react-scripts não encontrado, instalando...")
        subprocess.check_call(["npm.cmd", "install", "react-scripts"], cwd=FRONTEND_DIR, env=env)



def run_backend():
    print("Iniciando backend...")
    if platform.system() == "Windows":
        python_exec = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        python_exec = os.path.join(VENV_DIR, "bin", "python")
    return subprocess.Popen(
        [python_exec, "-m", "uvicorn", "main:app", "--reload"],
        cwd=BACKEND_DIR,
    )

def run_frontend():
    print("Iniciando frontend...")
    return subprocess.Popen(
        ["npm", "start"],
        cwd=FRONTEND_DIR,
        shell=(platform.system() == "Windows"),
    )

def main():
    backend_proc = None
    frontend_proc = None

    try:
        create_venv()
        install_backend_deps()

        # Testa se tkinter está disponível e avisa se não estiver
        try:
            import tkinter
        except ImportError:
            print("Aviso: tkinter não está disponível no ambiente Python.")
            print("Ele é parte da biblioteca padrão, mas pode não estar instalado corretamente.")

        install_frontend_deps()

        backend_proc = run_backend()
        frontend_proc = run_frontend()

        print("Backend e frontend rodando. Pressione Ctrl+C para parar.")

        while True:
            if backend_proc.poll() is not None:
                print("Backend parou.")
                break
            if frontend_proc.poll() is not None:
                print("Frontend parou.")
                break
            time.sleep(1)

    except subprocess.CalledProcessError as e:
        print(f"Erro durante instalação ou execução: {e}")
        print("Verifique seu ambiente e tente novamente.")

    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Encerrando...")

    finally:
        for proc in [backend_proc, frontend_proc]:
            if proc and proc.poll() is None:
                if platform.system() == "Windows":
                    proc.send_signal(signal.CTRL_BREAK_EVENT)
                else:
                    proc.send_signal(signal.SIGINT)
                proc.wait()

        print("Todos processos finalizados.")

if __name__ == "__main__":
    main()
