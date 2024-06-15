from datetime import datetime

class Reservation:
    """
    Class representing a book reservation.

    Attributes:
        user_id (int): The user ID.
        book_id (int): The book ID.
        start_date (date): The start date of the reservation.
        end_date (date): The end date of the reservation.
        status (str): The status of the reservation. Defaults to "pending".
    """
    def __init__(self, user_id, book_id, start_date, end_date, status="en attente"):
        """
        Initializes a new reservation.

        Args:
            user_id (int): The user ID.
            book_id (int): The book ID.
            start_date (str or date): The start date of the reservation (format 'YYYY-MM-DD' or date object).
            end_date (str or date): The end date of the reservation (format 'YYYY-MM-DD' or date object).
            status (str, optional): The status of the reservation. Defaults to "pending".
        """
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = self._convert_to_date(start_date)
        self.end_date = self._convert_to_date(end_date)
        self.status = status

    def _convert_to_date(self, date_str):
        """
        Converts a string to a date object.

        Args:
            date_str (str or date): The date as a string (format 'YYYY-MM-DD') or date object.

        Returns:
            date: The converted date object.
        """
        if isinstance(date_str, str):
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_str

    def to_dict(self):
        """
        Converts the Reservation object to a dictionary.

        Returns:
            dict: A dictionary representing the reservation.
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
        """
        Creates a Reservation instance from a dictionary.

        Args:
            data (dict): A dictionary containing the reservation data.

        Returns:
            Reservation: An instance of the Reservation class.
        """
        return cls(
            user_id=data['user_id'],
            book_id=data['book_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            status=data.get('status', "en attente")
        )
