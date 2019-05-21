
Feature: Registro Satisfactorio Aptitud
    Como postulante requiero registrar mi Aptitud

    Scenario Outline: Postulante registra su aptitud correctamente
        Given postulante se encuentra en opcion Aptitudes
        When postulante hace click en boton Agregar Aptitud
        When postulante ingresa Aptitud <aptitud>
        When postulante hace click en boton Guardar Aptitud
        Then postulante visualiza tooltip de confirmacion de Aptitud Guardada <mensaje>

            Examples: Credenciales
                |   aptitud         |   mensaje                                            |   
                |   proactivo       |    Se creó la habilidad del postulante correctamente | 

