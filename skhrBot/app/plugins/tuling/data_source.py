import json
from typing import Optional

import aiohttp
from nonebot import CommandSession
from nonebot import context_id

async def call_tuling_api(session: CommandSession, text: str) -> Optional[str]:

	if not text:
		return None

	url = 'http://openapi.tuling123.com/openapi/api/v2'

	payload = {
		'reqType': 0,
		'perception': {
			'inputText': {
				'text': text
			}
		},
		'userInfo': {
			'apiKey': session.bot.config.TULING_API_KEY,
			'userId': context_id(session.ctx, use_hash=True)
		}
	}

	group_unique_id = context_id(session.ctx, mode='group', use_hash=True)
	if group_unique_id:
		payload['userInfo']['groupId'] = group_unique_id

	try:
		async with aiohttp.ClientSession() as sess:
			async with sess.post(url, json=payload) as response:
				if response.status != 200:
					return None

				resp_payload = json.loads(await response.text())
				if resp_payload['results']:
					for result in resp_payload['results']:
						if result['resultType']:
							return result['values']['text']
	except (aiohttp.ClientError, json.JSONDecodeError, KeyError):
		return None

