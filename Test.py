class Test(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(calculate_total_cost(999, 0), "invalid input")
    
    def test_discount_35_percent(self):
        self.assertEqual(calculate_total_cost(900, 1000000), 351000000)
    
    def test_discount_20_percent(self):
        self.assertEqual(calculate_total_cost(600, 500000), 240040000)
    
    def test_no_discount(self):
        self.assertEqual(calculate_total_cost(300, 100000), 30040000)

