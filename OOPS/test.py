class ExpenseTracker:
    """calculate the expense of a month in any specified thing."""
    expense_tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):

        # public attribute
        self.tracker_category = tracker_category

        # private attributes
        self.__opening_balance = opening_balance
        self.__budget = budget

    """this is instance method"""

    # private method
    def __get_original_balance(self):
        return self.__opening_balance

    """also an instance method"""

    def check_balance(self, limit=1000):
        if self.budget >= limit:
            return True
        else:
            return "Your opening balance is less than the limit."

    """STATIC METHOD"""

    @staticmethod
    def convert_amount(amount):
        return float(amount)

    """CLASS METHOD"""

    @classmethod
    def get_attributes_from_string(cls, diary_entry: str):
        tracking_category, opening_balance, tracker_budget = diary_entry.split(" ")
        return ExpenseTracker(tracking_category.capitalize(),
                              cls.convert_amount(opening_balance),
                              cls.convert_amount(tracker_budget))
