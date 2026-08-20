# TIA Portal Openness 技术文档

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Sphinx](https://img.shields.io/badge/Sphinx-7.0+-green.svg)](https://www.sphinx-doc.org/)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-ready-orange.svg)](https://tia-portal-openness-docs.readthedocs.io/)

[English](README_EN.md) | 中文

## 项目简介

本项目是西门子 **TIA Portal Openness V17.0** 的完整中文技术文档，基于官方文档翻译整理，使用 **MkDocs + Material** 主题构建。

TIA Portal Openness 是西门子提供的开放式工程自动化工具接口，允许用户通过编程方式访问 TIA Portal 的功能，实现自动化工程任务的自动化处理。

## 功能特性

- **完整中文翻译** - 基于西门子官方文档的完整中文本地化
- **丰富的代码示例** - 包含大量 C# 代码示例和详细讲解
- **界面截图** - 121 张完整界面截图辅助理解
- **多格式文档支持** - 支持 PDF、Word、PPT、Excel 等文档智能提取
- **在线文档** - 部署在 Read the Docs，支持搜索和导航

## 文档内容

### 快速入门
- 任务说明 - 了解 TIA Portal Openness 的基本概念和应用场景
- 解决方案 - 总体解决方案概述
- 工作模式 - 详细的工作模式说明
- 创建应用程序 - 完整的创建步骤指南

### 应用程序示例
- **Basic Project Generator** - 基础项目生成器详解
- **TIA Portal Openness Demo** - Demo 应用完整说明

### 附录
- 服务与支持 - 技术支持和资源链接

## 快速开始

### 环境准备

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

### 构建文档

```bash
# 使用 MkDocs 构建
mkdocs build

# 本地预览
mkdocs serve

# 或使用 Makefile
make html        # 构建 HTML
make clean       # 清理构建产物
make help        # 查看可用命令
```

### 访问文档

构建完成后，在浏览器中打开 `http://127.0.0.1:8000` 进行预览。

## 项目结构

```
tia-openness-docs/
├── README.md                           # 中文说明文档
├── README_EN.md                        # 英文说明文档
├── LICENSE                             # MIT 许可证
├── mkdocs.yml                          # MkDocs 配置
├── requirements.txt                    # Python 依赖
├── .readthedocs.yaml                   # Read the Docs 配置
├── assets/                             # 静态资源
│   └── favicon.svg
└── docs/                               # 文档源文件
    ├── index.md                        # 首页
    ├── 01 任务.md
    ├── 02 解决方案.md
    ├── 03 工作模式.md
    ├── 04 创建新的 TIA Portal Openness 应用程序.md
    ├── 05 基础项目生成器.md
    ├── 06 TIA Portal Openness Demo Application.md
    ├── 07 附录.md
    ├── conf.py                         # Sphinx 配置
    └── images/                         # 文档图片
```

## 部署

### Read the Docs 自动部署

项目配置了 Read the Docs 自动部署：

1. 推送代码到 GitHub
2. Read the Docs 自动构建
3. 访问 https://tia-portal-openness-docs.readthedocs.io/

### 手动部署

```bash
# 构建文档
mkdocs build

# 部署到 GitHub Pages
mkdocs gh-deploy
```

## 相关链接

- [TIA Portal Openness 官方文档](https://support.industry.siemens.com/cs/ww/en/view/108716692)
- [西门子工业在线支持](https://support.industry.siemens.com)
- [MkDocs 官方文档](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

## 贡献

欢迎提交 Issue 和 Pull Request 来改进本文档。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 致谢

- 西门子官方 TIA Portal Openness 技术文档
- MkDocs 和 Material for MkDocs 团队
- 所有贡献者和支持者

---

**注意**: 本文档基于西门子官方技术文档翻译，仅供参考。如有疑问，请参考[官方文档](https://support.industry.siemens.com/cs/ww/en/view/108716692)。
