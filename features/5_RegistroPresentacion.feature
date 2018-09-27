Feature: Registro Satisfactorio Presentacion
    Como postulante requiero registrar mi presentacion

    Scenario Outline: Postulante registra su presentacion correctamente
        Given postulante se encuentra en opcion Presentacion
        When postulante hace click en boton Editar Presentacion
        When postulante ingresa su presentacion <presentacion>
        When postulante hace click en boton Guardar Presentacion
        Then postulante visualiza tooltip de confirmacion de Presentacion Guardada <mensaje>

            Examples: Credenciales
                |   presentacion    |   mensaje              |  
                |   ING. ELECTRONICO DE LA UNMSM - TITULADO 2013, proactivo,dispuesto a asumir retos y con ellos incrementar mi experiencia laboral actual, con aspiraciones de participar en la gran diversidad de aplicaciones de la ingeniería.  |   Se actualizó correctamente su información de Presentación   | 

        
