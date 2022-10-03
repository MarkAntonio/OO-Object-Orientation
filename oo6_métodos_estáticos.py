class Error:

    @staticmethod
    def protocol():
        print('Protocol error identified')

    @staticmethod
    def entrada():
        print('Input error has getted.')

    @staticmethod
    def error_500():
        print('Internal Server Error')

    @staticmethod
    def error_404():
        print('Not Found Error')


'''Métodos estáticos são coleção de modelos que não estão ligadas entre si.
Eles São usados sem a necessidade de uma instância, e não podem interagir com atributos de classe (cls)
ou de objeto (self) caso existam.
No diagrama de classe, o método estático é um método que tem um risco em baixo
'''

Error.protocol()
Error.entrada()
Error.error_404()
Error.error_500()
