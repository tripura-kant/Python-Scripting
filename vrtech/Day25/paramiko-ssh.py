import sys

try:
    import paramiko
except Exception as e:
    print(f'Exception is: {e}')
    sys.exit()

print("Okay")

remote_server = '10.224.216.191'
username = 'tripura.kant'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Use SSH agent (Teleport cert) to authenticate
    client.connect(
        hostname=remote_server,
        username=username,
        allow_agent=True,
        look_for_keys=True,
        timeout=10
    )

    stdin, stdout, stderr = client.exec_command("sudo pwd")
    print("Output:")
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print("Error output:")
        print(err)

except Exception as e:
    print(f'❌ Connection error: {e}')
finally:
    client.close()
