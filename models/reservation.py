from datetime import datetime

class Reservation:
    """_summary_
    """
    def __init__(self, user_id, book_id, start_date, end_date, status="en attente"):
        """_summary_

        Args:
            user_id (_type_): _description_
            book_id (_type_): _description_
            start_date (_type_): _description_
            end_date (_type_): _description_
            status (str, optional): _description_. Defaults to "en attente".
        """
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = self._convert_to_date(start_date)
        self.end_date = self._convert_to_date(end_date)
        self.status = status

    def _convert_to_date(self, date_str):
        """_summary_

        Args:
            date_str (_type_): _description_

        Returns:
            _type_: _description_
        """
        if isinstance(date_str, str):
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_str

    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            'user_id': self.user_id,
            'book_id': self.book_id,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        return cls(
            user_id=data['user_id'],
            book_id=data['book_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            status=data.get('status', "en attente")
        )
