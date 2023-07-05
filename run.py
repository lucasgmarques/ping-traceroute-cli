import subprocess
import re

def ping(host, timeout=None):
    try:
        output = subprocess.check_output(['ping', '-c', '4', '-W', str(timeout), host])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        raise Exception(f'Ping to {host} failed: {e}')

def traceroute(host, timeout=None):
    try:
        output = subprocess.check_output(['traceroute', '-w', str(timeout), host])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        raise Exception(f'Traceroute to {host} failed: {e}')

def validate_domain(domain):
    pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2,})$"
    return re.match(pattern, domain) is not None

def run():
    # Get the user input
    domains = input("Digite o domínio (separar por vírgula em caso de mais de um): ").split(',')
    
    for domain in domains:
        domain = domain.strip()
        # Validate the domain input
        if validate_domain(domain):
            # Call function with error handling and timeout of 5 seconds
            try:
                ping(domain, timeout=5)
            except Exception as e:
                print(f'Ping to {domain} failed: {e}')

            try:
                traceroute(domain, timeout=5)
            except Exception as e:
                print(f'Traceroute to {domain} failed: {e}')
        else:
            print("Domínio inválido. Entre um domínio válido.")

if __name__ == '__main__':
    run()

