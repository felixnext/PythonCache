'''
Caching Object that will store objects in a MongoDB.

Used to buffer documents into a mongo db store
'''

from datetime import datetime
from typing import Tuple, Any

from .Cache import Cache


class MongoCache(Cache):
    """Cache that buffers data into a mongo db database

    Args:
        handler (MongoConnection): Connection to the MongoDB Database
    """
    def __init__(self, handler, keep_history: bool):
        super().__init__(keep_history=keep_history)

        self.handler = handler

    def _store(self, key: str, date: datetime, value: Any) -> bool:
        # TODO: implement
        return super()._store(key, date, value)

    def _retrieve(self, key: str, date: datetime) -> Tuple[Any, datetime]:
        # TODO: implement
        return super()._retrieve(key, date=date)
