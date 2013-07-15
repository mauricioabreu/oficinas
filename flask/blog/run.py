# -*- coding: utf-8 -*- 

from app import app

# debug ativado tem como principal fator mostrar o stacktrace quando algum erro é levantado.
# não use debug ativado em modo de produção.
app.run(debug=True)
