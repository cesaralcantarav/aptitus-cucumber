from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante se encuentra en opcion Experiencia")
def postulante_selecciona_opc_experiencia(context):
    context.web.time_sleep()
    experiencia_opc = context.web.find_by_xpath("//*[@id='body']/div[1]/div/div/div[1]/a[4]")
    experiencia_opc.click()

@when(u"postulante hace click en boton Agregar Experiencia")
def postulante_click_boton_add_exp(context):
    add_exp_btn = context.web.find_by_id("experiencesAddBtn")
    add_exp_btn.click()

@when(u"postulante ingresa la empresa {empresa}")
def postulante_ingresa_empresa(context, empresa):
    company_field = context.web.find_by_id("companyexperiences")
    company_field.send_keys(str(empresa))

@when(u"postulante ingresa la industria {industria}")
def postulante_ingr_industria(context, industria):
    industry_field = context.web.find_by_id("industryexperiences")
    industry_field.send_keys(str(industria))

@when(u"postulante ingresa el puesto {puesto}")
def postulante_ingresa_puesto(context, puesto):
    job_field = context.web.find_by_name("job")
    job_field.send_keys(str(puesto))
    context.web.time_sleep()

@when(u"postulante selecciona el nivel de puesto {nivel_puesto}")
def postulante_ingresa_nivpuesto(context, nivel_puesto):
    level_field = context.web.find_by_id("levelIdexperiences")
    level_field.send_keys(str(nivel_puesto))

@when(u"postulante selecciona el area {area}")
def postulante_selecciona_area(context,area):
    area_field = context.web.find_by_id("areaIdexperiences")
    area_field.send_keys(str(area))

@when(u"postulante selecciona un mes inicio de experiencia {mes_inicio}")
def postulante_mes_inicio(context, mes_inicio):
    start_month_exp_field = context.web.find_by_id("startMonthexperiences")
    start_month_exp_field.send_keys(str(mes_inicio))

@when(u"postulante ingresa un año inicio de experiencia {anio_inicio}")
def postulante_ingresa_anioinicio(context, anio_inicio):
    start_year_exp_field = context.web.find_by_id("startYearexperiences")
    start_year_exp_field.send_keys(str(anio_inicio))

@when(u"postulante selecciona un mes fin de experiencia {mes_fin}")
def postulante_mes_fin(context, mes_fin):
    end_month_exp_field = context.web.find_by_id("endMonthexperiences")
    end_month_exp_field.send_keys(str(mes_fin))

@when(u"postulante ingresa un año fin de experiencia {anio_fin}")
def postulante_anio_fin(context, anio_fin):
    end_year_exp_field = context.web.find_by_id("endYearexperiences")
    end_year_exp_field.send_keys(str(anio_fin))

@when(u"postulante ingresa una descripción {descripcion}")
def postulante_ingresa_desc_exp(context, descripcion):
    description_field = context.web.find_by_id("descriptionexperiences")
    description_field.send_keys(str(descripcion))

@when(u"postulante hace click en boton Guardar Experiencia")
def postulante_click_btn_addexp(context):
    addexp_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[5]/div[1]/div/form/div/div[7]/button[2]/span")   
    addexp_btn.click()

@then(u"postulante visualiza tooltip de confirmacion de Experiencia Guardada {mensaje}")
def postulante_visualiza_toolt_exp(context, mensaje):
    correcto_tooltip = context.web.find_by_class_name("g-notify_message")
    assert (mensaje == correcto_tooltip.text)





















    




