class TestDataLoading(unittest.TestCase):
    def test_load_data(self):
        '''
        Test the load_data() function.
        '''
        from preprocess_data import load_data
        test_data, test_labels = load_data('test_data_path')
        expected_test_size = 200  # replace with your expected test size
        self.assertEqual(test_data.shape[0], expected_test_size)
        self.assertEqual(test_data.shape[0], test_labels.shape[0])

unittest.main()
