from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Informatica")
def postulante_selecciona_opc_infromatica(context):
    programa_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[8]") 
    programa_opc.click()

@when(u"postulante hace click en boton Agregar Conocimiento")
def postulante_click_btn_agrega_conoc(context):
    context.web.time_sleep()
    add_conoc_btn = context.web.find_by_id("computingSkillsAddBtn")
    add_conoc_btn.click()

@when(u"postulante ingresa un conocimiento {conocimiento}")
def postulante_ingresa_conocimient(context, conocimiento):
    computingSkills_field = context.web.find_by_id("programcomputingSkills")
    computingSkills_field.send_keys(str(conocimiento))

@when(u"postulante selecciona primera opcion de conocimiento")
def postulante_selecciona_prim_opc(context):
    computingSkills_select = context.web.find_by_id("react-autowhatever-1--item-0")
    computingSkills_select.click()

@when(u"postulante selecciona nivel de conocimiento {nivel}")
def postulante_selecciona_niv_conoc(context, nivel):
    level_field = context.web.find_by_id("levelcomputingSkills")
    level_field.send_keys(str(nivel))

@when(u"postulante hace click en boton Guardar Conocimiento")
def postulante_click_btn_guardarconoc(context):
    addcomputingSkills_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[9]/div[1]/div/form/div/div[2]/button[2]")
    addcomputingSkills_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Conocimiento Guardado {mensaje}")
def postulante_tooltip_compskills_conf(context, mensaje):
    correcto_tooltip_compskills = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip_compskills.text)









