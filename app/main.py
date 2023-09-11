import importlib
import os
from multiprocessing import Process

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.crawling.crawling import lyrics_crawling
from app.import_external_lib import import_external_fastapi_project, import_external_socket_server_project, \
    import_every_external_project
# from config.config import set_project_dir

app = FastAPI()

load_dotenv()

origins = os.getenv("ORIGINS_HOST")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lyrics_crawling)

import_every_external_project()

import os
import importlib

script_directory = os.path.dirname(__file__)
print("project_importer script_directory: ", script_directory)

module_path = "../external/Mercenary-FastAPI/app/socket_server"
absolute_module_path = os.path.abspath(os.path.join(script_directory, module_path))
relative_module_path = os.path.relpath(absolute_module_path, os.path.abspath(os.getcwd()))
relative_generator_module_path_for_importlib = relative_module_path.replace(os.path.sep, ".").lstrip(".")
relative_generator_module_path_for_importlib += ".generator"
print("relative_generator_module_path_for_importlib: ", relative_generator_module_path_for_importlib)

generator_module = importlib.import_module(relative_generator_module_path_for_importlib)

module_path = "../external/Mercenary-FastAPI/app/system_queue"
absolute_module_path = os.path.abspath(os.path.join(script_directory, module_path))
relative_module_path = os.path.relpath(absolute_module_path, os.path.abspath(os.getcwd()))
relative_system_queue_module_path_for_importlib = relative_module_path.replace(os.path.sep, ".").lstrip(".")
relative_system_queue_module_path_for_importlib += ".queue"
print("relative_system_queue_module_path_for_importlib: ", relative_system_queue_module_path_for_importlib)

system_queue_module = importlib.import_module(relative_system_queue_module_path_for_importlib)

module_path = "../external/Mercenary-FastAPI/app/socket_server/router"
absolute_module_path = os.path.abspath(os.path.join(script_directory, module_path))
relative_module_path = os.path.relpath(absolute_module_path, os.path.abspath(os.getcwd()))
relative_sock_serv_router_module_path_for_importlib = relative_module_path.replace(os.path.sep, ".").lstrip(".")
relative_sock_serv_router_module_path_for_importlib += ".socket_server_router"
print("relative_socket_server_router_module_path_for_importlib: ", relative_sock_serv_router_module_path_for_importlib)

socket_server_router_module = importlib.import_module(relative_sock_serv_router_module_path_for_importlib)
app.include_router(socket_server_router_module.socket_server_router)


if __name__ == '__main__':
    main_process_id = os.getpid()
    print(f"현재 프로세스의 ID: {main_process_id}")

    socket_server_process = Process(target=generator_module.run_socket_server,
                                    args=(system_queue_module.fastapi_queue,
                                          system_queue_module.socket_server_queue,
                                          main_process_id, ))
    socket_server_process.start()
    print("socket_server_process: ", socket_server_process)

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
