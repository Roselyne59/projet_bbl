import json
from datetime import date, datetime

class Reservation:
    def __init__(self, user_id, book_id, start_date, end_date, status="en attente"):
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = self._convert_to_date(start_date)
        self.end_date = self._convert_to_date(end_date)
        self.status = status

    def _convert_to_date(self, date_str):
        if isinstance(date_str, str):
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_str

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'book_id': self.book_id,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data['user_id'],
            book_id=data['book_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            status=data.get('status', "en attente")
        )
