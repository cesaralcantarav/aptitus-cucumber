from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Presentacion")
def postulante_selecciona_opc_presentacion(context):
    context.web.time_sleep()
    presentacion_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[3]")
    presentacion_opc.click()

@when(u"postulante hace click en boton Editar Presentacion")
def postulante_click_boton_edit_pres(context):
    presentacion_btn = context.web.find_by_id("btnEditpresentation1")
    presentacion_btn.click()

@when(u"postulante ingresa su presentacion {presentacion}")
def postulante_ingresa_presentacion(context, presentacion):
    prese_field = context.web.find_by_name("summary")
    prese_field.send_keys(str(presentacion))

@when(u"postulante hace click en boton Guardar Presentacion")
def postulante_click_btn_guar(context):
    guard_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[4]/div[2]/form/div/div[3]/button[2]/span/span")
    guard_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Presentacion Guardada {mensaje}")
def postulante_confirma_pres(context, mensaje):
    correcto_tooltip = context.web.find_by_class_name("g-notify_message")
    assert (mensaje==correcto_tooltip.text)








