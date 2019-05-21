@skip
# language: en
Feature: Login Postulante
    Como postulante requiero iniciar sesión en el portal aptitus.com para acceder a Mi cuenta

    Scenario Outline: Postulante ingresa con usuario y contrasenia correctamente        
        Given postulante ingresa a Aptitus
        When postulante hace click en link Ingresa
        When postulante ingresa email <email>
        When postulante ingresa constrasenia <contrasenia>
        When postulante hace click en boton Ingresar
        When postulante espera unos segundos
        Then postulante visualiza la vista Perfil <vista>

            Examples: Credenciales
                | email                           | contrasenia | vista           |
                | postulante6_dev4c@ecodigital.pe | 123456      | Destacar Perfil |


