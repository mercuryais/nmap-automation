import subprocess

def data(script):
    result = subprocess.run(f"{script} -oX -", capture_output=True, text=True)
    print(script + ' ' + "-oX")
    with open('data.xml', 'a') as dataFile:
        dataFile.write(result.stdout)