@echo off
chcp 65001 >nul
echo ================================
echo   论坛体小说生成器 - 二维码生成工具
echo ================================
echo.

set /p URL="请输入你的应用网址（示例：https://forum-novel-generator.onrender.com）: "

if "%URL%"=="" (
    echo ❌ 网址不能为空
    pause
    exit /b 1
)

echo.
echo 🔄 正在生成二维码...
echo.

python generate_qrcode.py "%URL%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================
    echo   生成完成！
    echo ================================
    echo.
    echo 📱 使用方法:
    echo    1. 打开 assets\qrcode.png
    echo    2. 用手机扫码
    echo    3. 开始使用论坛体小说生成器！
) else (
    echo.
    echo ❌ 生成失败，请检查：
    echo    1. 是否安装了 Python
    echo    2. 是否安装了 qrcode 库
    echo.
    echo 💡 安装 qrcode 库:
    echo    pip install qrcode
)

echo.
pause
