
Feature: Registro Satisfactorio Pretension Salarial
    Como postulante requiero registrar mi pretension salarial

    Scenario Outline: Postulante registra su pretension salarial correctamente 
        Given postulante se encuentra en opcion Pretension Salarial
        When postulante hace click en boton Editar Pretension Salarial
        When postulante ingresa su pretension salarial <pretension>
        When postulante hace click en boton Guardar
        Then postulante visualiza tooltip de confirmacion pretension guardada <mensaje_pret>

            Examples: Credenciales
                |   pretension  |   mensaje_pret                                        |
                |   400000      |   Se actualizó correctamente su pretensión salarial   |
     