class MySingleton:
    _instance = None

    # __new__ is a class method that is called before __init__.
    # It is responsible for creating the self instance of the class.
    # before that happen we check if the _instance is already created or not.
    # If the instance is already created, we return the same instance.
    # The return value of __new__ is then passed to __init__ as the self parameter.
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MySingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print('MySingleton.__init__ called')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = MySingleton()
        return cls._instance
