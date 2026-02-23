FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONPATH=/app:/app/src
ENV COZE_WORKSPACE_PATH=/app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖（增加超时和重试）
RUN pip install --no-cache-dir --timeout=1000 --retries=10 -r requirements.txt || \
    pip install --no-cache-dir --timeout=1000 -r requirements.txt

# 复制项目文件
COPY . .

# 暴露端口（Railway 会通过环境变量设置）
EXPOSE $PORT

# 启动命令（使用环境变量 PORT）
CMD ["sh", "-c", "python -u src/main.py -m http -p ${PORT:-5000}"]
