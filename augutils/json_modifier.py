import json
import os
import time
import shutil
from utils.paths import get_storage_path, get_machine_id_path
from utils.device_codes import generate_machine_id, generate_device_id

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

def modify_telemetry_ids() -> dict:
    """
    修改 VS Code storage.json 文件和 machine ID 文件中的遥测 ID。
    在修改前创建备份。
    
    此函数执行以下操作：
    1. 创建 storage.json 和 machine ID 文件的备份
    2. 读取 storage.json 文件
    3. 生成新的 machine ID 和 device ID
    4. 更新 storage.json 中的 telemetry.machineId 和 telemetry.devDeviceId 值
    5. 使用新的 machine ID 更新 machine ID 文件
    6. 保存修改后的文件
    
    返回:
        dict: 包含旧 ID、新 ID 和备份信息的字典
        {
            'old_machine_id': str,  # 旧的机器 ID
            'new_machine_id': str,  # 新的机器 ID
            'old_device_id': str,   # 旧的设备 ID
            'new_device_id': str,   # 新的设备 ID
            'storage_backup_path': str,  # storage.json 备份文件的路径
            'machine_id_backup_path': str # machine ID 备份文件的路径
        }
    """
    storage_path = get_storage_path()
    machine_id_path = get_machine_id_path()
    
    if not os.path.exists(storage_path):
        raise FileNotFoundError(f"Storage file not found at: {storage_path}")
    
    # 修改前创建备份
    storage_backup_path = _create_backup(storage_path)
    machine_id_backup_path = None
    if os.path.exists(machine_id_path):
        machine_id_backup_path = _create_backup(machine_id_path)
    
    # 读取当前的 JSON 内容
    with open(storage_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 存储旧值
    old_machine_id = data.get('telemetry.machineId', '')
    old_device_id = data.get('telemetry.devDeviceId', '')
    
    # 生成新的 ID
    new_machine_id = generate_machine_id()
    new_device_id = generate_device_id()
    
    # 更新 storage.json 中的值
    data['telemetry.machineId'] = new_machine_id
    data['telemetry.devDeviceId'] = new_device_id
    
    # 将修改后的内容写回 storage.json
    with open(storage_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    # 将新的 machine ID 写入 machine ID 文件
    with open(machine_id_path, 'w', encoding='utf-8') as f:
        f.write(new_device_id)
    
    return {
        'old_machine_id': old_machine_id,
        'new_machine_id': new_machine_id,
        'old_device_id': old_device_id,
        'new_device_id': new_device_id,
        'storage_backup_path': storage_backup_path,
        'machine_id_backup_path': machine_id_backup_path
    } 