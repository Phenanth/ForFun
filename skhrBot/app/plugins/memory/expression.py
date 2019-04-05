EXPR_DB_MEMORY_ADD = """INSERT INTO memory values(%s, %s, %s)"""
EXPR_DB_MEMORY_FINDALL = """SELECT mKey, mValue FROM memory WHERE qq_account = %s"""

EXPR_ADD_SUCCESS = """添加备忘录事务成功完成"""
EXPR_FAILURE = """事务失败"""