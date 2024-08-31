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
        self.credito = []
        self.interes = 0
        self.cobroAdicional = 0

        if banco:
            self.establecer_valores(banco)

        # Calcula el saldo si se pasan valores específicos de bolsillo
        if bolsillo_trabajadores or bolsillo_inventario or bolsillo_transporte or bolsillo_establecimientos or bolsillo_pago_credito:
            self.saldo = (bolsillo_trabajadores + bolsillo_inventario + 
                          bolsillo_transporte + bolsillo_establecimientos + bolsillo_pago_credito)

        CuentaBancaria.cuentas.append(self)
        self.credito = []
    
    def establecer_valores(self, banco):
            banco = self.banco
            banco1 = Banco[banco]
            self.interes = Banco.banco1.INTERES
            self.cobroAdicional = Banco.banco1.COBRO_ADICIONAL

    def depositar(self, cantidad, tipo):
        if(tipo == "saldo"):
            if (cantidad > 0):
                self.saldo += cantidad

        elif(tipo == "bolsilloTrabajadores"):
            if (cantidad > 0):
                self.bolsilloTrabajadores += cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
            
        elif(tipo == "bolsilloInventario"):
            if (cantidad > 0):
                self.bolsilloInventario += cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        
        elif(tipo == "bolsilloTransporte"):
    	    if (cantidad > 0):
                self.bolsilloTransporte += cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        
        elif(tipo == "bolsilloEstablecimientos"):
    	    if (cantidad > 0):
                self.bolsilloEstablecimientos += cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        
        elif(tipo == "bolsilloPagoCredito"):
    	    if (cantidad > 0):
                self.bolsilloPagoCredito += cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
    
    def retirar(self, cantidad, tipo):
        if(tipo == "saldo"):
     	    if (cantidad <= saldo):
                self.saldo -= cantidad;
           
        elif(tipo == "bolsilloTrabajadores"):
       	    if (cantidad <= bolsilloTrabajadores):
                self.bolsilloTrabajadores -= cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        elif(tipo == "bolsilloInventario"):
       	    if (cantidad <= bolsilloInventario):
                self.bolsilloInventario -= cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        elif(tipo == "bolsilloTransporte"):
       	    if (cantidad <= bolsilloTransporte):
                self.bolsilloTransporte -= cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        elif(tipo == "bolsilloEstablecimientos"):
       	    if (cantidad <= bolsilloEstablecimientos):
                self.bolsilloEstablecimientos -= cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
        elif (tipo == "bolsilloPagoCredito"):
    	    if (cantidad <= bolsilloPagoCredito):
                self.bolsilloPagoCredito -= cantidad
                self.saldo = bolsilloTrabajadores + bolsilloTransporte + bolsilloInventario + bolsilloEstablecimientos + bolsilloPagoCredito
      

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
            saldo = self.saldo - valor
            self.setSaldo(saldo)
        else:
            cobroAdicional = self.getCobroAdicional()
            saldo = self.saldo - (valor + cobroAdicional)
            self.setSaldo(saldo)
    
        saldoCuentaAhorros = cuentaAhorros.saldo + valor
        cuentaAhorros.setSaldo(saldoCuentaAhorros)
    
        porcentajeInteres = self.getInteres()
        interes = cuentaAhorros.obtenerSaldo() * porcentajeInteres
        saldoFinal = cuentaAhorros.obtenerSaldo() - interes
        cuentaAhorros.setSaldo(saldoFinal)

    def transaccion(self, valor, cuentaCorriente, tipo):
        if self.getBanco() == cuentaCorriente.getBanco():
            if tipo == "saldo":
                saldo = self.saldo - valor
                self.setSaldo(saldo)
            elif tipo == "bolsilloTrabajadores":
                saldo1 = self.bolsilloTrabajadores - valor
                self.setBolsilloTrabajadores(saldo1)
            elif tipo == "bolsilloInventario":
                saldo2 = self.bolsilloInventario - valor
                self.setBolsilloInventario(saldo2)
            elif tipo == "bolsilloTransporte":
                saldo3 = self.bolsilloTransporte - valor
                self.setBolsilloTransporte(saldo3)
            elif tipo == "bolsilloEstablecimientos":
                saldo4 = self.bolsilloEstablecimientos - valor
                self.setBolsilloEstablecimientos(saldo4)
        else:
            cobroAdicional = self.getCobroAdicional()
            if tipo == "saldo":
                saldo = self.saldo - (valor + cobroAdicional)
                self.setSaldo(saldo)
            elif tipo == "bolsilloTrabajadores":
                saldo = self.bolsilloTrabajadores - (valor + cobroAdicional)
                self.setBolsilloTrabajadores(saldo)
            elif tipo == "bolsilloInventario":
                saldo = self.bolsilloInventario - (valor + cobroAdicional)
                self.setBolsilloInventario(saldo)
            elif tipo == "bolsilloTransporte":
                saldo = self.bolsilloTransporte - (valor + cobroAdicional)
                self.setBolsilloTransporte(saldo)
            elif tipo == "bolsilloEstablecimientos":
                saldo = self.bolsilloEstablecimientos - (valor + cobroAdicional)
                self.setBolsilloEstablecimientos(saldo)
    
        saldoCuenta = cuentaCorriente.saldo + valor
        cuentaCorriente.setSaldo(saldoCuenta)

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
    
    def getInteres(self):
        return self.interes
    
    def getCobroAdicional(self):
        return self.cobroAdicional

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
    
    def setInteres(self, interes):
        self.interes = interes
    
    def setCobroAdicional(self, cobroAdicional):
        self.cobroAdicional = cobroAdicional

    def actualizarSaldo(self):
        self.saldo = (self.bolsillo_trabajadores + self.bolsillo_inventario +
                      self.bolsillo_transporte + self.bolsillo_establecimientos +
                      self.bolsillo_pago_credito)

    