"""
AI Data Tools - AI数据处理工具
支持数据转换、清洗、分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDataTools:
    """
    AI数据处理工具
    支持：转换、清洗、分析
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def convert_format(self, data: str, source: str, target: str) -> str:
        """转换格式"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下{source}格式数据转换为{target}格式：

{data[:2000]}

只返回转换后的数据："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def clean_data(self, data: List[Dict], rules: List[str] = None) -> Dict:
        """清洗数据"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(data[:20], ensure_ascii=False)
        rules_text = ", ".join(rules or ["去重", "空值处理", "格式统一"])

        prompt = f"""请清洗以下数据：

数据：{data_text}
规则：{rules_text}

请返回JSON格式：
{{
    "cleaned_data": [{{}}],
    "removed_count": 数量,
    "changes": ["变更说明"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"cleaned": content}

    def analyze_dataset(self, data: List[Dict]) -> Dict:
        """分析数据集"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(data[:20], ensure_ascii=False)

        prompt = f"""请分析以下数据集：

{data_text}

请返回JSON格式：
{{
    "summary": "总结",
    "statistics": {{"字段": "统计"}},
    "patterns": ["模式"],
    "anomalies": ["异常"],
    "visualizations": ["建议图表"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_schema(self, data: List[Dict]) -> Dict:
        """生成数据Schema"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(data[:10], ensure_ascii=False)

        prompt = f"""请根据以下数据生成Schema：

{data_text}

请返回JSON格式：
{{
    "schema": {{
        "type": "object",
        "properties": {{}}
    }},
    "description": "描述"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"schema": content}

    def transform_data(self, data: List[Dict], transformation: str) -> List[Dict]:
        """转换数据"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        data_text = json.dumps(data[:20], ensure_ascii=False)

        prompt = f"""请按以下要求转换数据：

数据：{data_text}
转换：{transformation}

只返回转换后的JSON数组："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"transformed": content}]

    def merge_datasets(self, datasets: List[List[Dict]], strategy: str = "append") -> List[Dict]:
        """合并数据集"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        datasets_text = json.dumps([d[:5] for d in datasets], ensure_ascii=False)

        prompt = f"""请按{strategy}策略合并以下数据集：

{datasets_text}

只返回合并后的JSON数组："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"merged": content}]


def create_tools(**kwargs) -> AIDataTools:
    """创建数据工具"""
    return AIDataTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Data Tools")
    print()

    # 测试
    data = [{"name": "张三", "age": 25}, {"name": "李四", "age": 30}]
    analysis = tools.analyze_dataset(data)
    print(json.dumps(analysis, ensure_ascii=False, indent=2))
