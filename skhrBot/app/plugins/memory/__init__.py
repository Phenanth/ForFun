import json

from nonebot import (
	on_command, CommandSession,
	argparse
)

from .data_operation import db_memory_operation

__plugin_name__ = '命令行风格交互的备忘录'
__plugin_usage__ = r"""
命令行风格的备忘录

使用方法：
		memory --operation OPERATION [options]

OPERATION
		-o, --operation  备忘录操作
		支持操作: [add | find | findall | del | delall]

OPTIONS：
		-h, --help 显示本使用帮助
		-k, --key 备忘录关键字
		-v, --value 备忘录内容
"""

USAGE = r"""
命令行风格交互的备忘录

使用方法：
		memory --operation OPERATION [options]

OPERATION
		-o, --operation  备忘录操作
		支持操作: [add | find | findall | del | delall]

OPTIONS：
		-h, --help 显示本使用帮助
		-k, --key 备忘录关键字
		-v, --value 备忘录内容
"""


@on_command('memory', shell_like=True, aliases=('memory', 'mm'))
async def memory(session: CommandSession):

	parser = argparse.ArgumentParser(session=session)
	parser.add_argument('-o', '--operation')
	parser.add_argument('-k', '--key')
	parser.add_argument('-v', '--value')
	args = parser.parse_args(session.argv)

	data = {
		'operation': '',
		'key': '',
		'value': '',
		"qq_account": session.ctx['sender']['user_id']
	}

	data['operation' ] = args.operation

	if data['operation' ] == 'add' or data['operation' ] == 'find' or data['operation' ] == 'del':
		if not args.key:
			session.send('参数错误, 请使用--help查询使用帮助')
		data['key'] = args.key

	if data['operation' ] == 'add':
		if not args.value:
			session.send('参数错误, 请使用--help查询使用帮助')
		data['value'] = args.value

	results = await db_memory_operation(data)

	if data['operation'] == 'add':
		await session.send(results)
	elif data['operation'] == 'findall':
		await session.send('备忘录一览:' + ''.join(('\n\n' + result[0] + '\n' + result[1] ) for result in results))

