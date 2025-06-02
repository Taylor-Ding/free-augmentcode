import os
import sys
from pathlib import Path


def get_home_dir() -> str:
    """
    获取用户在不同平台上的主目录。
    
    返回:
        str: 用户主目录的路径
    """
    return str(Path.home())


def get_app_data_dir() -> str:
    """
    获取不同平台上的应用程序数据目录。
    
    返回:
        str: 应用程序数据目录的路径
        
    特定平台的路径:
        - Windows: %APPDATA% (通常是 C:\\Users\\<用户名>\\AppData\\Roaming)
        - macOS: ~/Library/Application Support
        - Linux: ~/.local/share
    """
    if sys.platform == "win32":
        # Windows系统
        return os.getenv("APPDATA", "")
    elif sys.platform == "darwin":
        # macOS系统
        return os.path.join(str(Path.home()), "Library/Application Support")
    else:
        # Linux 及其他类 Unix 系统
        return os.path.join(str(Path.home()), ".local/share")


def get_storage_path() -> str:
    """
    获取不同平台上的 storage.json 文件路径。
    
    返回:
        str: storage.json 文件的路径
        
    特定平台的路径:
        - Windows: %APPDATA%/Code/User/globalStorage/storage.json
        - macOS: ~/Library/Application Support/Code/User/globalStorage/storage.json
        - Linux: ~/.config/Code/User/globalStorage/storage.json
    """
    if sys.platform == "win32":
        # Windows系统
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Code", "User", "globalStorage", "storage.json")
    elif sys.platform == "darwin":
        # macOS系统
        return os.path.join(str(Path.home()), "Library", "Application Support", "Code", "User", "globalStorage", "storage.json")
    else:
        # Linux 及其他类 Unix 系统
        return os.path.join(str(Path.home()), ".config", "Code", "User", "globalStorage", "storage.json")


def get_db_path() -> str:
    """
    获取不同平台上的 state.vscdb 文件路径。
    
    返回:
        str: state.vscdb 文件的路径
        
    特定平台的路径:
        - Windows: %APPDATA%/Code/User/globalStorage/state.vscdb
        - macOS: ~/Library/Application Support/Code/User/globalStorage/state.vscdb
        - Linux: ~/.config/Code/User/globalStorage/state.vscdb
    """
    if sys.platform == "win32":
        # Windows系统
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Code", "User", "globalStorage", "state.vscdb")
    elif sys.platform == "darwin":
        # macOS系统
        return os.path.join(str(Path.home()), "Library", "Application Support", "Code", "User", "globalStorage", "state.vscdb")
    else:
        # Linux 及其他类 Unix 系统
        return os.path.join(str(Path.home()), ".config", "Code", "User", "globalStorage", "state.vscdb")


def get_machine_id_path() -> str:
    """
    获取不同平台上的机器 ID 文件路径。
    
    返回:
        str: 机器 ID 文件的路径
        
    特定平台的路径:
        - Windows: %APPDATA%/Code/User/machineid
        - macOS: ~/Library/Application Support/Code/machineid
        - Linux: ~/.config/Code/User/machineid
    """
    if sys.platform == "win32":
        # Windows系统
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Code", "User", "machineid")
    elif sys.platform == "darwin":
        # macOS系统
        return os.path.join(str(Path.home()), "Library", "Application Support", "Code", "machineid")
    else:
        # Linux 及其他类 Unix 系统
        return os.path.join(str(Path.home()), ".config", "Code", "machineid")


def get_workspace_storage_path() -> str:
    """
    获取不同平台上的 workspaceStorage 目录路径。
    
    返回:
        str: workspaceStorage 目录的路径
        
    特定平台的路径:
        - Windows: %APPDATA%/Code/User/workspaceStorage
        - macOS: ~/Library/Application Support/Code/User/workspaceStorage
        - Linux: ~/.config/Code/User/workspaceStorage
    """
    if sys.platform == "win32":
        # Windows系统
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Code", "User", "workspaceStorage")
    elif sys.platform == "darwin":
        # macOS系统
        return os.path.join(str(Path.home()), "Library", "Application Support", "Code", "User", "workspaceStorage")
    else:
        # Linux 及其他类 Unix 系统
        return os.path.join(str(Path.home()), ".config", "Code", "User", "workspaceStorage") 