class TestPrediction(unittest.TestCase):
    def test_prediction_output(self):
        '''
        Test the prediction output.
        '''
        from preprocess_data import load_data, preprocess_data
        test_data, _ = load_data('test_data_path')
        test_data = preprocess_data(test_data)
        y_pred = model.predict(test_data)
        self.assertEqual(y_pred.shape, (len(test_data), NUM_CLASSES))
        self.assertTrue(np.all((0 <= y_pred) & (y_pred <= 1)))

unittest.main()
