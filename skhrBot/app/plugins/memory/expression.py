EXPR_DB_MEMORY_ADD = """INSERT INTO memory values(%s, %s, %s, 0)"""
EXPR_DB_MEMORY_FINDALL = """SELECT mKey, mValue FROM memory WHERE qq_account=%s AND isDeleted=0"""
EXPR_DB_MEMORY_DEL = """UPDATE memory SET isDeleted=1 WHERE qq_account=%s  AND mKey=%s"""
# EXPR_DB_MEMORY_DEL = """DELETE FROM memory WHERE qq_account=%s AND mKey=%s"""
EXPR_DB_MEMORY_FIND = """ SELECT mKey, mValue FROM memory WHERE qq_account=%s AND  mKey=%s  AND isDeleted=0"""
EXPR_DB_MEMORY_DELALL = """UPDATE memory SET isDeleted=1 WHERE qq_account=%s"""
# EXPR_DB_MEMORY_DELALL = """DELETE FROM memory WHERE qq_account=%s"""

EXPR_ADD_SUCCESS = """添加备忘录事务成功完成"""
EXPR_DEL_SUCCESS = """删除备忘录事务成功完成"""
EXPR_DELALL_SUCCESS = """成功清空备忘录"""

EXPR_FAILURE = """事务失败"""
EXPR_ADD_FAILURE = """关键字重复，请重新选择一个关键字"""

EXPR_FIND_NONE = """未找到指定关键字的备忘录"""
EXPR_FINDALL_NONE = """你的备忘录为空"""
EXPR_OPT_NOT_FOUND = """事务名错误，请使用--help查看使用帮助"""