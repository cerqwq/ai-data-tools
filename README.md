# 📊 AI Data Tools

AI数据处理工具，支持数据转换、清洗、分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔄 格式转换
- 🧹 数据清洗
- 📊 数据分析
- 📋 Schema生成
- 🔧 数据转换
- 🔗 数据集合并

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_data_tools import create_tools

tools = create_tools()

# 格式转换
csv = tools.convert_format(json_data, "JSON", "CSV")

# 数据清洗
cleaned = tools.clean_data(data, ["去重", "空值处理"])

# 数据分析
analysis = tools.analyze_dataset(data)

# Schema生成
schema = tools.generate_schema(data)

# 数据转换
transformed = tools.transform_data(data, "将日期转为时间戳")

# 数据集合并
merged = tools.merge_datasets([data1, data2], "append")
```

## 📁 项目结构

```
ai-data-tools/
├── tools.py       # 数据工具核心
└── README.md
```

## 📄 许可证

MIT License
