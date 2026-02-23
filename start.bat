@echo off
chcp 65001 >nul
echo =========================================
echo   论坛体小说生成器
echo =========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 错误：未检测到Python，请先安装Python
    pause
    exit /b 1
)

echo ✅ Python已安装
echo.

REM 默认端口
set PORT=5000

REM 检查是否指定了端口参数
if not "%~1"=="" (
    set PORT=%~1
)

echo 🚀 正在启动服务...
echo 📡 服务端口: %PORT%
echo 🌐 访问地址: http://localhost:%PORT%
echo 📱 Web界面: http://localhost:%PORT/assets/index.html
echo.
echo ⚠️  按 Ctrl+C 停止服务
echo.
echo =========================================
echo.

REM 启动服务
python src/main.py -m http -p %PORT%

pause
