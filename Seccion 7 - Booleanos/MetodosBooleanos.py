cadena = "Estoy mostrando los metodos booleanos para las Strings"
cadena2 = "CMSJDNfFISDNFISDNCINXICNDIUNSIJND"
cadena3 = "cmindcvndsifdnfijofnisncnsmed"

print(cadena.startswith("e")) #False - No empieza con e, es case sensitive
print(cadena.endswith("S")) #False - No termina con S, es case sensitive

print(cadena2.isupper()) #True - Esta todo en mayusculas
print(cadena3.islower()) #True - Esta todo en minusculas