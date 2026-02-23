from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import MergeInput, MergeOutput
import re


def merge_node(state: MergeInput, config: RunnableConfig, runtime: Runtime[Context]) -> MergeOutput:
    """
    title: 故事整合
    desc: 将标题、开篇、网友回复和楼主更新整合成完整论坛体小说，楼主回复穿插在楼层中
    integrations: 
    """
    ctx = runtime.context
    
    final_story_parts = []
    
    # 标题 - 支持"标题："前缀
    title_text = state.title.strip()
    if title_text.startswith("标题：") or title_text.startswith("标题:"):
        title_text = title_text.split("：", 1)[-1].split(":", 1)[-1].strip()
    final_story_parts.append(f"【标题】\n{title_text}\n")
    
    # 1楼（开篇）- 可能包含楼层号前缀
    opening_text = state.opening_post.strip()
    # 移除可能的楼层号前缀
    if re.match(r'^1楼\s+楼主[:：]', opening_text):
        # 提取楼层号后面的内容
        match = re.match(r'^1楼\s+楼主[:：]\s*(.+)', opening_text, re.DOTALL)
        if match:
            opening_text = match.group(1).strip()
    final_story_parts.append(f"1楼 楼主：\n{opening_text}\n\n")
    
    # 解析所有楼层（网友回复+楼主回复）
    all_floors = {}
    
    # 解析网友回复
    reply_lines = state.replies.split('\n')
    current_floor = None
    for line in reply_lines:
        line = line.strip()
        if not line:
            continue
        
        # 匹配楼层号（如：2楼 吃瓜群众：）
        floor_match = re.match(r'^(\d+)楼\s+(.+?)[:：]', line)
        if floor_match:
            if current_floor and current_floor['floor'] not in [11, 21, 31, 41]:
                all_floors[current_floor['floor']] = current_floor
            floor_num = int(floor_match.group(1))
            # 跳过11楼、21楼、31楼、41楼，这些是楼主回复的位置
            if floor_num not in [11, 21, 31, 41]:
                user_type = floor_match.group(2).strip()
                current_floor = {'floor': floor_num, 'user': user_type, 'content': ''}
            else:
                current_floor = None
        elif current_floor:
            # 楼中楼回复
            if line.startswith('>') or line.startswith('回复'):
                current_floor['content'] += f"\n> {line}"
            else:
                current_floor['content'] += f"\n{line}"
    
    if current_floor and current_floor['floor'] not in [11, 21, 31, 41]:
        all_floors[current_floor['floor']] = current_floor
    
    # 解析楼主回复
    update_lines = state.updates.split('\n')
    current_floor_num = None
    for line in update_lines:
        line = line.strip()
        if not line:
            continue
        
        # 匹配楼主楼层号（如：11楼 楼主：）
        floor_match = re.match(r'^(\d+)楼\s+楼主[:：]', line)
        if floor_match:
            floor_num = int(floor_match.group(1))
            if floor_num in [11, 21, 31, 41]:
                current_floor_num = floor_num
                all_floors[floor_num] = {'floor': floor_num, 'user': '楼主', 'content': ''}
        elif current_floor_num and all_floors.get(current_floor_num, {}).get('user') == '楼主':
            # 添加到当前楼层内容
            all_floors[current_floor_num]['content'] += f"\n{line}"
    
    # 按楼层号排序
    sorted_floors = sorted(all_floors.items(), key=lambda x: x[0])
    
    # 输出所有楼层
    for floor_num, floor in sorted_floors:
        final_story_parts.append(f"{floor['floor']}楼 {floor['user']}：\n{floor['content'].strip()}\n\n")
    
    final_story_parts.append("（全剧终）")
    
    final_story = "\n".join(final_story_parts)
    
    return MergeOutput(final_story=final_story)
