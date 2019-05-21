from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Aptitudes")
def postulante_selecciona_opc_aptitudes(context):
    aptitudes_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[10]") 
    aptitudes_opc.click()

@when(u"postulante hace click en boton Agregar Aptitud")
def postulante_click_btn_argaptitus(context):
    context.web.time_sleep()
    add_apt_btn = context.web.find_by_id("aptitudesAddBtn")
    add_apt_btn.click()

@when(u"postulante ingresa Aptitud {aptitud}")
def postulante_ingresa_aptitud(context, aptitud):
    aptitude_field = context.web.find_by_id("nameaptitudes")
    aptitude_field.send_keys(str(aptitud))

@when(u"postulante hace click en boton Guardar Aptitud")
def postulante_click_btn_guard_apt(context):
    addaptitude_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[11]/div/div[1]/div/form/div/div[2]/button[2]")
    addaptitude_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Aptitud Guardada {mensaje}")
def postulante_tooltip_aptitude_conf(context, mensaje):
    correcto_tooltip_aptitude = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip_aptitude.text)


