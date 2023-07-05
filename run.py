import subprocess
import re

def ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '4', host])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping to {host} failed: {e}')

def traceroute(host):
    try:
        output = subprocess.check_output(['traceroute', host])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        raise Exception(f'Traceroute to {host} failed: {e}')

def validate_domain(domain):
    pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2,})$"
    return re.match(pattern, domain) is not None

def run():
    # Get the user input
    domain = input("Digite o domínio: ")
    
    # Validate the domain input
    if validate_domain(domain):
        # Call function with error handling
        try:
            ping(domain)
        except Exception as e:
            print(f'Ping to {domain} failed: {e}')

        try:
            traceroute(domain)
        except Exception as e:
            print(f'Traceroute to {domain} failed: {e}')
    else:
        print("Domínio inválido. Entre um domínio válido.")

if __name__ == '__main__':
    run()

