import clases

persona = clases.Persona()
persona.setNombre("Ivo")
persona.setApellido("Ferrari")
persona.setAltura("1.77")
persona.setEdad("25")

print(persona.getNombre())
print(persona.getApellido())

Ivo = clases.Informatico()
Ivo.setNombre("Ivo")
Ivo.aprender("Python")
print(Ivo.getLenguajes())