# TIA Portal Openness Technical Documentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Sphinx](https://img.shields.io/badge/Sphinx-7.0+-green.svg)](https://www.sphinx-doc.org/)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-ready-orange.svg)](https://tia-portal-openness-docs.readthedocs.io/)

English | [中文](README.md)

## Overview

This project is a complete Chinese technical documentation for **Siemens TIA Portal Openness V17.0**, translated from the official documentation and built using **MkDocs + Material** theme.

TIA Portal Openness is an open engineering automation tool interface provided by Siemens, allowing users to programmatically access TIA Portal's functionality and automate engineering tasks.

## Features

- **Complete Chinese Translation** - Full Chinese localization based on official Siemens documentation
- **Rich Code Examples** - Extensive C# code examples with detailed explanations
- **Interface Screenshots** - 121 complete interface screenshots for better understanding
- **Multi-format Document Support** - Intelligent extraction for PDF, Word, PPT, Excel and more
- **Online Documentation** - Deployed on Read the Docs with search and navigation support

## Documentation Content

### Quick Start
- Task Description - Learn basic concepts and application scenarios of TIA Portal Openness
- Solution - Overview of the overall solution
- Working Modes - Detailed working mode explanation
- Create Application - Complete step-by-step creation guide

### Application Examples
- **Basic Project Generator** - Comprehensive guide to the basic project generator
- **TIA Portal Openness Demo** - Complete demo application documentation

### Appendix
- Services & Support - Technical support and resource links

## Quick Start

### Prerequisites

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Build Documentation

```bash
# Build with MkDocs
mkdocs build

# Local preview
mkdocs serve

# Or use Makefile
make html        # Build HTML
make clean       # Clean build artifacts
make help        # Show available commands
```

### Access Documentation

After building, open `http://127.0.0.1:8000` in your browser to preview.

## Project Structure

```
tia-openness-docs/
├── README.md                           # Chinese documentation
├── README_EN.md                        # English documentation
├── LICENSE                             # MIT License
├── mkdocs.yml                          # MkDocs configuration
├── requirements.txt                    # Python dependencies
├── .readthedocs.yaml                   # Read the Docs configuration
├── assets/                             # Static assets
│   └── favicon.svg
└── docs/                               # Documentation source files
    ├── index.md                        # Homepage
    ├── 01 任务.md
    ├── 02 解决方案.md
    ├── 03 工作模式.md
    ├── 04 创建新的 TIA Portal Openness 应用程序.md
    ├── 05 基础项目生成器.md
    ├── 06 TIA Portal Openness Demo Application.md
    ├── 07 附录.md
    ├── conf.py                         # Sphinx configuration
    └── images/                         # Documentation images
```

## Deployment

### Read the Docs Automatic Deployment

The project is configured for automatic deployment with Read the Docs:

1. Push code to GitHub
2. Read the Docs automatically builds
3. Access at https://tia-portal-openness-docs.readthedocs.io/

### Manual Deployment

```bash
# Build documentation
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Related Links

- [TIA Portal Openness Official Documentation](https://support.industry.siemens.com/cs/ww/en/view/108716692)
- [Siemens Industry Online Support](https://support.industry.siemens.com)
- [MkDocs Official Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

## Contributing

Issues and Pull Requests are welcome to improve this documentation.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Siemens official TIA Portal Openness technical documentation
- MkDocs and Material for MkDocs teams
- All contributors and supporters

---

**Note**: This documentation is translated from Siemens' official technical documentation for reference purposes only. For any questions, please refer to the [official documentation](https://support.industry.siemens.com/cs/ww/en/view/108716692).
