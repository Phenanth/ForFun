from aiocqhttp.message import escape
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.helpers import render_expression

from .data_source import call_tuling_api

__plugin_name__ = '聊天'
__plugin_usage__ = r"""
聊天

直接找我聊天即可！
""".strip()

EXPR_DONT_UNDERSTAND = (
	'我现在还不太明白你在说什么(或者是API调用失败了 *LOL*), 输入\'helpme [模块名](可选)\'获得使用帮助',
	'其实我不太明白你的意思(或者是API调用失败了 *LOL*), 输入\'helpme [模块名](可选)\'获得使用帮助',
	'我有点看不懂你的意思(或者是API调用失败了 *LOL*), 输入\'helpme [模块名](可选)\'获得使用帮助'
)

@on_command('tuling')
async def tuling(session: CommandSession):
	message = session.state.get('message')

	reply = await call_tuling_api(session, message)
	if reply:
		await session.send(escape(reply))
	else:
		await session.send(render_expression(EXPR_DONT_UNDERSTAND))

@on_natural_language
async def _(session: NLPSession):
	return IntentCommand(90.0, 'tuling', args={'message': session.msg_text})

