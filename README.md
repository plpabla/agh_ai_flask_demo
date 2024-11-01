# Endpoints

# `GET /`

Hello world message

# `GET /calculate`

Calculations with query params:

    operation={sum|diff|mul|div}
    arg1=number
    arg2=number

Example:

    /calculate?operation=sum&arg1=12&arg2=23
