from behave import given, when, then
from behave.log_capture import capture

@given(u"postulante ingresa a Aptitus para registrar sus datos")
def postulante_ingresa_aptitus_r(context):
    context.web.open("https://dev.4a.aptitus.com/")

@when("postulante hace click para desplegar el menu")
def postulante_click_menu(context):
    menu = context.web.find_by_class_name("triangle")
    menu.click()

@when("postulante hace click en menu Mi Perfil")
def postulante_registra_datos(context):
    link = context.web.find_by_xpath ("//*[@title='Mi Perfil']")
    link.click()
    #opc = context.web.find_by_xpath("//*[@id='root']/div/header/div/div/div/div[2]/ul/li/ul/li[2]/a")
    #opc.click()

@when("postulante hace click en botón Editar Datos Personales")
def postulante_click_boton_editar(context):
    editar_btn = context.web.find_by_id("btnEditpersonalData1")
    editar_btn.click()


@when("postulante registra su nombre {nombre}")
def postulante_registra_nombre(context, nombre):
    nombre_field = context.web.find_by_id("names")
    nombre_field.clear()
    nombre_field.send_keys(str(nombre))

@when("postulante registra su apellido paterno {ape_pat}")
def postulante_registra_ape_pat(context, ape_pat):
    apepat_field = context.web.find_by_id("firstSurname")
    apepat_field.clear()
    apepat_field.send_keys(str(ape_pat))

@when("postulante registra su apellido materno {ape_mat}")
def postulante_registra_ape_mat(context, ape_mat):
    apemat_field = context.web.find_by_id("secondSurname")
    apemat_field.clear()
    apemat_field.send_keys(str(ape_mat))

@when("postulante registra su fecha de nacimiento {fech_nac}")
def postulante_registra_fech_nac(context, fech_nac):
    fech_nc_field = context.web.find_by_id("birthedAt")
    fech_nc_field.send_keys(str(fech_nac))

@when("postulante selecciona su genero {genero}")
def postulante_selecciona_genero(context, genero):
    genero_field = context.web.find_by_id("gender")
    genero_field.send_keys(str(genero))

@when("postulante selecciona su tipo de documento {tipo_doc}")
def postulante_selecciona_tipo_documento(context, tipo_doc):
    tip_doc_field = context.web.find_by_id("documentType")
    tip_doc_field.send_keys(str(tipo_doc))

@when("postulante registra su numero de documento {num_doc}")
def postulante_registra_numero_doc(context, num_doc):
    nro_doc_field = context.web.find_by_id("documentNumber")
    nro_doc_field.clear()
    nro_doc_field.send_keys(str(num_doc))

@when("postulante registra su celular {celular}")
def postulante_registra_celular(context, celular ):
    celular_field = context.web.find_by_id("cellphone")
    celular_field.clear()
    celular_field.send_keys(str(celular))

@when("postulante registra su telefono fijo {telef_fijo}")
def postulante_registra_telef(context, telef_fijo):
    telef_field = context.web.find_by_id("telephone")
    telef_field.clear()
    telef_field.send_keys(str(telef_fijo))


@when("postulante selecciona su estado civil {estado_civil}")
def postulante_selecciona_estado(context, estado_civil):
    est_field = context.web.find_by_id("civilStatus")
    est_field.send_keys(str(estado_civil))

@when("postulante ingresa su ubicacion {ubicacion}")
def postulante_selecciona_ubic(context, ubicacion):
    ubic_field = context.web.find_by_name("location")
    ubic_field.clear()
    ubic_field.send_keys(str(ubicacion))

@when("postulante espera que se deplieguen opciones")
def postulante_espera_segundos(context):
    context.web.time_sleep()

@when("postulante selecciona la primera opción segun su ubicacion")
def postulante_seleciona_primera_opcion(context):
    prim_opc = context.web.find_by_id("react-autowhatever-1--item-0")
    prim_opc.click()

@when("postulante registra su direccion {direccion}")
def postulante_registra_descrip(context, direccion):
    dire_field = context.web.find_by_id("address")
    dire_field.clear()
    dire_field.send_keys(str(direccion))

@when("postulante hace click en botón Guardar")
def postulante_click_btn_guardar(context):
    guardar_btn = context.web.find_by_xpath("//*[@id='body']/div[2]/div[2]/div[2]/form/div/div[9]/button[2]")
    guardar_btn.click()

@then("postulante visualiza tooltip con mensaje {mensaje}")
def postulante_visualiza_tooltip(context, mensaje):
    correcto_tooltip = context.web.find_by_class_name("g-notify_message")
    assert (mensaje==correcto_tooltip.text)









  












   