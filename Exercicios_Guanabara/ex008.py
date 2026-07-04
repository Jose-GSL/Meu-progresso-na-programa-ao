metro = float(input('Digite um valor em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10 
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'a medida de {metro} corresponde a ')
print(f'{km:.2f}km, {hm:.2f}hm, {dam:.2f}dam, {dm:.2f}dm, {cm:.2f}cm e {mm:.2f}mm')
