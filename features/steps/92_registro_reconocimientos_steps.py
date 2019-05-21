from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Reconocimiento")
def postulante_selecciona_opc_reconocimiento(context):
    reconocimiento_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[9]") 
    reconocimiento_opc.click()

@when(u"postulante hace click en boton Agregar Reconocimiento")
def postulante_click_btn_agrega_recon(context):
    context.web.time_sleep()
    add_recon_btn = context.web.find_by_id("awardsAddBtn")
    add_recon_btn.click()

@when(u"postulante ingresa un titulo {titulo}")
def postulante_ingresa_titulo(context, titulo):
    awards_field = context.web.find_by_id("titleawards")
    awards_field.send_keys(str(titulo))

@when(u"postulante ingresa un emisor {emisor}")
def postulante_ingresa_emisor(context, emisor):
    issueraward_field = context.web.find_by_id("issuerawards")
    issueraward_field.send_keys(str(emisor))

@when(u"postulante selecciona un mes de logro {mes_inicio}")
def postulante_selecciona_mes_logro(context, mes_inicio):
    monthawards_field = context.web.find_by_id("monthawards")
    monthawards_field.send_keys(str(mes_inicio))

@when(u"postulante selecciona un anio de logro {anio_inicio}")
def postulante_selecciona_anio_logro(context, anio_inicio):
    yearawards_field = context.web.find_by_id("yearawards")
    yearawards_field.send_keys(str(anio_inicio))

@when(u"postulante ingresa descripcion del logro {descripcion}")
def postulante_selecciona_descrip(context, descripcion):
    descriptionawards_field = context.web.find_by_id("descriptionawards")
    descriptionawards_field.send_keys(str(descripcion))

@when(u"postulante hace click en boton Guardar Reconocimiento")
def postulante_click_btn_guard_reconocimiento(context):
    adddescriptionawards_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[10]/div[1]/div/form/div/div[4]/button[2]")
    adddescriptionawards_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Reconocimiento Guardado {mensaje}")
def postulante_tooltip_award_conf(context, mensaje):
    correcto_tooltip_award = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip_award.text)







