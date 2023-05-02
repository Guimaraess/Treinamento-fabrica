km = float(input('digite a kilometragem:'))
if km <= 200:
  preço = 1.50 * km
else:
  preço = 1.25 * km
print('o preço da viagem {}'.format(preço))