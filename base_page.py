class BasePage:
    """
    Klasa bazowa kazdej strony.
    Nie bedzie miala instacji.  Faktyczne strony beda po niej dziedziczyc.
    """
    def __init__(self, driver):
        self.driver = driver
        # Kazda strona bedzie sie automatycznie sprawdzala
        self._verify_page()

    def _verify_page(self):
        """
        Weryfikacja strony
        """
        pass
