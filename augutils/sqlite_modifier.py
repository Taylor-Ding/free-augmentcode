import sqlite3
import shutil
import time
from utils.paths import get_db_path

def _create_backup(file_path: str) -> str:
    """
    创建指定文件的带时间戳的备份。
    
    参数:
        file_path (str): 要备份的文件的路径
        
    返回:
        str: 备份文件的路径
        
    格式: <文件名>.bak.<时间戳>
    """
    timestamp = int(time.time())
    backup_path = f"{file_path}.bak.{timestamp}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def clean_augment_data() -> dict:
    """
    从 SQLite 数据库中清除与 augment 相关的数据。
    在修改前创建备份。
    
    此函数执行以下操作：
    1. 获取 SQLite 数据库路径
    2. 创建数据库文件的备份
    3. 打开数据库连接
    4. 删除键包含 'augment' 的记录
    
    返回:
        dict: 包含操作结果的字典
        {
            'db_backup_path': str,  # 数据库备份文件的路径
            'deleted_rows': int     # 删除的行数
        }
    """
    db_path = get_db_path()
    
    # 修改前创建备份
    db_backup_path = _create_backup(db_path)
    
    # 连接到数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # 执行删除查询
        cursor.execute("DELETE FROM ItemTable WHERE key LIKE '%augment%'")
        deleted_rows = cursor.rowcount
        
        # 提交更改
        conn.commit()
        
        return {
            'db_backup_path': db_backup_path,
            'deleted_rows': deleted_rows
        }
    finally:
        # 始终关闭连接
        cursor.close()
        conn.close() 