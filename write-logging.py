import logging

"""
ログメッセージをキーバリューで書くことがある。
これはログ解析ソフトがキーバリュー検索が可能なため
"""

logger = logging.getLogger(__name__)

logger.error("Api call is failed")

logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})
