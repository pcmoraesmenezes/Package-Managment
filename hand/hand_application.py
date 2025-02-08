import requests

class HandApplication:
    """
    Classe HandApplication para realizar uma requisição HTTP e exibir a resposta.

    Essa classe realiza uma requisição GET para uma URL definida e imprime
    o código de status da resposta e o conteúdo em formato JSON.

    Atributos:
        BASE_URL (str): URL para onde será enviada a requisição.
    """

    def __init__(self):
        """
        Inicializa a instância de HandApplication.

        Define a URL base (BASE_URL) para a requisição HTTP.
        """
        print("HandApplication initialized")
        self.BASE_URL = "https://httpbin.org/get"

    def _get_response(self):
        """
        Realiza uma requisição GET para a URL definida em BASE_URL.

        Returns:
            requests.Response: Objeto de resposta da requisição HTTP.
        """
        response = requests.get(self.BASE_URL)
        return response

    def execute(self):
        """
        Executa a aplicação.

        Realiza a requisição GET, imprime o código de status da resposta e
        o conteúdo em formato JSON.
        
        Exemplo:
            >>> app = HandApplication()
            >>> app.execute()
        """
        print("HandApplication executed")
        response = self._get_response()
        print(response.status_code)
        print(response.json())


if __name__ == '__main__':
    app = HandApplication()
    app.execute()
