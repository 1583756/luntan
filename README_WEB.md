# 论坛体小说生成器 - Web应用

![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![状态](https://img.shields.io/badge/状态-可用-success)

一个基于LangGraph的论坛体小说生成工作流，提供友好的Web界面，让你轻松生成高质量的论坛体小说！

## ✨ 特性

- 🎨 **美观的Web界面** - 渐变紫色主题，响应式设计
- 📱 **多端支持** - 支持手机、平板、电脑
- ⚡ **一键生成** - 输入主题，点击生成
- 📋 **一键复制** - 快速复制小说内容
- 💾 **一键下载** - 下载为txt文件
- 🏷️ **快速示例** - 预设主题，一键填入
- 🔄 **自动保存** - 下载功能自动保存

## 🚀 快速开始

### 方式1：使用启动脚本（推荐）

#### Linux/Mac用户：
```bash
./start.sh
```

#### Windows用户：
```bat
start.bat
```

### 方式2：手动启动

```bash
python src/main.py -m http -p 5000
```

### 方式3：指定端口

```bash
python src/main.py -m http -p 8080
```

## 🌐 访问界面

启动服务后，在浏览器中打开：

- **主页**: http://localhost:5000
- **Web界面**: http://localhost:5000/assets/index.html
- **API文档**: http://localhost:5000/docs
- **健康检查**: http://localhost:5000/health

## 📱 使用方法

### 1. 输入主题

在输入框中输入你想要的小说主题，例如：
```
我好像做了一件很不体面的事，双男主BL小说
```

### 2. 点击生成

点击"✨ 生成小说"按钮，等待10-30秒

### 3. 查看结果

生成完成后，会显示完整的论坛体小说

### 4. 保存小说

- 点击"📋 复制"复制到剪贴板
- 点击"💾 下载"保存为txt文件

## 🎯 推荐主题

### 复仇类
```
我是为了报复才接近他的，结果自己栽进去了，双男主BL小说
```

### 悬疑类
```
室友昨天晚上带回一个快递，拆开里面是一把带血的斧头，双男主BL小说
```

### 校园类
```
我在图书馆遇到了暗恋的学长，双男主BL小说
```

### 职场类
```
我好像做了一件很不体面的事，双男主BL小说
```

### 日常类
```
我昨天晚上做了一件坏事，双男主BL小说
```

## 📊 生成效果

生成的论坛体小说特点：
- ✅ 吸睛标题（5-20字，有悬念）
- ✅ 完整楼层（2-41楼连续）
- ✅ 楼主回复分散（11楼、21楼、31楼、41楼）
- ✅ 结局内容分散（不挤在一楼）
- ✅ 网友类型丰富（吃瓜群众、嗑学家、课代表等）
- ✅ 内容质量高（每条回复都有价值）

## 🔧 技术架构

- **后端**: FastAPI + LangGraph + LangChain
- **前端**: HTML + CSS + JavaScript（原生，无依赖）
- **大模型**: coze-coding-dev-sdk（豆包/DeepSeek/Kimi等）
- **部署**: 可本地运行，也可部署到服务器

## 📁 项目结构

```
项目根目录/
├── src/
│   ├── graphs/              # 工作流代码
│   │   ├── state.py
│   │   ├── graph.py
│   │   └── nodes/
│   └── main.py              # 服务入口
├── config/                  # 配置文件
│   ├── outline_llm_cfg.json
│   ├── opening_llm_cfg.json
│   ├── replies_llm_cfg.json
│   └── update_llm_cfg.json
├── assets/                  # 前端文件
│   ├── index.html           # Web界面
│   └── 使用说明.md
├── start.sh                 # Linux/Mac启动脚本
├── start.bat                # Windows启动脚本
└── README.md                # 本文件
```

## 🌐 部署到外网

### 🎯 方案1：一键部署到 Render（推荐，完全免费）

#### 超简单三步：

1. **运行部署脚本**

   Linux/Mac:
   ```bash
   chmod +x deploy-to-render.sh
   ./deploy-to-render.sh
   ```

   Windows:
   ```bat
   deploy-to-render.bat
   ```

2. **在 Render 创建服务**

   - 访问: https://dashboard.render.com/
   - 点击 "New" → "Web Service"
   - 连接你的 GitHub 仓库
   - 配置如下：
     - Name: `forum-novel-generator`
     - Runtime: `Docker`
     - Plan: 选择 `Free`
   - 添加环境变量：
     - Key: `COZE_WORKSPACE_PATH`
     - Value: `/app`
   - 点击 "Create Web Service"

3. **等待部署完成**

   - 部署需要 5-10 分钟
   - 部署完成后会得到一个网址，如：
     ```
     https://forum-novel-generator.onrender.com
     ```

4. **访问应用**

   直接在浏览器打开网址即可使用！

**优势**：
- ✅ 完全免费
- ✅ 自动 HTTPS
- ✅ 自动重启
- ✅ 持久运行
- ✅ 支持自定义域名

**详细教程**: 查看 `云端部署指南.md`

---

### ⚡ 方案2：使用 ngrok（临时测试，最简单）

如果你只是想快速测试给别人看：

1. **安装 ngrok**

   - Windows: https://ngrok.com/download
   - Mac: `brew install ngrok`
   - Linux: 从官网下载

2. **启动服务**

   ```bash
   ./start.sh
   ```

3. **映射端口**

   新开一个终端：

   ```bash
   ngrok http 5000
   ```

4. **分享链接**

   ngrok 会显示一个公网地址，如：
   ```
   https://abc123.ngrok.io
   ```

   把这个地址分享给朋友即可！

**注意**: ngrok 的地址每次重启都会改变，适合临时测试。

---

### ☁️ 方案3：部署到 Railway（完全免费）

1. 访问 https://railway.app
2. 点击 "Start a new project"
3. 连接 GitHub 仓库
4. 添加环境变量：`COZE_WORKSPACE_PATH=/app`
5. 点击 Deploy
6. 等待 3-5 分钟，获取访问地址

**详细教程**: 查看 `云端部署指南.md`

---

### 🏠 方案4：云服务器部署

适合需要长期稳定运行、自定义配置的场景。

#### 推荐平台：

- 阿里云（新用户有优惠）
- 腾讯云
- 华为云
- AWS（有免费套餐）
- DigitalOcean（$5/月）

#### 部署步骤：

```bash
# 1. 上传代码到服务器
scp -r /path/to/project user@server:/path/

# 2. SSH连接服务器
ssh user@server
cd /path/to/project

# 3. 安装依赖
pip install -r requirements.txt

# 4. 后台启动服务
nohup python src/main.py -m http -p 5000 > /dev/null 2>&1 &

# 5. 开放端口
ufw allow 5000  # Ubuntu/Debian
# 或
firewall-cmd --permanent --add-port=5000/tcp  # CentOS/RHEL
firewall-cmd --reload

# 6. 访问
http://你的服务器IP:5000
```

**详细教程**: 查看 `云端部署指南.md`

---

## 📱 部署对比

| 方案 | 成本 | 难度 | 稳定性 | 适用场景 |
|------|------|------|--------|----------|
| **Render** | 免费 | ⭐⭐ | ⭐⭐⭐⭐⭐ | 长期使用 ⭐推荐 |
| **Railway** | 免费 | ⭐⭐ | ⭐⭐⭐⭐ | 长期使用 |
| **ngrok** | 免费 | ⭐ | ⭐⭐ | 临时测试 |
| **云服务器** | $5+/月 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 企业使用 |

---

## 🎉 推荐方案

**如果你想要：**

- 🚀 **最快部署** → ngrok（3分钟）
- 💰 **免费长期** → Render（10分钟）
- 🏢 **稳定企业** → 云服务器
- 🔧 **高度定制** → 云服务器

---

## 💡 小贴士

1. **记住网址** - 部署成功后保存好你的应用地址
2. **分享方式** - 可以直接分享网址，也可以生成二维码
3. **自定义域名** - 云服务可以绑定自己的域名
4. **监控流量** - 免费套餐有流量限制，注意监控使用量

**详细部署教程**: 查看 `云端部署指南.md`

## 📖 API使用

如果你想通过编程方式使用：

### 生成小说
```bash
curl -X POST "http://localhost:5000/run" \
  -H "Content-Type: application/json" \
  -d '{"theme": "你的主题"}'
```

### Python示例
```python
import requests

response = requests.post(
    "http://localhost:5000/run",
    json={"theme": "我好像做了一件很不体面的事"}
)
result = response.json()
print(result["final_story"])
```

## 🆘 常见问题

### Q: 启动失败怎么办？
A: 检查Python版本（3.8+）和依赖是否安装完整

### Q: 生成很慢怎么办？
A: 生成需要10-30秒，请耐心等待，或者检查网络连接

### Q: 如何修改生成内容？
A: 修改 `config/` 目录下的JSON配置文件

### Q: 可以自定义结局类型吗？
A: 可以！在主题中直接说明，如："HE结局"、"BE结局"

### Q: 支持局域网访问吗？
A: 支持！使用 `http://你的局域网IP:5000` 访问

## 📞 技术支持

- 查看日志: `/app/work/logs/bypass/app.log`
- 查看API文档: http://localhost:5000/docs
- 查看使用说明: `assets/使用说明.md`

## 📄 许可证

本项目仅供学习和个人使用。

## 🙏 致谢

- LangGraph
- LangChain
- FastAPI
- coze-coding-dev-sdk

---

**享受你的论坛体小说生成之旅！** 🎉

**快速开始**: `./start.sh` （Linux/Mac）或 `start.bat` （Windows）
