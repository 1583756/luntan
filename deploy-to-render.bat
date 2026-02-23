@echo off
chcp 65001 >nul
echo ================================
echo   一键部署到 Render 平台
echo ================================
echo.

REM 检查 git
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] 未检测到 git，请先安装 git
    echo 下载地址: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM 检查是否已配置 git
if not exist ".git" (
    echo [INFO] 初始化 git 仓库...
    git init
    git add .
    git commit -m "Initial commit: Forum Novel Generator"
    git branch -M main
    echo [SUCCESS] Git 仓库已初始化
) else (
    echo [SUCCESS] Git 仓库已存在
)

echo.
echo [INFO] 接下来的步骤：
echo.
echo 1. 创建 GitHub 仓库
echo    - 访问: https://github.com/new
echo    - 创建一个 Public 仓库
echo    - 仓庛建议: forum-novel-generator
echo.
echo 2. 推送代码到 GitHub
echo    在下方填入你的仓库地址
echo.

set /p REPO_URL="请输入你的 GitHub 仓库地址（如：https://github.com/username/repo.git）: "

if "%REPO_URL%"=="" (
    echo [ERROR] 仓库地址不能为空
    pause
    exit /b 1
)

echo.
echo [INFO] 推送代码到 GitHub...

REM 添加 remote
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    git remote set-url origin %REPO_URL%
) else (
    git remote add origin %REPO_URL%
)

REM 推送代码
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    goto success
) else (
    goto fail
)

:success
echo.
echo [SUCCESS] 代码已成功推送到 GitHub！
echo.
echo 3. 在 Render 部署
echo.
echo    请按照以下步骤操作：
echo.
echo    a) 访问: https://dashboard.render.com/
echo    b) 点击 New - Web Service
echo    c) 点击 Connect 连接你的 GitHub 仓库
echo    d) 选择刚创建的仓库
echo    e) 配置如下：
echo       - Name: forum-novel-generator
echo       - Runtime: Docker
echo       - Root Directory: .
echo       - Dockerfile Path: Dockerfile
echo       - Plan: 选择 Free
echo    f) 添加环境变量：
echo       - Key: COZE_WORKSPACE_PATH
echo       - Value: /app
echo    g) 点击 Create Web Service
echo.
echo 4. 等待部署完成
echo.
echo    - 部署通常需要 5-10 分钟
echo    - 可以在 Render 控制台查看进度
echo    - 部署完成后会显示一个网址，如：
echo      https://forum-novel-generator.onrender.com
echo.
echo 5. 访问你的应用
echo.
echo    直接在浏览器打开部署网址即可使用！
echo.
echo [SUCCESS] 部署完成！
echo.
echo [TIP] 提示：
echo    - 记得保存好你的应用网址
echo    - 可以直接分享网址给朋友
echo    - 手机、平板、电脑都能访问
echo    - 免费套餐有流量限制，注意监控使用量
goto end

:fail
echo.
echo [ERROR] 推送失败，请检查：
echo    1. GitHub 仓库地址是否正确
echo    2. 是否有 GitHub 账号权限
echo    3. 网络连接是否正常
echo.
echo 你可以手动推送：
echo    git remote add origin %REPO_URL%
echo    git push -u origin main

:end
echo.
echo ================================
echo   需要帮助？查看：云端部署指南.md
echo ================================
pause
