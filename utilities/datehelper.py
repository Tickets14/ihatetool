from datetime import datetime, timedelta

class DateHelper:
    @staticmethod
    def get_current_date() -> datetime.date:
        """
        Returns the current date.

        Returns:
            datetime.date: The current date.
        """
        return datetime.now().date()

    @staticmethod
    def get_current_datetime() -> datetime:
        """
        Returns the current datetime.

        Returns:
            datetime: The current datetime.
        """
        return datetime.now()

    @staticmethod
    def add_days_to_date(date: datetime, days: int) -> datetime:
        """
        Adds the given number of days to the given date.

        Args:
            date (datetime): The date to add days to.
            days (int): The number of days to add.

        Returns:
            datetime: The new date after adding the given number of days.
        """
        if not isinstance(date, datetime):
            raise ValueError("The 'date' parameter must be a datetime object")
        return date + timedelta(days=days)

    @staticmethod
    def format_date(date: datetime, format_string: str = "%Y-%m-%d") -> str:
        """
        Formats the given date according to the specified format string.

        Args:
            date (datetime): The date to format.
            format_string (str, optional): The format string to use. Defaults to "%Y-%m-%d".

        Returns:
            str: The formatted date string.
        """
        if not isinstance(date, datetime):
            raise ValueError("The 'date' parameter must be a datetime object")
        return date.strftime(format_string)

    @staticmethod
    def parse_date(date_string: str, format_string: str = "%Y-%m-%d") -> datetime:
        """
        Parses the given date string according to the specified format string.

        Args:
            date_string (str): The date string to parse.
            format_string (str, optional): The format string to use. Defaults to "%Y-%m-%d".

        Returns:
            datetime: The parsed datetime object.
        """
        return datetime.strptime(date_string, format_string)


