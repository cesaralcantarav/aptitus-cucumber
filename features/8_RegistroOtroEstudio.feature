
Feature: Registro Satisfactorio Otro Estudio
    Como postulante requiero registrar mi Otro Estudio

    Scenario Outline: Postulante registra su otro estudio correctamente
        Given postulante se encuentra en opcion otro estudio
        When postulante hace click en boton Agregar Otro Estudio
        When postulante ingresa otro estudio nombre <otro_estudio>
        When postulante ingresa otro estudio institucion <institucion>
        When postulante selecciona tipo otro estudio <otro_estudio_tipo>
        When postulante selecciona pais <pais>
        When postulante selecciona un mes inicio de otro estudio <mes_inicio>
        When postulante selecciona un anio inicio de otro estudio <anio_inicio>
        When postulante selecciona un mes fin de otro estudio <mes_fin>
        When postulante selecciona un anio fin de otro estudio <anio_fin>
        When postulante hace click en boton Guardar Otro Estudio 
        Then postulante visualiza tooltip de confirmacion de Otro Estudio Guardado <mensaje>

            Examples: Credenciales
                |   otro_estudio    |   institucion              | otro_estudio_tipo|   pais                |   mes_inicio  | anio_inicio |   mes_fin | anio_fin    |    mensaje                                               |
                |   Curso de cobol  |   Universidad de Santander |  Especialización |Santa Sede (Vaticano)  |   Septiembre  |   1990      | Enero     | 2000         | Se creó el otro estudio del postulante correctamente.    |

