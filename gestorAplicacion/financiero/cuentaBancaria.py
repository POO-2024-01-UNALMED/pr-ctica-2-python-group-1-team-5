from gestorAplicacion.financiero.banco import Banco

class CuentaBancaria:
    cuentas = []

    def __init__(self, numero_cuenta, titular,banco, saldo_inicial=0.0,bolsilloTrabajadores=0.0, bolsilloInventario=0.0, bolsilloTransporte=0.0, bolsilloEstablecimientos=0.0, bolsilloPagoCredito=0.0):
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self._banco = banco
        self._bolsilloTrabajadores = bolsilloTrabajadores
        self._bolsilloInventario = bolsilloInventario
        self._bolsilloTransporte = bolsilloTransporte
        self._bolsilloEstablecimientos = bolsilloEstablecimientos
        self._bolsilloPagoCredito = bolsilloPagoCredito
        self._saldo = saldo_inicial
        self._credito = []
        self._interes = 0
        self._cobroAdicional = 0

        if banco:
            self.establecerValores(banco)

        # Calcula el saldo si se pasan valores específicos de bolsillo
        if bolsilloTrabajadores or bolsilloInventario or bolsilloTransporte or bolsilloEstablecimientos or bolsilloPagoCredito:
            self._saldo = (self._bolsilloTrabajadores + self._bolsilloInventario + 
                          self._bolsilloTransporte + self._bolsilloEstablecimientos + self._bolsilloPagoCredito)

        CuentaBancaria.cuentas.append(self)
        self.credito = []
    
    def establecerValores(self, banco):
            self._interes = banco.value[1]
            self._cobroAdicional = banco.value[2]

    def depositar(self, cantidad, tipo):
        if(tipo == "saldo"):
            if (cantidad > 0):
                self._saldo += cantidad

        elif(tipo == "bolsilloTrabajadores"):
            if (cantidad > 0):
                self._bolsilloTrabajadores += cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
            
        elif(tipo == "bolsilloInventario"):
            if (cantidad > 0):
                self._bolsilloInventario += cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        
        elif(tipo == "bolsilloTransporte"):
    	    if (cantidad > 0):
                self._bolsilloTransporte += cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        
        elif(tipo == "bolsilloEstablecimientos"):
    	    if (cantidad > 0):
                self._bolsilloEstablecimientos += cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        
        elif(tipo == "bolsilloPagoCredito"):
    	    if (cantidad > 0):
                self._bolsilloPagoCredito += cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
    
    def retirar(self, cantidad, tipo):
        if(tipo == "saldo"):
     	    if (cantidad <= saldo):
                self._saldo -= cantidad
           
        elif(tipo == "bolsilloTrabajadores"):
       	    if (cantidad <= bolsilloTrabajadores):
                self._bolsilloTrabajadores -= cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        elif(tipo == "bolsilloInventario"):
       	    if (cantidad <= bolsilloInventario):
                self._bolsilloInventario -= cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        elif(tipo == "bolsilloTransporte"):
       	    if (cantidad <= bolsilloTransporte):
                self._bolsilloTransporte -= cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        elif(tipo == "bolsilloEstablecimientos"):
       	    if (cantidad <= bolsilloEstablecimientos):
                self._bolsilloEstablecimientos -= cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
        elif (tipo == "bolsilloPagoCredito"):
    	    if (cantidad <= bolsilloPagoCredito):
                self._bolsilloPagoCredito -= cantidad
                self._saldo = _bolsilloTrabajadores + _bolsilloTransporte + _bolsilloInventario + _bolsilloEstablecimientos + _bolsilloPagoCredito
      

    def infoCredito(self, credito):
        creditos = self.getCredito()
        if creditos.size() > 0:
             return """ID: {}
             Precio: {}
             Porcentaje por pagar: {}""".format(
             creditos.get(credito).getID(), creditos.get(credito).getPrecio(), creditos.get(credito).getPorcentajeCreditoPorPagar())
        else:
            return "No hay credito activo con ese indice"   
    
    def transaccionCuentaAhorros(self, valor, cuentaAhorros):
        if self.getBanco() == cuentaAhorros.getBanco():
            saldo = self._saldo - valor
            self.setSaldo(saldo)
        else:
            cobroAdicional = self.getCobroAdicional()
            saldo = self._saldo - (valor + cobroAdicional)
            self.setSaldo(saldo)
    
        saldoCuentaAhorros = cuentaAhorros._saldo + valor
        cuentaAhorros.setSaldo(saldoCuentaAhorros)
    
        porcentajeInteres = self.getInteres()
        interes = cuentaAhorros.getSaldo() * porcentajeInteres
        saldoFinal = cuentaAhorros.getSaldo() - interes
        cuentaAhorros.setSaldo(saldoFinal)

    def transaccion(self, valor, cuentaCorriente, tipo):
        if self.getBanco() == cuentaCorriente.getBanco():
            if tipo == "saldo":
                saldo = self._saldo - valor
                self.setSaldo(saldo)
            elif tipo == "bolsilloTrabajadores":
                saldo1 = self._bolsilloTrabajadores - valor
                self.setBolsilloTrabajadores(saldo1)
            elif tipo == "bolsilloInventario":
                saldo2 = self._bolsilloInventario - valor
                self.setBolsilloInventario(saldo2)
            elif tipo == "bolsilloTransporte":
                saldo3 = self._bolsilloTransporte - valor
                self.setBolsilloTransporte(saldo3)
            elif tipo == "bolsilloEstablecimientos":
                saldo4 = self._bolsilloEstablecimientos - valor
                self.setBolsilloEstablecimientos(saldo4)
        else:
            cobroAdicional = self.getCobroAdicional()
            if tipo == "saldo":
                saldo = self._saldo - (valor + cobroAdicional)
                self.setSaldo(saldo)
            elif tipo == "bolsilloTrabajadores":
                saldo = self._bolsilloTrabajadores - (valor + cobroAdicional)
                self.setBolsilloTrabajadores(saldo)
            elif tipo == "bolsilloInventario":
                saldo = self._bolsilloInventario - (valor + cobroAdicional)
                self.setBolsilloInventario(saldo)
            elif tipo == "bolsilloTransporte":
                saldo = self._bolsilloTransporte - (valor + cobroAdicional)
                self.setBolsilloTransporte(saldo)
            elif tipo == "bolsilloEstablecimientos":
                saldo = self._bolsilloEstablecimientos - (valor + cobroAdicional)
                self.setBolsilloEstablecimientos(saldo)
    
        saldoCuenta = cuentaCorriente._saldo + valor
        cuentaCorriente.setSaldo(saldoCuenta)

    # Getters
    def getNumeroCuenta(self):
        return self.numero_cuenta

    def getTitular(self):
        return self._titular

    def getBanco(self):
        return self._banco

    def getBolsilloTrabajadores(self):
        return self._bolsilloTrabajadores

    def getBolsilloInventario(self):
        return self._bolsilloInventario

    def getBolsilloTransporte(self):
        return self._bolsilloTransporte

    def getBolsilloEstablecimientos(self):
        return self._bolsilloEstablecimientos

    def getBolsilloPagoCredito(self):
        return self._bolsilloPagoCredito

    def getSaldo(self):
        return self._saldo

    def getCredito(self):
        return self._credito
    
    def getInteres(self):
        return self._interes
    
    def getCobroAdicional(self):
        return self._cobroAdicional

    # Setters
    def setNumeroCuenta(self, numero_cuenta):
        self._numero_cuenta = numero_cuenta

    def setTitular(self, titular):
        self._titular = titular

    def setBanco(self, banco):
        self._banco = banco

    def setBolsilloTrabajadores(self, bolsillo_trabajadores):
        self._bolsilloTrabajadores = bolsillo_trabajadores
        self.actualizarSaldo()

    def setBolsilloInventario(self, bolsillo_inventario):
        self._bolsilloInventario = bolsillo_inventario
        self.actualizarSaldo()

    def setBolsilloTransporte(self, bolsillo_transporte):
        self._bolsilloTransporte = bolsillo_transporte
        self.actualizarSaldo()

    def setBolsilloEstablecimientos(self, bolsillo_establecimientos):
        self._bolsilloEstablecimientos = bolsillo_establecimientos
        self.actualizarSaldo()

    def setBolsilloPagoCredito(self, bolsillo_pago_credito):
        self._bolsilloPagoCredito = bolsillo_pago_credito
        self.actualizarSaldo()

    def setSaldo(self, saldo):
        self._saldo = saldo

    def setCredito(self, credito):
        self._credito = credito
    
    def setInteres(self, interes):
        self._interes = interes
    
    def setCobroAdicional(self, cobroAdicional):
        self._cobroAdicional = cobroAdicional

    def actualizarSaldo(self):
        self._saldo = (self._bolsilloTrabajadores + self._bolsilloInventario +
                      self._bolsilloTransporte + self._bolsilloEstablecimientos +
                      self._bolsilloPagoCredito)

    