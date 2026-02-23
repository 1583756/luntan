from typing import Optional, List
from pydantic import BaseModel, Field


class GlobalState(BaseModel):
    """全局状态定义"""
    theme: str = Field(..., description="用户输入的主题")
    story_outline: str = Field(default="", description="故事大纲")
    title: str = Field(default="", description="帖子标题")
    opening_post: str = Field(default="", description="帖子开篇（1楼）")
    replies: str = Field(default="", description="网友回复")
    updates: str = Field(default="", description="楼主更新")
    final_story: str = Field(default="", description="完整的论坛体小说")


class GraphInput(BaseModel):
    """工作流的输入"""
    theme: str = Field(..., description="用户输入的主题，例如：宿管阿姨其实是隐藏大佬")


class GraphOutput(BaseModel):
    """工作流的输出"""
    final_story: str = Field(..., description="完整的论坛体小说")


class OutlineInput(BaseModel):
    """故事大纲生成节点的输入"""
    theme: str = Field(..., description="用户输入的主题")


class OutlineOutput(BaseModel):
    """故事大纲生成节点的输出"""
    story_outline: str = Field(..., description="故事大纲，包含人物关系、事件发展和反转节点")


class OpeningInput(BaseModel):
    """帖子开篇生成节点的输入"""
    story_outline: str = Field(..., description="故事大纲")
    theme: str = Field(..., description="原始主题")


class OpeningOutput(BaseModel):
    """帖子开篇生成节点的输出"""
    title: str = Field(..., description="吸睛的帖子标题")
    opening_post: str = Field(..., description="1楼帖子内容")


class RepliesInput(BaseModel):
    """网友回复生成节点的输入"""
    story_outline: str = Field(..., description="故事大纲")
    opening_post: str = Field(..., description="1楼帖子内容")


class RepliesOutput(BaseModel):
    """网友回复生成节点的输出"""
    replies: str = Field(..., description="多楼层的网友互动内容")


class UpdateInput(BaseModel):
    """楼主更新生成节点的输入"""
    story_outline: str = Field(..., description="故事大纲")
    replies: str = Field(..., description="网友回复")


class UpdateOutput(BaseModel):
    """楼主更新生成节点的输出"""
    updates: str = Field(..., description="楼主更新内容")


class MergeInput(BaseModel):
    """故事整合节点的输入"""
    title: str = Field(..., description="帖子标题")
    opening_post: str = Field(..., description="1楼帖子内容")
    replies: str = Field(..., description="网友回复")
    updates: str = Field(..., description="楼主更新")


class MergeOutput(BaseModel):
    """故事整合节点的输出"""
    final_story: str = Field(..., description="完整的论坛体小说")
