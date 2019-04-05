import json
from nonebot import CommandSession

import MySQLdb

from . import expression as e

db = MySQLdb.connect(user="root", host="localhost", passwd="charlotte2", db="botMemory")


# Need optimizing here if the error submerges.
def db_memory_add(data:json):
	cursor = db.cursor()
	count = 0

	params = (data['qq_account'], data['key'], data['value'])
	try:
		count = cursor.execute(e.EXPR_DB_MEMORY_ADD, params)
		db.commit()
	except db.IntegrityError:
		results = e.EXPR_ADD_FAILURE
	finally:
		results = e.EXPR_ADD_SUCCESS

	if count == 0:
		results = e.EXPR_ADD_FAILURE

	cursor.close()

	return results

def db_memory_findall(data:json):
	cursor = db.cursor()
	count = 0

	params = (data['qq_account'],)
	count = cursor.execute(e.EXPR_DB_MEMORY_FINDALL, params)

	if count > 0:
		results = cursor.fetchall()
	else:
		results = e.EXPR_FINDALL_NONE

	cursor.close()

	return results

def db_memory_del(data:json):
	cursor = db.cursor()
	count = 0

	params = (data['qq_account'], data['key'])
	count = cursor.execute(e.EXPR_DB_MEMORY_DEL, params)
	db.commit()

	if count == 1:
		results = e.EXPR_DEL_SUCCESS
	else:
		results = e.EXPR_FAILURE

	cursor.close()

	return results

def db_memory_find(data:json):
	cursor = db.cursor()
	count = 0

	params = (data['qq_account'], data['key'])
	count = cursor.execute(e.EXPR_DB_MEMORY_FIND, params)

	if count > 0:
		results = cursor.fetchall()
	else:
		results = EXPR_FIND_NONE

	cursor.close()

	return results

def db_memory_delall(data:json):
	cursor = db.cursor()
	count = 0

	params = (data['qq_account'],)
	count = cursor.execute(e.EXPR_DB_MEMORY_DELALL, params)
	db.commit()

	results = e.EXPR_DELALL_SUCCESS

	cursor.close()

	return results

async def db_memory_operation(data: json):

	if data['operation'] == 'add':
		return db_memory_add(data)
	elif data['operation'] == 'findall':
		return db_memory_findall(data)
	elif data['operation'] == 'del':
		return db_memory_del(data)
	elif data['operation'] == 'find':
		return db_memory_find(data)
	elif data['operation'] == 'delall':
		return db_memory_delall(data)
	else:
		return e.EXPR_OPT_NOT_FOUND
