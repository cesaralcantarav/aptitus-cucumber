
Feature: Registro Satisfactorio Idioma
    Como postulante requiero registrar mi Idioma

    Scenario Outline: Postulante registra su idioma correctamente
        Given postulante se encuentra en opcion idioma
        When postulante hace click en boton Agregar Idioma
        When postulante selecciona un Idioma <idioma>
        When postulante selecciona nivel escrito <nivel_escrito>
        When postulante selecciona nivel oral <nivel_oral>
        When postulante hace click en boton Guardar Idioma
        Then postulante visualiza tooltip de confirmacion de Idioma Guardado <mensaje>

            Examples: Credenciales
                |   idioma     |      nivel_escrito    |   nivel_oral  |   mensaje                                             |
                |   Italiano   |   Básico              |   Intermedio  |   Se agregó el idioma del postulante correctamente.   |