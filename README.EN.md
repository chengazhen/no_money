# Cursor Pro Automation Tool User Guide

## Note
Recently, some users have sold this software on platforms like Xianyu. Please avoid such practices—there’s no need to earn money this way.

## License
This project is licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
This means you may:  
- **Share** — Copy and redistribute the material in any medium or format.  
But you must comply with the following conditions:
- **Non-commercial** — You may not use the material for commercial purposes.

## Video Tutorial
[Watch the tutorial video](https://www.bilibili.com/video/BV1QTckewELS/)

## Features
Automated account registration and token refreshing to free your hands.

## Download Link
[https://github.com/chengazhen/cursor-auto-free/releases](https://github.com/chengazhen/cursor-auto-free/releases)

## Important Notes
1. **Ensure you have Chrome installed. If not, [download here](https://www.google.com/intl/en_pk/chrome/).**  
2. **You must log into your account, regardless of its validity. Logged-in is mandatory.**  
3. **A stable internet connection is required, preferably via an overseas node. Do not enable global proxy.**

## Configuration Instructions
- Use a Cloudflare domain email. Search for instructions if needed.  
- **(Very Important)** Use temp-mail.plus email. Search for instructions if needed.  
- Forward Cloudflare emails to temp-mail.plus.  
- Download the `.env.example` file to the program's root directory and rename it to `.env`.

### Example `.env` file:
```bash
DOMAIN='xxxxx.me'    # Your email domain (search for Cloudflare email usage)
TEMP_MAIL='xxxxxx'   # Temporary email prefix (no suffix needed)
```
Example:
```bash
DOMAIN='wozhangsan.me'
TEMP_MAIL='ccxxxxcxx'
```
The program will randomly generate emails with the `@wozhangsan.me` suffix.

## How to Run the Program

### Mac
1. Open Terminal and navigate to the application directory.  
2. Grant execution permission:  
```bash
chmod +x ./CursorPro
```  
3. Run the program:
   - In Terminal:  
```bash
./CursorPro
```  
   - Or double-click the file in Finder.  

If errors occur, refer to [solutions](https://sysin.org/blog/macos-if-crashes-when-opening/).

### Windows
Double-click `CursorPro.exe`.

## How to Verify
After running the script, restart your editor. If the displayed account matches the log, it worked successfully.

## Usage Notes
1. Requirements:
   - Stable internet connection.
   - Sufficient system permissions.

2. During use:
   - Wait for the program to complete all operations.
   - Close the program only after seeing the "script completed" message.

## Common Issues
1. Program freezes:
   - Check your internet connection.
   - Restart the program.

## Disclaimer
This tool is for educational and research purposes only. Users bear full responsibility for any consequences. Commercial use is strictly prohibited. Violations of the license terms may result in legal action.

## Update Log
- **2025-01-09**: Added logs and auto-build feature.  
- **2025-01-10**: Switched to Cloudflare domain email.  
- **2025-01-11**: Added headless mode and proxy configuration through .env file.

Some source code is from [gpt-cursor-auto](https://github.com/hmhm2022/gpt-cursor-auto).
