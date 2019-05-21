from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion idioma")
def postulante_selecciona_opc_idioma(context):
    idioma_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[7]")                           
    idioma_opc.click()

@when(u"postulante hace click en boton Agregar Idioma")
def postulante_click_boton_agidioma(context):
    add_idioma_btn = context.web.find_by_id("languagesAddBtn")
    add_idioma_btn.click()

@when(u"postulante selecciona un Idioma {idioma}")
def postulante_selecciona_idioma(context, idioma):
    language_field = context.web.find_by_id("languageIdlanguages")
    language_field.send_keys(str(idioma))

@when(u"postulante selecciona nivel escrito {nivel_escrito}")
def postulante_selecciona_nivel_escrito(context, nivel_escrito):
    writing_Level_field = context.web.find_by_id("writingLevellanguages")
    writing_Level_field.send_keys(str(nivel_escrito))
    
@when(u"postulante selecciona nivel oral {nivel_oral}")
def postulante_selecciona_nivel_oral(context, nivel_oral):
    speaking_Level_field = context.web.find_by_id("speakingLevellanguages")
    speaking_Level_field.send_keys(str(nivel_oral))

@when(u"postulante hace click en boton Guardar Idioma")
def postulante_click_btn_guar_idio(context):
    addlanguage_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[8]/div[1]/div/form/div/div[3]/button[2]")
    addlanguage_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Idioma Guardado {mensaje}")
def postulante_tooltip_lang_conf(context, mensaje):
    context.web.time_sleep()
    correcto_tooltip_lang = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip_lang.text)





