from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion estudio")
def postulante_selecciona_opc_estudio(context):
    context.web.time_sleep()
    estudio_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[4]")
    estudio_opc.click()

@given(u"postulante hace click en boton Agregar Estudio")
def postulante_click_boton_agregar_estudio(context):
    add_est_btn = context.web.find_by_id("studiesAddBtn")
    add_est_btn.click

@when(u"postulante selecciona Grado {grado}")
def postulante_selecciona_grado(context, grado):
    area_field = context.web.find_by_id("gradeIdstudies")
    area_field.send_keys(str(grado))


@when(u"postulante selecciona Estado {estado}")
def postulante_selecciona_estado(context, estado):
    state_field = context.web.find_by_id("stateIdstudies")
    state_field.send_keys(str(estado))

@when(u"postulante ingresa Institucion {institucion}")
def postulante_ingresa_institucion(context, estado):
    institution_field = context.web.find_by_id("institutionstudies")
    institution_field.send_keys(str(institucion))
    context.time_sleep()

@when(u"postulante ingresa Carrera {carrera}")
def postulante_ingresa_carrera(context, carrera):
    career_field = context.web.find_by_id("careerstudies")
    career_field.send_keys(str(carrera))

@when(u"postulante selecciona un mes inicio de estudio {mes_inicio}")
def postulante_selecciona_ms_ini(context, mes_inicio):
    start_month_exp_field = context.web.find_by_id("startMonthstudies")
    start_month_exp_field.send_keys(str(mes_inicio))

@when(u"postulante selecciona un anio inicio de estudio {anio_inicio}")
def postulante_selecciona_anio_ini(context, anio_inicio):
    start_year_exp_field = context.web.find_by_id("startYearstudies")
    start_year_exp_field.send_keys(str(anio_inicio))

@when(u"postulante selecciona un mes fin de estudio {mes_fin}")
def postulante_selecciona_ms_fin(context, mes_fin):
    end_month_exp_field = context.web.find_by_id("endMonthstudies")
    end_month_exp_field.send_keys(str(mes_fin))

@when(u"postulante selecciona un anio fin de estudio {anio_fin}")
def postulante_selecciona_anio_fin(context, anio_fin):
    end_year_exp_field = context.web.find_by_id("endYearstudies")
    end_year_exp_field.send_keys(str(anio_fin))

@when(u"postulante selecciona un pais {pais}")
def postulante_selecciona_pais(context, pais):
    country_field = context.web.find_by_id("countryIdstudies")
    country_field.send_keys(str(pais))

@when(u"postulante hace click en boton Guardar Estudios")
def postulante_click_btn(context):
    addstudy_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[6]/div[1]/div/form/div/div[5]/button[2]")
    addstudy_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Estudio Guardado")
def postulante_tooltip_conf(context, mensaje):
    correcto_tooltip = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip.text)
    







        

