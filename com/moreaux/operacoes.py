class Testravis:

    def velocidade(self, espaco, tempo):
        self.v = espaco / tempo
        return 'velocidade: {} m/s'.format(self.v)

    def dados(self,nome, idade=None):
        if(idade is not None):
            return 'idade: {}'.format(idade)
        else:
            return 'idade: nao informada'
    
