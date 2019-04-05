import nonebot
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from .data_source import get_list_of_commands

@on_command('usage', aliases=('helpme', '使用帮助', '使用方法'))
async def _(session: CommandSession):
	plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

	args = session.current_arg_text.strip().lower()
	if not args:
		await session.send(
			'我现在支持的功能有:\n\n' + '\n'.join(p.name for p in plugins))
		return

	for p in plugins:
		if p.name.lower() == args:
			await session.send(p.usage)

# async def helpme(session: CommandSession):
# 	commands = await get_list_of_commands()

# 	await session.send(commands)

# @on_natural_language(keywords={'可以做什么', '能做什么'})
# async def _(session: NLPSession):
# 	return IntentCommand(75.0, 'helpme')
