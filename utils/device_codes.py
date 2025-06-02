import os
import uuid
import secrets


def generate_machine_id() -> str:
    """
    为机器 ID 生成一个随机的64个字符的十六进制字符串。
    类似于在 bash 中使用 /dev/urandom，但这里使用 Python 的加密函数。
    
    返回:
        str: 一个64个字符的十六进制字符串
    """
    # 生成32个随机字节 (将变为64个十六进制字符)
    random_bytes = secrets.token_bytes(32)
    # 转换为十六进制字符串
    return random_bytes.hex()


def generate_device_id() -> str:
    """
    为设备 ID 生成一个随机的 UUID v4。
    
    返回:
        str: 一个小写的 UUID v4 字符串，格式为：xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
        其中 x 是任何十六进制数字，y 是 8、9、A 或 B 中的一个
    """
    # 生成一个随机的 UUID v4
    device_id = str(uuid.uuid4())
    return device_id.lower()


if __name__ == "__main__":
    # 示例用法
    print(f"Machine ID: {generate_machine_id()}")
    print(f"Device ID: {generate_device_id()}") 