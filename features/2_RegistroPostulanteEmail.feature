Feature: Registro Postulante
    Como postulante requiero registrarme en el portal aptitus.com

    Scenario Outline: Postulante se registra con email y clave correctamente        
        Given postulante ingresa a Aptitus para registrarse
        When postulante hace click en link Registrate
        When postulante ingresa nombre <nombre>
        When postulante ingresa apellido paterno <ape_pat>
        When postulante ingresa apellido materno <ape_mat>
        When postulante ingresa e-mail para registrarse <email>
        When postulante ingresa contrasenia para registrarse <contrasenia>
        When postulante ingresa trabajo ideal <trabajo_ideal>
        When postulante espera
        When postulante selecciona opcion del autocomplete
        When postulante espera2
        When postulante selecciona lugar ideal
        When postulante hace click en boton Crear cuenta
        When postulante espera unos segundos
        Then postulante visualiza la vista Mi Perfil <vista>

            Examples: Data
                |   nombre      |    ape_pat    |   ape_mat     |   email                                |   contrasenia |   trabajo_ideal       |   lugar_ideal     |   vista           |
                |   Zarela      |   Monteverde  |   Velasquez   |   zarela.montemayor42@ecodigital.pe    |   123456      |   Analista            |   Amazonas        |   Destacar Perfil |


