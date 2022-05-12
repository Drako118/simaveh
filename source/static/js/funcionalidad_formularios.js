function mostrartipopersona(id) {
    if (id == "persona_natural") {
        $("#persona_natural").show();
        $("#persona_juridica").hide();
    }

    if (id == "persona_juridica") {
        $("#persona_juridica").show();
        $("#persona_natural").hide();    
    }

}

