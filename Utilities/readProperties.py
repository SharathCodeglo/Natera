import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class read_config:
    @staticmethod
    def get_url():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def get_signURL():
        signa_url = config.get('common info', 'signa_url')
        return signa_url

    @staticmethod
    def get_AlteraURL():
        altera_url = config.get('common info', 'Altera_url')
        return altera_url

    @staticmethod
    def get_EmpowerURL():
        empower_url = config.get('common info', 'Empower_url')
        return empower_url


