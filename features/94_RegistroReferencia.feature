Feature: Registro Satisfactorio Referencia
    Como postulante requiero registrar mi Referencia

    Scenario Outline: Postulante registra su referencia correctamente
        Given postulante se encuentra en opcion Referencias
        When postulante hace click en boton Agregar Referencia
        When postulante selecciona primera experiencia del listado
        When postulante ingresa el nombre de referencia <nombre>
        When postulante ingresa puesto que ocupa su referencia <puesto>
        When postulante ingresa el email de su referencia <email>
        When postulante ingresa el telefono de su referencia <telefono>
        When postulante hace click en boton Guardar Referencia
        Then postulante visualiza tooltip de confirmacion de Referencia Guardada <mensaje>

            Examples: Credenciales
                |   nombre                      |   puesto          |   email                       |   telefono    |                           mensaje                 |
                |   ING. ROCIO ALBERCA PERALES  |   Jefe de Sistemas|   mvasquez@ecodigital.com.pe  |   962542826   |Se creó la referencia del postulante correctamente.|  

