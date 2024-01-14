class Category:
  def __init__(self, name):
      self.name = name
      self.ledger = []

  def __str__(self):
      name_len = len(self.name)
      start_len = round((30 - name_len) / 2)
      first_line = "*" * start_len + f"{self.name}" + "*" * (30 - start_len - name_len)

      def format_line(entry):
          desc_len = len(entry["description"])
          amount_str = self.format_amount(entry["amount"])
          desc = entry["description"]

          amount_len = len(amount_str)

          if desc_len > 23:
              desc = desc[:23]
              desc_len = 23

          the_line = f"{desc}{' ' * (30 - amount_len - desc_len)}{amount_str}"
          return the_line

      total_amount = self.format_amount(self.get_balance())

      return first_line + '\n' + '\n'.join(map(format_line, self.ledger)) + '\n' + f'Total: {total_amount}'

  def deposit(self, amount, desc=""):
      entry = {"amount": amount, "description": desc}
      self.ledger.append(entry)

  def get_balance(self):
      return sum(entry["amount"] for entry in self.ledger)

  def check_funds(self, amount):
      return amount <= self.get_balance()

  def withdraw(self, amount, desc=''):
      if self.check_funds(amount):
          entry = {"amount": -amount, "description": desc}
          self.ledger.append(entry)
          return True
      else:
          return False

  def transfer(self, amount, category):
      if self.withdraw(amount, f'Transfer to {category.name}'):
          category.deposit(amount, f'Transfer from {self.name}')
          return True
      return False

  def format_amount(self, amount):
      return f'{amount:.2f}'[:7]


def create_spend_chart(categories):
  if not all(isinstance(category, Category) for category in categories):
      raise ValueError("All elements in 'categories' must be instances of the Category class.")

  def calculate_percent_amount(spend_amount, total):
      return [int(((amt / total) * 10) // 1) * 10 for amt in spend_amount]

  def generate_spend_chart_lines(percent_amount):
      chart_output = "Percentage spent by category"
      for i in range(100, -1, -10):
          chart_output += f"\n{i:3}|" + "".join(" o " if j >= i else "   " for j in percent_amount) + " "
      chart_output += "\n    ----------"
      return chart_output

  def generate_category_labels(categories, max_length):
      chart_output = ""
      for i in range(max_length):
          chart_output += "\n    "
          for category in categories:
              if i < len(category.name):
                  chart_output += " " + category.name[i] + " "
              else:
                  chart_output += "   "
          chart_output += " "
      return chart_output

  category_list = [category.name for category in categories]
  spend_amount = [sum(abs(entry["amount"]) for entry in category.ledger if entry["amount"] < 0) for category in categories]

  total = sum(spend_amount)
  percent_amount = calculate_percent_amount(spend_amount, total)

  category_length = [len(category.name) for category in categories]
  max_length = max(category_length)

  chart_output = generate_spend_chart_lines(percent_amount)
  chart_output += generate_category_labels(categories, max_length)

  return chart_output
