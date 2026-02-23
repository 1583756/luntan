import os
import json
from jinja2 import Template
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.runtime import Runtime
from coze_coding_dev_sdk import LLMClient
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import UpdateInput, UpdateOutput


def update_node(state: UpdateInput, config: RunnableConfig, runtime: Runtime[Context]) -> UpdateOutput:
    """
    title: 楼主更新生成
    desc: 生成楼主的回复，以"XX楼 楼主"的形式穿插在楼层中
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
    user_prompt_content = up_tpl.render({"story_outline": state.story_outline, "replies": state.replies})
    
    client = LLMClient(ctx=ctx)
    
    messages = [
        SystemMessage(content=sp),
        HumanMessage(content=user_prompt_content)
    ]
    
    response = client.invoke(
        messages=messages,
        model=llm_config.get("model", "doubao-seed-2-0-pro-260215"),
        temperature=llm_config.get("temperature", 0.9),
        max_completion_tokens=llm_config.get("max_completion_tokens", 1500),
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
    
    return UpdateOutput(updates=content)
