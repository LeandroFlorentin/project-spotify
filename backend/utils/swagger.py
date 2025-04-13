from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Seguridad para el Swagger UI
security = HTTPBearer()


# Dependencia que no valida nada, pero hace que Swagger lo muestre
def show_bearer_in_swagger(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    return
