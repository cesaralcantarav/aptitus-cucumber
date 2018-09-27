
from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante ingresa a Aptitus para registrarse")
def postulante_ingresa_aptitus_r(context):
    context.web.open("https://dev.4a.aptitus.com/")

@when(u"postulante hace click en link Registrate")
def postulante_click_link_registrate(context):
    link = context.web.find_by_xpath("/html/body/header/section[2]/div[1]/div/ul/li[3]/a")
    link.click()

@when(u"postulante ingresa nombre {nombre}")
def postulante_ingresa_nombre(context, nombre):
    nombre_field = context.web.find_by_id("txtName")
    nombre_field.send_keys(str(nombre))

@when(u"postulante ingresa apellido paterno {ape_pat}")
def postulante_ingresa_apellido_paterno(context, ape_pat):
    apellidop_field = context.web.find_by_id("txtFirstLastName")
    apellidop_field.send_keys(str(ape_pat))

@when(u"postulante ingresa apellido materno {ape_mat}")
def postulante_ingresa_apellido_materno(context, ape_mat):
    apellidom_field = context.web.find_by_id("txtSecondLastName")
    apellidom_field.send_keys(str(ape_mat))


@when (u"postulante ingresa e-mail para registrarse {email}")
def postulante_ingresa_email(context, email):
    email_field = context.web.find_by_id("txtEmail")
    email_field.send_keys(str(email))
   

@when(u"postulante ingresa contrasenia para registrarse {contrasenia}")
def postulante_ingresa_contrasenia_r(context, contrasenia):
    contrasenia_field_r = context.web.find_by_id("pswd")
    contrasenia_field_r.send_keys(str(contrasenia))

@when(u"postulante ingresa trabajo ideal {trabajo_ideal}")
def postulante_ingresa_trabajo_ideal(context, trabajo_ideal):
    trab_ideal_field = context.web.find_by_id("txtJob")
    trab_ideal_field.send_keys(str(trabajo_ideal))

@when(u"postulante espera")
def postulante_espera(context):
    context.web.time_sleep()  

@when(u"postulante selecciona opcion del autocomplete")
def postulante_selecciona_opcion(context):
    opc = context.web.find_by_xpath("//*[@id='ui-id-2']/li[1]")
    opc.click()

@when(u"postulante espera2")
def postulante_espera(context):
    context.web.time_sleep() 

@when(u"postulante selecciona lugar ideal")
def postulante_selecciona_lugar_ideal(context):
    lug_ideal_select = context.web.find_by_xpath("//*[@id='selLocation']/option[2]")
    lug_ideal_select.click()

@when(u"postulante hace click en boton Crear cuenta")
def postulante_click_boton_crearcuenta(context):
    crea_cuenta_btn = context.web.find_by_xpath("//*[@id='frmUserRegistrationFast']/div[4]/div/button")
    crea_cuenta_btn.click()

@then(u"postulante visualiza la vista Mi Perfil {vista}")
def postulante_visualiza_perfil(context, vista):
    perfil_page = context.web.find_by_xpath("/html/body/div/div/div[2]/div/section/div[1]/div/div/div[2]/a[1]/button")
    assert (vista==perfil_page.text)


 











