class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        '''
        Test the preprocess_data() function.
        '''
        from preprocess_data import preprocess_data
        (x_train, y_train), _ = preprocess_data()
        expected_train_size = 1000  # replace with your expected train size
        self.assertEqual(x_train.shape[0], expected_train_size)
        self.assertTrue(np.all((0 <= x_train) & (x_train <= 1)))

unittest.main()
