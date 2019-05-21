from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion otro estudio")
def postulante_selecciona_opc_otro_estudio(context):
    otro_estudio_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[6]")
    otro_estudio_opc.click()

@when(u"postulante hace click en boton Agregar Otro Estudio")
def postulante_click_boton_agregar_otestudio(context):
    context.web.time_sleep()
    add_oe_btn = context.web.find_by_id("otherStudiesAddBtn")
    add_oe_btn.click()

@when(u"postulante ingresa otro estudio nombre {otro_estudio}")
def postulante_ingresa_nomb_otest(context, otro_estudio):
    other_study_field = context.web.find_by_id("nameotherStudies")
    other_study_field.send_keys(str(otro_estudio))

@when(u"postulante ingresa otro estudio institucion {institucion}")
def postulante_ingresa_int(context, institucion):
    institution_field = context.web.find_by_id("institutionotherStudies")
    institution_field.send_keys(str(institucion))

@when(u"postulante selecciona tipo otro estudio {otro_estudio_tipo}")
def postulante_selecciona_tipest(context, otro_estudio_tipo):
    other_study_type_field = context.web.find_by_id("otherStudyTypeIdotherStudies")
    other_study_type_field.send_keys(str(otro_estudio_tipo))

@when(u"postulante selecciona pais {pais}")
def postulante_selecciona_pais(context, pais):
    country_field = context.web.find_by_id("countryIdotherStudies")
    country_field.send_keys(str(pais))

@when(u"postulante selecciona un mes inicio de otro estudio {mes_inicio}")
def postulante_selecciona_ms_ini(context, mes_inicio):
    start_month_otes_field = context.web.find_by_id("startMonthotherStudies")
    start_month_otes_field.send_keys(str(mes_inicio))

@when(u"postulante selecciona un anio inicio de otro estudio {anio_inicio}")
def postulante_selecciona_anio_ini(context,anio_inicio):
    start_year_otes_field = context.web.find_by_id("startYearotherStudies")
    start_year_otes_field.send_keys(str(anio_inicio))

@when(u"postulante selecciona un mes fin de otro estudio {mes_fin}")
def postulante_selecciona_ms_fin(context, mes_fin):
    end_month_otes_field = context.web.find_by_id("endMonthotherStudies")
    end_month_otes_field.send_keys(str(mes_fin))

@when(u"postulante selecciona un anio fin de otro estudio {anio_fin}")
def postulante_selecciona_anio_fin(context, anio_fin):
    end_year_otes_field = context.web.find_by_id("endYearotherStudies")
    end_year_otes_field.send_keys(str(anio_fin))

@when(u"postulante hace click en boton Guardar Otro Estudio")
def postulante_click_btn_ot_est(context):
    addotherstudy_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[7]/div[1]/div/form/div/div[5]/button[2]")
    addotherstudy_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Otro Estudio Guardado {mensaje}")
def postulante_tooltip_otes_conf(context, mensaje):
    correcto_tooltip_otes = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip_otes.text)

















