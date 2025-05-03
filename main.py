import os
import requests
from fastapi import FastAPI
from solvers import browsehomework, sendrequest, getrequests
from students import addhomework, gethomework, deletehomework

# --- CA Certificate Download (Run once on startup) ---
def download_ca_cert():
    cert_url = 'https://cockroachlabs.cloud/clusters/41c32845-f06a-4f55-a5aa-0e8842e1a79a/cert'
    cert_dir = os.path.expanduser('~/.postgresql')
    cert_path = os.path.join(cert_dir, 'root.crt')

    os.makedirs(cert_dir, exist_ok=True)

    if not os.path.exists(cert_path):  
        response = requests.get(cert_url)
        if response.status_code == 200:
            with open(cert_path, 'wb') as f:
                f.write(response.content)
            print(f"Certificate downloaded and saved to {cert_path}")
        else:
            print(f"Failed to download certificate. HTTP status code: {response.status_code}")
    else:
        print(f"Certificate already exists at {cert_path}")

# Run the cert download before app starts
download_ca_cert()

# --- FastAPI App Setup ---
app = FastAPI()

# Student-related routes
app.include_router(addhomework.router, prefix="/students/addhomework", tags=["students"])
app.include_router(gethomework.router, prefix="/students/gethomework", tags=["students"])
app.include_router(deletehomework.router, prefix="/students/deletehomework", tags=["students"])

# Solver-related routes
app.include_router(browsehomework.router, prefix="/solvers/browsehomework", tags=["solvers"])
app.include_router(sendrequest.router, prefix="/solvers/sendrequest", tags=["solvers"])
app.include_router(getrequests.router, prefix="/solvers/getrequests", tags=["solvers"])
