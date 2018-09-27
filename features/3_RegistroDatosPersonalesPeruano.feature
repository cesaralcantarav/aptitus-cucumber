
Feature: Registro Datos Personales Peruano
    Como postulante peruano requiero registrar mis datos Personales

    Scenario Outline: Postulante peruano registra sus datos personales correctamente 
        Given postulante ingresa a Aptitus para registrar sus datos
        When postulante hace click para desplegar el menu
        When postulante hace click en menu Mi Perfil
        When postulante hace click en botón Editar Datos Personales
        When postulante registra su nombre <nombre>
        When postulante registra su apellido paterno <ape_pat>
        When postulante registra su apellido materno <ape_mat>
        When postulante registra su fecha de nacimiento <fech_nac>
        When postulante selecciona su genero <genero>
        When postulante selecciona su tipo de documento <tipo_doc>
        When postulante registra su numero de documento <num_doc>
        When postulante registra su celular <celular>
        When postulante registra su telefono fijo <telef_fijo>
        When postulante selecciona su estado civil <estado_civil>
        When postulante ingresa su ubicacion <ubicacion>
        When postulante espera que se deplieguen opciones
        When postulante selecciona la primera opción segun su ubicacion
        When postulante registra su direccion <direccion>
        When postulante hace click en botón Guardar
        Then postulante visualiza tooltip con mensaje <mensaje>

            Examples: Credenciales
                |   nombre   |   ape_pat         |   ape_mat     |   fech_nac    |   genero      |   tipo_doc    |   num_doc     |   celular     |   telef_fijo  |   estado_civil    |   ubicacion                       |   direccion                   |   mensaje                                                     |
                |   NombEdit |  Apepat         |    Apemat    |   25/12/1993  |   Femenino   |   DNI         |   09994356    |   123456789   |   3492968     |   Unión Libre     |   San Isidro, Lima, Lima, Perú    |   Calle los geranios nro 23   |   Se actualizó la información del postulante correctamente.   |
           





