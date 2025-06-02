import os
import shutil
import time
import zipfile
import stat
from utils.paths import get_workspace_storage_path
from pathlib import Path

def remove_readonly(func, path, excinfo):
    """在删除过程中处理只读文件和目录"""
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception as e:
        return False
    return True

def force_delete_directory(path: Path) -> bool:
    """
    强制删除目录及其所有内容。
    成功则返回 True，否则返回 False。
    """
    try:
        if os.name == 'nt':
            # 对于 Windows，处理只读文件并使用长路径
            path_str = '\\\\?\\' + str(path.resolve())
            shutil.rmtree(path_str, onerror=remove_readonly)
        else:
            shutil.rmtree(path, onerror=remove_readonly)
        return True
    except Exception:
        return False

def clean_workspace_storage() -> dict:
    """
    创建备份后清理工作区存储目录。
    
    此函数执行以下操作：
    1. 获取工作区存储路径
    2. 创建目录中所有文件的 zip 备份
    3. 删除目录中的所有文件
    
    返回:
        dict: 包含操作结果的字典
        {
            'backup_path': str,  # 备份文件的路径
            'deleted_files_count': int # 删除的文件数量
        }
    """
    workspace_path = get_workspace_storage_path()
    
    if not os.path.exists(workspace_path):
        raise FileNotFoundError(f"Workspace storage directory not found at: {workspace_path}")
    
    # 转换为 Path 对象以便更好地处理路径
    workspace_path = Path(workspace_path)
    
    # 创建带时间戳的备份文件名
    timestamp = int(time.time())
    backup_path = f"{workspace_path}_backup_{timestamp}.zip"
    
    # 创建 zip 备份
    failed_compressions = []
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in workspace_path.rglob('*'):
            if file_path.is_file():
                try:
                    file_path_str = str(file_path)
                    if os.name == 'nt':
                        file_path_str = '\\\\?\\' + str(file_path.resolve())
                    
                    arcname = file_path.relative_to(workspace_path)
                    zipf.write(file_path_str, str(arcname))
                except (OSError, PermissionError, zipfile.BadZipFile) as e:
                    failed_compressions.append({
                        'file': str(file_path),
                        'error': str(e)
                    })
                    continue
    
    # 删除前统计文件数量
    total_files = sum(1 for _ in workspace_path.rglob('*') if _.is_file())
    
    # 删除目录中的所有文件
    failed_operations = []
    
    def handle_error(e: Exception, path: Path, item_type: str):
        failed_operations.append({
            'type': item_type,
            'path': str(path),
            'error': str(e)
        })

    # 首次尝试：一次性删除整个目录树
    if not force_delete_directory(workspace_path):
        # 如果批量删除失败，则尝试逐个文件删除的方法
        # 首先删除文件
        for file_path in workspace_path.rglob('*'):
            if file_path.is_file():
                try:
                    # 如果存在只读属性，则清除它
                    if os.name == 'nt':
                        file_path_str = '\\\\?\\' + str(file_path.resolve())
                        os.chmod(file_path_str, stat.S_IWRITE)
                    else:
                        os.chmod(str(file_path), stat.S_IWRITE)
                    
                    file_path.unlink(missing_ok=True)
                except (OSError, PermissionError) as e:
                    handle_error(e, file_path, 'file')

        # 从最深层到根目录删除目录
        dirs_to_delete = sorted(
            [p for p in workspace_path.rglob('*') if p.is_dir()],
            key=lambda x: len(str(x).split(os.sep)),
            reverse=True
        )
        
        for dir_path in dirs_to_delete:
            try:
                # 首先尝试强制删除
                if not force_delete_directory(dir_path):
                    # 如果强制删除失败，尝试常规删除
                    if os.name == 'nt':
                        dir_path_str = '\\\\?\\' + str(dir_path.resolve())
                        os.rmdir(dir_path_str)
                    else:
                        dir_path.rmdir()
            except (OSError, PermissionError) as e:
                handle_error(e, dir_path, 'directory')
    
    return {
        'backup_path': str(backup_path),
        'deleted_files_count': total_files,
        'failed_operations': failed_operations,
        'failed_compressions': failed_compressions
    } 