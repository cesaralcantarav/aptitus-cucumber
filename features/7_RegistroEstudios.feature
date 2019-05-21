
Feature: Registro Satisfactorio Estudio
    Como postulante requiero registrar mi Estudio

    Scenario Outline: Postulante registra su estudio correctamente
        Given postulante se encuentra en opcion estudio
        When postulante hace click en boton Agregar Estudio
        When postulante selecciona Grado <grado>
        When postulante selecciona Estado <estado>
        When postulante ingresa Institucion <institucion>
        When postulante selecciona primera opcion segun su institucion
        When postulante ingresa Carrera <carrera>
        When postulante selecciona un mes inicio de estudio <mes_inicio>
        When postulante selecciona un anio inicio de estudio <anio_inicio>
        When postulante selecciona un mes fin de estudio <mes_fin>
        When postulante selecciona un anio fin de estudio <anio_fin>
        When postulante selecciona un pais <pais>
        When postulante hace click en boton Guardar Estudios
        Then postulante visualiza tooltip de confirmacion de Estudio Guardado <mensaje>

            Examples: Credenciales
                |   grado            |   estado     |   institucion                 |   carrera         |   mes_inicio  |   anio_inicio |   mes_fin |  anio_fin |   pais    |   mensaje                                         |
                |   Universitario    |  Titulado    |   Universidad del Pacifico    |   Arquitectura    |   Enero       |   2015        |   Octubre |   2015    |   Perú    |   Se creó el estudio del postulante correctamente |

