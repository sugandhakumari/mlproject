class CustomException(Exception):
    """
    Custom Exception class to handle specific errors in the application.
    """

    def __init__(self, message: str, error_details: Exception = None):
        """
        Initialize the CustomException with an error message and optional error details.

        :param message: Error message to describe the exception.
        :param error_details: Optional original exception details.
        """
        super().__init__(message)
        self.error_details = error_details

    def __str__(self):
        """
        Return a string representation of the exception, including error details if available.
        """
        if self.error_details:
            return f"{self.args[0]} | Details: {str(self.error_details)}"
        return self.args[0]