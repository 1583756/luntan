from langgraph.graph import StateGraph, END
from langgraph.runtime import Runtime
from graphs.state import (
    GlobalState,
    GraphInput,
    GraphOutput
)
from graphs.nodes.outline_node import outline_node
from graphs.nodes.opening_node import opening_node
from graphs.nodes.replies_node import replies_node
from graphs.nodes.update_node import update_node
from graphs.nodes.merge_node import merge_node

builder = StateGraph(GlobalState, input_schema=GraphInput, output_schema=GraphOutput)

builder.add_node("outline_node", outline_node, metadata={"type": "agent", "llm_cfg": "config/outline_llm_cfg.json"})
builder.add_node("opening_node", opening_node, metadata={"type": "agent", "llm_cfg": "config/opening_llm_cfg.json"})
builder.add_node("replies_node", replies_node, metadata={"type": "agent", "llm_cfg": "config/replies_llm_cfg.json"})
builder.add_node("update_node", update_node, metadata={"type": "agent", "llm_cfg": "config/update_llm_cfg.json"})
builder.add_node("merge_node", merge_node)

builder.set_entry_point("outline_node")
builder.add_edge("outline_node", "opening_node")
builder.add_edge("opening_node", "replies_node")
builder.add_edge("replies_node", "update_node")
builder.add_edge("update_node", "merge_node")
builder.add_edge("merge_node", END)

main_graph = builder.compile()
