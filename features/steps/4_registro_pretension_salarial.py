from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Pretension Salarial")
def postulante_selecciona_opc_pretension(context):
    context.web.time_sleep()
    pretension_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[2]")
    pretension_opc.click()


@when("postulante hace click en boton Editar Pretension Salarial")
def postulante_click_boton(context):
    pretension_btn = context.web.find_by_id("btnEditsalary1")
    pretension_btn.click()

@when("postulante ingresa su pretension salarial {pretension}")
def postulante_ing_pretension(context, pretension):
    pretension_field = context.web.find_by_name("salary")
    pretension_field.send_keys(str(pretension))

@when("postulante hace click en boton Guardar")
def postulante_click_btn_guardar(context):
    guard_pret_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[3]/div[2]/form/div/div[2]/button[2]/span/span")
    guard_pret_btn.click()

@then("postulante visualiza tooltip de confirmacion pretension guardada {mensaje_pret}")
def postulante_visualiza_tooltip_pret(context, mensaje_pret):
    correct_pret_tooltip = context.web.find_by_class_name("g-notify_message")
    assert (mensaje_pret==correct_pret_tooltip.text)




