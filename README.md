# Cursor Pro 自动化工具

<div align="center">

[![Release](https://img.shields.io/github/v/release/chengazhen/cursor-auto-free?style=flat-square&logo=github&color=blue)](https://github.com/chengazhen/cursor-auto-free/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square&logo=bookstack)](https://github.com/chengazhen/cursor-auto-free/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/chengazhen/cursor-auto-free?style=flat-square&logo=github)](https://github.com/chengazhen/cursor-auto-free/stargazers)

[中文](#中文) | [English](#english) 
<p align="center">
  <img src="./screen/logo.png" alt="Cursor Pro Logo" width="200"/>
</p>

</div>

## 🔄 更新日志
<details>
<summary>v0.0.7 - 快照</summary>
1. 抓包获取账号变成Pro版本<br>
<p align="center">
  <img src="./screen/cursor_2025-01-08_18-33-24.png" alt="v0.0.7" width="600"/>
</p><br>
<p align="center">
  <img src="./screen/cursor_2025-01-08_18-40-32.png" alt="v0.0.7" width="600"/>
</p><br>
</details>

<details>
<summary>v0.0.6</summary>
1. 修复了无法获取邮箱验证码的问题<br>
2. 增加了机器ID重置功能<br>
3. 增加了进度条显示
</details>

<details>
<summary>v0.0.5</summary>
1. 增加了 log 日志，方便调试
2. 增加了退出cursor
3. 增加了自动构建功能
</details>

## 中文

## 🚀 功能介绍
自动注册账号，自动刷新本地token，解放双手。

## ⬇️ 下载地址
https://github.com/chengazhen/cursor-auto-free/releases

## ⚠️ 重要提示
1. **确保已安装 Chrome 浏览器**
   - 如果未安装，请从[官方网站下载](https://www.google.com/intl/en_pk/chrome/)

2. **必须先完成账号登录**
   - 不论账号是否有效，必须先完成登录步骤

3. **网络要求**
   - 需要稳定的网络连接
   - 建议使用国外节点
   - ⚠️ 切勿开启全局代理

## 🛠️ 构建使用
### Win / Mac / Linux 通用

<p align="center">
  <img src="./screen/build_2025-01-04_11-02-45.png" alt="构建步骤 1" width="400"/>
  <img src="./screen/build_2025-01-04_11-04-43.png" alt="构建步骤 2" width="600"/>
</p>

```bash
# 根据您的操作系统选择以下任一方式构建：
Windows: build.bat
macOS:   build.mac.command
Linux:   build.sh
```

### .env文件中配置Chrome路径
```bash
CHROME_PATH=
```

## 📱 运行方法

### 更直觀的查看進度條
<p align="center">
  <img src="./screen/run_2025-01-04_23-26-22.gif" alt="Run Step 1" width="600"/>
</p>
<details>
<summary>進度條</summary>
<p align="center">
  <img src="./screen/run_2025-01-04_23-26-57.png" alt="Run Step 2" width="600"/>
  <img src="./screen/run_2025-01-04_23-28-29.png" alt="Run Step 3" width="600"/>
  <img src="./screen/run_2025-01-04_23-28-08.png" alt="Run Step 4" width="600"/>
  </p>
</details>


### macOS
1. 打开终端，进入应用目录
2. 授权执行权限：
```bash
chmod +x ./CursorPro
```
3. 运行程序：
```bash
./CursorPro
```
或直接在访达（Finder）中双击运行

> 💡 如遇到启动问题，请参考[解决方案](https://sysin.org/blog/macos-if-crashes-when-opening/)

<p align="center">
  <img src="./screen/c29ea438-ee74-4ba1-bbf6-25e622cdfad5.png" alt="macOS 错误示例" width="350"/>
</p>

### Windows
直接双击运行 `CursorPro.exe`

## ✅ 验证方法
运行脚本完成后，重启编辑器，确认账号信息与脚本输出日志一致：

<p align="center">
  <img src="./screen/截屏2025-01-04 09.44.48.png" alt="验证成功示例" width="350"/>
</p>

## 📝 使用注意事项

1. **运行环境要求**
   - 稳定的网络连接
   - 足够的系统权限

2. **使用过程中**
   - 请勿手动关闭浏览器窗口
   - 耐心等待程序自动完成操作
   - 看到"脚本执行完毕"提示后再关闭程序

## ❓ 常见问题解决

1. **程序运行卡住**
   - 检查网络连接
   - 重启程序重试

## ⚖️ 免责声明
本工具仅供学习研究使用，请遵守相关服务条款。使用本工具产生的任何后果由使用者自行承担。
仓库核心源码来自[gpt-cursor-auto](https://github.com/hmhm2022/gpt-cursor-auto)；自行优化了验证和邮箱注册逻辑；解决了无法获取邮箱验证码的问题。

---

> 仓库源码来自开源；自行优化了验证和邮箱注册逻辑；解决了无法获取邮箱验证码的问题。

---
## English

## 🚀 Features
Automatic account registration and local token refresh, hands-free operation.

## ⬇️ Download
https://github.com/chengazhen/cursor-auto-free/releases

## ⚠️ Important Notes
1. **Ensure Chrome Browser is Installed**
   - If not installed, download from [Official Website](https://www.google.com/intl/en_pk/chrome/)

2. **Account Login Required**
   - Must complete login first, regardless of account validity

3. **Network Requirements**
   - Stable internet connection required
   - International network node recommended
   - ⚠️ Do not enable global proxy

## 🛠️ Build Instructions
### For Win / Mac / Linux

<p align="center">

  <img src="./screen/build_2025-01-04_11-02-45.png" alt="Build Step 1" width="400"/>
  <img src="./screen/build_2025-01-04_11-04-43.png" alt="Build Step 2" width="600"/>
</p>

```bash
# Choose the appropriate build method for your OS:
Windows: build.bat
macOS:   build.mac.command
Linux:   build.sh
```

### .env file configuration
```bash
CHROME_PATH=
```

## 📱 Running Instructions

### Show Progress Bar
<p align="center">
  <img src="./screen/run_2025-01-04_23-26-22.gif" alt="Run Step 1" width="600"/>
</p>
<details>
<summary>Progress</summary>
<p align="center">
  <img src="./screen/run_2025-01-04_23-26-57.png" alt="Run Step 2" width="600"/>
  <img src="./screen/run_2025-01-04_23-28-29.png" alt="Run Step 3" width="600"/>
  <img src="./screen/run_2025-01-04_23-28-08.png" alt="Run Step 4" width="600"/>
  </p>
</details>

### macOS
1. Open terminal and navigate to application directory
2. Grant execution permissions:
```bash
chmod +x ./CursorPro
```
3. Run the program:
```bash
./CursorPro
```
Or double-click in Finder to run

> 💡 If you encounter startup issues, check the [Solution Guide](https://sysin.org/blog/macos-if-crashes-when-opening/)

<p align="center">
  <img src="./screen/c29ea438-ee74-4ba1-bbf6-25e622cdfad5.png" alt="macOS Error Example" width="350"/>
</p>

### Windows
Double-click `CursorPro.exe` to run

## ✅ Verification
After running the script, restart your editor and verify that the account information matches the script output log:

<p align="center">
  <img src="./screen/截屏2025-01-04 09.44.48.png" alt="Verification Success Example" width="350"/>
</p>

## 📝 Usage Notes

1. **System Requirements**
   - Stable network connection
   - Sufficient system permissions

2. **During Operation**
   - Do not manually close browser windows
   - Wait patiently for automatic completion
   - Close program only after seeing "Script Execution Complete"

## ❓ Troubleshooting

1. **Program Freezes**
   - Check network connection
   - Restart the program

## ⚖️ Disclaimer
This tool is for learning and research purposes only. Please comply with relevant terms of service. Users assume all responsibility for any consequences of using this tool.
Git Core Source Code: [gpt-cursor-auto](https://github.com/hmhm2022/gpt-cursor-auto)；Optimized verification and email registration logic; solved the problem of not being able to retrieve email verification codes.

---

> Repository source code is open-source; verification and email registration logic optimized; fixed email verification code retrieval issues. 
