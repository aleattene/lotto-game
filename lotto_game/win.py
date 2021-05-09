class Win:

    def __init__(self, city, extracted_numbers):
        self.city = city
        self.extracted_numbers = extracted_numbers

    def __str__(self):
        return (f"""
        City: {self.city}
        Numbers: {self.extracted_numbers}
       """)
