import subprocess

packages = [
    "absl-py==1.4.0",
    "alabaster==0.7.13",
    "altgraph==0.17.3",
    "amqp==5.1.1",
    "aniso8601==9.0.1",
    "annotated-types==0.5.0",
    "ansi2html==1.8.0",
    "ansible==7.4.0",
    "ansible-core==2.14.4",
    "anyio==3.6.2",
    "appnope==0.1.3",
    "argon2-cffi==21.3.0",
    "argon2-cffi-bindings==21.2.0",
    "arrow==1.2.3",
    "asgiref==3.7.2",
    # Add the rest of your packages here
]

for package in packages:
    subprocess.run(["pip", "install", package])
