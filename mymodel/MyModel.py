class MyModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """
    
    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing")

    def predict(self,X,features_names):
        """
        Return prediction.
        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run idenity function")
        return X

    def send_feedback(self,features,feature_names,reward,truth,routing):
        """
        Handle feedback
        Parameters
        ----------
        features : array - the features sent in the original predict request
        feature_names : array of feature names. May be None if not available.
        reward : float - the reward
        truth : array with correct value (optional)
        """
        print("Send feedback called")
        return []
