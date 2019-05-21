
Feature: Registro Satisfactorio Informatica
    Como postulante requiero registrar mi Programa Informatico

    Scenario Outline: Postulante registra su programa correctamente
        Given postulante se encuentra en opcion Informatica
        When postulante hace click en boton Agregar Conocimiento
        When postulante ingresa un conocimiento <conocimiento>
        When postulante selecciona primera opcion de conocimiento
        When postulante selecciona nivel de conocimiento <nivel>
        When postulante hace click en boton Guardar Conocimiento
        Then postulante visualiza tooltip de confirmacion de Conocimiento Guardado <mensaje>

            Examples: Credenciales
                |   conocimiento    |   nivel        |       mensaje                                        |
                |   Excel           |   Intermedio   |  Se creó el programa del postulante correctamente    |