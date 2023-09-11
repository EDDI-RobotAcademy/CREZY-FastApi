import os
import sys
import importlib.util


def import_external_fastapi_project():
    mercenary_socket_server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../external/Mercenary-FastAPI')
    sys.path.append(mercenary_socket_server_path)

    print("mercenary_socket_server_path: ", mercenary_socket_server_path)

    for module_filename in os.listdir(os.path.join(mercenary_socket_server_path)):
        if module_filename.endswith('.py'):
            module_name = module_filename[:-3]
            module_path = os.path.join(mercenary_socket_server_path, module_filename)
            module_spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)


def import_external_socket_server_project():
    mercenary_socket_server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../external/Mercenary-FastAPI/app/includes/Mercenary-Socket-Server')
    sys.path.append(mercenary_socket_server_path)

    print("mercenary_socket_server_path: ", mercenary_socket_server_path)

    for module_filename in os.listdir(os.path.join(mercenary_socket_server_path)):
        if module_filename.endswith('.py'):
            module_name = module_filename[:-3]
            module_path = os.path.join(mercenary_socket_server_path, module_filename)
            module_spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)


def adjust_system_path():
    pass


def import_every_external_project():
    mercenary_fastapi_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '../external/Mercenary-FastAPI')

    for root, _, files in os.walk(mercenary_fastapi_path):
        for module_filename in files:
            if module_filename.endswith('.py') and module_filename != 'main.py':
                module_name = module_filename[:-3]
                module_path = os.path.join(root, module_filename)

                try:
                    module_spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(module_spec)
                    module_spec.loader.exec_module(module)

                except Exception as e:
                    print(f"모듈 {module_name} 로딩 중 오류 발생: {str(e)}")
