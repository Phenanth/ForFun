import json
from nonebot import argparse
from nonebot import on_command, CommandSession

__plugin_name__ = '测试[开发者用]'
__plugin_usage__ = r"""
测试 [开发者用]

开发者用于了解框架结构和测试用的接口, 好孩子不要用
"""

@on_command('test', aliases={'test'})
async def test(session: CommandSession):
	args = session.ctx['sender']['user_id']
	await session.send(f'User Information: {args}')
