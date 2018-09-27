Feature: Registro Satisfactorio Experiencia
    Como postulante requiero registrar mi Experiencia

    Scenario Outline: Postulante registra su experiencia correctamente
        Given postulante se encuentra en opcion experiencia
        When postulante hace click en boton Agregar Experiencia
        When postulante ingresa la empresa <empresa>
        When postulante ingresa la industria <industria>
        When postulante ingresa el puesto <puesto>
        When postulante selecciona el nivel de puesto <nivel_puesto>
        When postulante selecciona el area <area>
        When postulante selecciona un mes inicio de experiencia <mes_inicio>
        When postulante ingresa un año inicio de experiencia <anio_inicio>
        When postulante selecciona un mes fin de experiencia <mes_fin>
        When postulante ingresa un año fin de experiencia <anio_fin>
        When postulante ingresa una descripción <descripcion>
        When postulante hace click en boton Guardar Experiencia
        Then postulante visualiza tooltip de confirmacion de Experiencia Guardada <mensaje>

            Examples: Credenciales
                |     empresa       |   industria   |   puesto              |   nivel_puesto            |   area                                       |   mes_inicio   |anio_inicio|   mes_fin |anio_fin|   descripcion             |   mensaje                                            |
                |   Ovicar s.a.c    |   Sistemas    |   Analista de T.I     |   Técnicos / Operativos   |   Tecnología, Sistemas y Telecomunicaciones  |    Diciembre   |   2015    | Noviembre | 2016   |   Esta es la descripcion  |  Se creó la experiencia del postulante correctamente |






    