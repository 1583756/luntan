import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.runtime import Runtime
from coze_coding_dev_sdk import LLMClient
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import OpeningInput, OpeningOutput


def opening_node(state: OpeningInput, config: RunnableConfig, runtime: Runtime[Context]) -> OpeningOutput:
    """
    title: 帖子开篇生成
    desc: 生成吸睛的标题和1楼内容，开篇即吸引
    integrations: 大语言模型
    """
    ctx = runtime.context
    
    cfg_file = os.path.join(os.getenv("COZE_WORKSPACE_PATH"), config['metadata']['llm_cfg'])
    with open(cfg_file, 'r') as fd:
        _cfg = json.load(fd)

    llm_config = _cfg.get("config", {})
    sp = _cfg.get("sp", "")
    up = _cfg.get("up", "")

    up_tpl = Template(up)
    user_prompt_content = up_tpl.render({"story_outline": state.story_outline, "theme": state.theme})
    
    client = LLMClient(ctx=ctx)
    
    messages = [
        SystemMessage(content=sp),
        HumanMessage(content=user_prompt_content)
    ]
    
    response = client.invoke(
        messages=messages,
        model=llm_config.get("model", "doubao-seed-2-0-pro-260215"),
        temperature=llm_config.get("temperature", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 2000),
        thinking=llm_config.get("thinking", "disabled")
    )
    
    content = ""
    if isinstance(response.content, str):
        content = response.content
    elif isinstance(response.content, list):
        if response.content and isinstance(response.content[0], str):
            content = " ".join(response.content)
        else:
            text_parts = [item.get("text", "") for item in response.content if isinstance(item, dict) and item.get("type") == "text"]
            content = " ".join(text_parts)
    
    lines = content.split("\n", 1)
    title = lines[0].strip() if lines else "论坛帖子"
    opening_post = lines[1].strip() if len(lines) > 1 else content.strip()
    
    return OpeningOutput(title=title, opening_post=opening_post)
