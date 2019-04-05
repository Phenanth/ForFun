import json
from nonebot import CommandSession

import MySQLdb

from . import expression as e

db = MySQLdb.connect(user="root", host="localhost", passwd="charlotte2", db="botMemory")



def db_memory_add(data:json):
	cursor = db.cursor()

	params = (data['qq_account'], data['key'], data['value'])
	count = cursor.execute(e.EXPR_DB_MEMORY_ADD, params)
	db.commit()

	if count == 1:
		results = e.EXPR_ADD_SUCCESS
	else:
		results = e.EXPR_FAILURE

	cursor.close()

	return results

def db_memory_findall(data:json):
	cursor = db.cursor()

	params = (data['qq_account'],)
	count = cursor.execute(e.EXPR_DB_MEMORY_FINDALL, params)

	results = cursor.fetchall()

	cursor.close()

	return results


async def db_memory_operation(data: json):

	if data['operation'] == 'add':
		return db_memory_add(data)
	elif data['operation'] == 'findall':
		return db_memory_findall(data)
