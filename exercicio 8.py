medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
print ('A media de {:.0f}m corresponde a {:.0f}cm e {:.0f}mm e {:.0f}dm '.format(medida, cm, mm, dm))
