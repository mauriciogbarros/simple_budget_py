# Budget app
freeCodeCamp Python Certification - Certification Project #2
A simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

## User Stories
1. You should have a `Category` class that accepts a name as the argument.
2. The `Category` class should have an instance attribute `ledger` that is a list, and contains the list of transactions.
3. The `Category` class should have the following methods:
   1. A `deposit` method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the `ledger` list in the form of `{'amount': amount, 'description': description}`.
   2. A `withdraw` method that accepts an amount and an optional description (default to an empty string). The method should store in `ledger` the amount passed in as a negative number, and should return `True` if the withdrawal succeeded and `False` otherwise.
   3. A `get_balance` method that returns the current category balance based on `ledger`.
   4. A `transfer` method that accepts an amount and another `Category` instance, withdraws the amount with description `Transfer to [Destination]`, deposits it into the other category with description `Transfer from [Source]`, where `[Destination]` and `[Source]` should be replaced by the name of destination and source categories. The method should return `True` when the transfer is successful, and `False` otherwise.
   5. A `check_funds` method that accepts an amount and returns `False` if it exceeds the balance or `True` otherwise. This method must be used by both the `withdraw` and `transfer` methods.
4. When a `Category` object is printed, it should:
   1. Display a title line of 30 characters with the category name centered between `*` characters.
   2. List each `ledger` entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
   3. Show a final line `Total: [balance]`, where `[balance]` should be replaced by the category total.
5. You should have a function outside the `Category` class name `create_spend_chart(categories)` that returns a bar-chart string. To build the chart:
   1. Start with the title `Percentage spent by category`.
   2. Calculate percentages from withdrawals only and not from deposits. The percentages should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
   3. Label the y-axis from `100` down to `0` in steps of 10.
   4. Use `o` characters for the bars.
   5. Include a horizontal line two spaces past the last bar.
   6. Write category names vertically below the bar.
