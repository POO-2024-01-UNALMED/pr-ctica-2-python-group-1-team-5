class CuentaBancaria:
    cuentas = []

    def __init__(self, numero_cuenta, titular, saldo_inicial=0.0, banco=None,bolsillo_trabajadores=0.0, bolsillo_inventario=0.0, bolsillo_transporte=0.0, bolsillo_establecimientos=0.0, bolsillo_pago_credito=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.banco = banco
        self.bolsillo_trabajadores = bolsillo_trabajadores
        self.bolsillo_inventario = bolsillo_inventario
        self.bolsillo_transporte = bolsillo_transporte
        self.bolsillo_establecimientos = bolsillo_establecimientos
        self.bolsillo_pago_credito = bolsillo_pago_credito
        self.saldo = saldo_inicial

        if banco:
            self.establecer_valores(banco)

        # Calcula el saldo si se pasan valores específicos de bolsillo
        if bolsillo_trabajadores or bolsillo_inventario or bolsillo_transporte or bolsillo_establecimientos or bolsillo_pago_credito:
            self.saldo = (bolsillo_trabajadores + bolsillo_inventario + 
                          bolsillo_transporte + bolsillo_establecimientos + bolsillo_pago_credito)

        CuentaBancaria.cuentas.append(self)
        self.credito = []

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            #terminar el else
    
    # Getters
    def getNumeroCuenta(self):
        return self.numero_cuenta

    def getTitular(self):
        return self.titular

    def getBanco(self):
        return self.banco

    def getBolsilloTrabajadores(self):
        return self.bolsillo_trabajadores

    def getBolsilloInventario(self):
        return self.bolsillo_inventario

    def getBolsilloTransporte(self):
        return self.bolsillo_transporte

    def getBolsilloEstablecimientos(self):
        return self.bolsillo_establecimientos

    def getBolsilloPagoCredito(self):
        return self.bolsillo_pago_credito

    def getSaldo(self):
        return self.saldo

    def getCredito(self):
        return self.credito

    # Setters
    def setNumeroCuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def setTitular(self, titular):
        self.titular = titular

    def setBanco(self, banco):
        self.banco = banco

    def setBolsilloTrabajadores(self, bolsillo_trabajadores):
        self.bolsillo_trabajadores = bolsillo_trabajadores
        self.actualizarSaldo()

    def setBolsilloInventario(self, bolsillo_inventario):
        self.bolsillo_inventario = bolsillo_inventario
        self.actualizarSaldo()

    def setBolsilloTransporte(self, bolsillo_transporte):
        self.bolsillo_transporte = bolsillo_transporte
        self.actualizarSaldo()

    def setBolsilloEstablecimientos(self, bolsillo_establecimientos):
        self.bolsillo_establecimientos = bolsillo_establecimientos
        self.actualizarSaldo()

    def setBolsilloPagoCredito(self, bolsillo_pago_credito):
        self.bolsillo_pago_credito = bolsillo_pago_credito
        self.actualizarSaldo()

    def setSaldo(self, saldo):
        self.saldo = saldo

    def setCredito(self, credito):
        self.credito = credito

    def actualizarSaldo(self):
        self.saldo = (self.bolsillo_trabajadores + self.bolsillo_inventario +
                      self.bolsillo_transporte + self.bolsillo_establecimientos +
                      self.bolsillo_pago_credito)

    