# Free AugmentCode

[English](#english) | [中文](#chinese)

# <a name="chinese"></a>中文版

Free AugmentCode 是一个用于清理AugmentCode相关数据的工具，可以在同一台电脑上无限次登录不同的账号，避免账号被锁定。

## 功能特性

- 📝 修改Telemetry ID
  - 重置设备 ID 和机器 ID
  - 自动备份原始 ID 文件
  - 生成新的随机 ID

- 🗃️ 数据库清理
  - 清理 SQLite 数据库中的特定记录
  - 自动备份数据库文件
  - 删除包含 'augment' 关键字的记录

- 💾 工作区存储管理
  - 清理工作区存储文件
  - 自动备份工作区数据

## 安装说明

1. 确保你的系统已安装 Python 3.10及以上
2. 克隆此仓库到本地：
   ```bash
   git clone https://github.com/yourusername/free-augmentcode.git
   cd free-augmentcode
   ```

## 使用方法

1. 退出AugmentCode插件
2. 完全退出 VS Code
3. 执行脚本：

```bash
python index.py
```

4. 重新启动 VS Code
5. AugmentCode 插件中使用新的邮箱进行登录

## 项目结构

```
free-augmentcode/
├── index.py              # 主程序入口
├── augutils/             # 工具类目录
│   ├── json_modifier.py      # JSON 文件修改工具
│   ├── sqlite_modifier.py    # SQLite 数据库修改工具
│   └── workspace_cleaner.py  # 工作区清理工具
└── utils/                # 通用工具目录
    └── paths.py             # 路径管理工具
```

## 代码流程图

```mermaid
graph TD
    A[Start index.py] --> B{Display System Paths};
    B --> C{Modify Telemetry IDs};
    C --&gt; D[Call modify_telemetry_ids];
    D --&gt; D_B1[Backup storage.json and machineid file];
    D_B1 --&gt; D_R[Read storage.json];
    D_R --&gt; D_G[Generate new IDs];
    D_G --&gt; D_U[Update storage.json];
    D_U --&gt; D_W[Write new machineid file];
    D_W --&gt; E{Clean SQLite Database};
    E --&gt; F[Call clean_augment_data];
    F --&gt; F_B1[Backup state.vscdb];
    F_B1 --&gt; F_C[Connect to DB];
    F_C --&gt; F_D[Delete 'augment' records];
    F_D --&gt; F_CM[Commit changes];
    F_CM --&gt; G{Clean Workspace Storage};
    G --&gt; H[Call clean_workspace_storage];
    H --&gt; H_B1[Backup workspaceStorage (zip)];
    H_B1 --&gt; H_D[Delete contents of workspaceStorage];
    H_D --&gt; I[End];
```

**流程图节点说明：**

- `A[Start index.py]`: 启动 `index.py` 脚本
- `B{Display System Paths}`: 显示系统路径信息
- `C{Modify Telemetry IDs}`: 修改遥测ID（设备ID和机器ID）
- `D[Call modify_telemetry_ids]`: 调用 `modify_telemetry_ids` 函数
- `D_B1[Backup storage.json and machineid file]`: 备份 `storage.json` 和 `machineid` 文件
- `D_R[Read storage.json]`: 读取 `storage.json` 文件内容
- `D_G[Generate new IDs]`: 生成新的设备ID和机器ID
- `D_U[Update storage.json]`: 更新 `storage.json` 文件中的ID
- `D_W[Write new machineid file]`: 将新的机器ID写入 `machineid` 文件
- `E{Clean SQLite Database}`: 清理SQLite数据库
- `F[Call clean_augment_data]`: 调用 `clean_augment_data` 函数
- `F_B1[Backup state.vscdb]`: 备份 `state.vscdb` 数据库文件
- `F_C[Connect to DB]`: 连接到SQLite数据库
- `F_D[Delete 'augment' records]`: 从数据库中删除包含 'augment' 关键字的记录
- `F_CM[Commit changes]`: 提交数据库更改
- `G{Clean Workspace Storage}`: 清理工作区存储
- `H[Call clean_workspace_storage]`: 调用 `clean_workspace_storage` 函数
- `H_B1[Backup workspaceStorage (zip)]`: 将 `workspaceStorage` 目录压缩备份为zip文件
- `H_D[Delete contents of workspaceStorage]`: 删除 `workspaceStorage` 目录中的所有内容
- `I[End]`: 程序结束

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

此项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

# <a name="english"></a>English Version

Free AugmentCode is a tool for cleaning AugmentCode-related data, allowing unlimited logins with different accounts on the same computer while avoiding account lockouts.

## Features

- 📝 Telemetry ID Modification
  - Reset device ID and machine ID
  - Automatic backup of original data
  - Generate new random IDs

- 🗃️ Database Cleanup
  - Clean specific records in SQLite database
  - Automatic database file backup
  - Remove records containing 'augment' keyword

- 💾 Workspace Storage Management
  - Clean workspace storage files
  - Automatic workspace data backup

## Installation

1. Ensure Python 3.10 or above is installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/free-augmentcode.git
   cd free-augmentcode
   ```

## Usage

1. Exit the AugmentCode plugin
2. Completely close VS Code
3. Run the script:

```bash
python index.py
```

4. Restart VS Code
5. Log in to the AugmentCode plugin with a new email

## Project Structure

```
free-augmentcode/
├── index.py              # Main program entry
├── augutils/             # Utility classes directory
│   ├── json_modifier.py      # JSON file modification tool
│   ├── sqlite_modifier.py    # SQLite database modification tool
│   └── workspace_cleaner.py  # Workspace cleanup tool
└── utils/                # Common utilities directory
    └── paths.py             # Path management tool
```

## Code Flowchart

```mermaid
graph TD
    A[Start index.py] --> B{Display System Paths};
    B --> C{Modify Telemetry IDs};
    C --&gt; D[Call modify_telemetry_ids];
    D --&gt; D_B1[Backup storage.json and machineid file];
    D_B1 --&gt; D_R[Read storage.json];
    D_R --&gt; D_G[Generate new IDs];
    D_G --&gt; D_U[Update storage.json];
    D_U --&gt; D_W[Write new machineid file];
    D_W --&gt; E{Clean SQLite Database};
    E --&gt; F[Call clean_augment_data];
    F --&gt; F_B1[Backup state.vscdb];
    F_B1 --&gt; F_C[Connect to DB];
    F_C --&gt; F_D[Delete 'augment' records];
    F_D --&gt; F_CM[Commit changes];
    F_CM --&gt; G{Clean Workspace Storage};
    G --&gt; H[Call clean_workspace_storage];
    H --&gt; H_B1[Backup workspaceStorage (zip)];
    H_B1 --&gt; H_D[Delete contents of workspaceStorage];
    H_D --&gt; I[End];
```

## Contributing

Issues and Pull Requests are welcome to help improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 