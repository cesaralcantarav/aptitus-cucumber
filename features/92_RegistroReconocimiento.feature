
Feature: Registro Satisfactorio Reconocimiento
    Como postulante requiero registrar mi Reconocimiento

    Scenario Outline: Postulante registra su reconocimiento correctamente
        Given postulante se encuentra en opcion Reconocimiento
        When postulante hace click en boton Agregar Reconocimiento
        When postulante ingresa un titulo <titulo>
        When postulante ingresa un emisor <emisor>
        When postulante selecciona un mes de logro <mes_inicio>
        When postulante selecciona un anio de logro <anio_inicio>
        When postulante ingresa descripcion del logro <descripcion>
        When postulante hace click en boton Guardar Reconocimiento
        Then postulante visualiza tooltip de confirmacion de Reconocimiento Guardado <mensaje>

            Examples: Credenciales
                |   titulo                                                          |       emisor                       |  mes_inicio | anio_inicio |   descripcion                                                                                                                  |             mensaje                             |
                |   Taller Básico "Manipulación, Almacenamiento y Transporte de GLP"|   Ministerio de Petróleo y Minería |  Julio      |    2018     |Certificado que demuestra mi conocimiento en la gestión (manipulación, almacenamiento y transporte) de Gas Licuado al Petróleo. | Se creó el logro del postulante correctamente.  |


