from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Referencias")
def postulante_selecciona_opc_aptitudes(context):
    aptitudes_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[10]") 
    aptitudes_opc.click()

@when(u"postulante hace click en boton Agregar Referencia")
def postulante_click_btn_agrega_referencia(context):
    context.web.time_sleep()
    add_refer_btn = context.web.find_by_id("referencesAddBtn")
    add_refer_btn.click()

@when(u"postulante selecciona primera experiencia del listado")
def postulant_selects_first_experience(context):
    experienceReference_select = context.web.find_by_xpath("//*[@id='experienceIdreferences']/option[2]")
    experienceReference_select.click()

@when(u"postulante ingresa el nombre de referencia {nombre}")
def postulante_ingresa_nombre(context, nombre):
    referenceName_field = context.web.find_by_id("namereferences")
    referenceName_field.send_keys(str(nombre))

@when(u"postulante ingresa puesto que ocupa su referencia {puesto}")
def postulante_ingresa_puesto(context, puesto):
    job_field = context.web.find_by_id("jobreferences")
    job_field.send_keys(str(puesto))

@when(u"postulante ingresa el email de su referencia {email}")
def postulante_ingresa_email(context, email):
    email_field = context.web.find_by_id("emailreferences")
    email_field.send_keys(str(email))

@when(u"postulante ingresa el telefono de su referencia {telefono}")
def postulante_ingresa_telefono(context, telefono):
    telep_cellp_field = context.web.find_by_id("primaryCellphonereferences")
    telep_cellp_field.send_keys(str(telefono))

@when(u"postulante hace click en boton Guardar Referencia")
def postulante_click_btn_guardrefer(context):
    addreference_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[12]/div[1]/div/form/div/div[4]/button[2]")
    addreference_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Referencia Guardada {mensaje}")
def postulante_tooltip_reference_conf(context, mensaje):
    correcto_tooltip_reference = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip_reference.text)






