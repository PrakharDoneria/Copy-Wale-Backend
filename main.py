from fastapi import FastAPI
from solvers import browsehomework, sendrequest, getrequests
from students import addhomework, gethomework, deletehomework

app = FastAPI()

# Include student-related routes
app.include_router(addhomework.router, prefix="/students/addhomework", tags=["students"])
app.include_router(gethomework.router, prefix="/students/gethomework", tags=["students"])
app.include_router(deletehomework.router, prefix="/students/deletehomework", tags=["students"])

# Include solver-related routes
app.include_router(browsehomework.router, prefix="/solvers/browsehomework", tags=["solvers"])
app.include_router(sendrequest.router, prefix="/solvers/sendrequest", tags=["solvers"])
app.include_router(getrequests.router, prefix="/solvers/getrequests", tags=["solvers"])
