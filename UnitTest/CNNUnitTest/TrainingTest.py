class TestTraining(unittest.TestCase):
    def test_training(self):
        # assuming the same model and data setup as before
        history = model.fit(train_generator,
                            steps_per_epoch=len(train_generator),
                            epochs=EPOCHS,
                            validation_data=validation_generator,
                            validation_steps=len(validation_generator),
                            callbacks=callbacks)
        # Check that some training has occurred, i.e., loss has decreased
        self.assertLess(min(history.history['loss']), history.history['loss'][0])

unittest.main()
