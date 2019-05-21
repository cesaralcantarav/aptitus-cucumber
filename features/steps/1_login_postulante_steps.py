from behave import given, when, then
from behave.log_capture import capture


@given("postulante ingresa a Aptitus")
def postulante_ingresa_aptitus(context):
    context.web.open("https://pre4c.aptitus.com/")

@when("postulante hace click en link Ingresa")
def postulante_click_link_ingresa(context):
    link = context.web.find_by_xpath("/html/body/header/section[2]/div[1]/div/ul/li[4]/a")
    link.click()

@when("postulante ingresa email {email}")
def postulante_ingresa_email(context, email):
    email_field = context.web.find_by_id("txtUser")
    email_field.send_keys(str(email))

@when("postulante ingresa constrasenia {contrasenia}")
def postulante_ingresa_contrasenia(context, contrasenia):
    password_filed = context.web.find_by_id("txtPasswordLogin")
    password_filed.send_keys(str(contrasenia))

@when("postulante hace click en boton Ingresar")
def postulante_click_boton_ingresa(context):
    ingresa_btn = context.web.find_by_xpath("//*[@id='frmUserLogIn']/button")
    ingresa_btn.click()
    #//*[@id="frmUserLogIn"]/button
    #/html/body/div[12]/div/div/div/div/div/div[3]/form/button

@when("postulante espera unos segundos")
def postulante_espera_segundos(context):
    context.web.time_sleep()

@then("postulante visualiza la vista Perfil {vista}")
def postulante_visualiza_perfil(context, vista):
    perfil_page = context.web.find_by_xpath("/html/body/div/div/div[2]/div/section/div[1]/div/div/div[2]/a[1]/button")
    assert (vista==perfil_page.text)




 

