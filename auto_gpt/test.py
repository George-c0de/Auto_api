import subprocess

proc = subprocess.Popen(['python', '-m', 'autogpt'], stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if not line:
        break
    # декодируем байты в строку
    decoded_line = line.decode('utf-8')
    # the real code does filtering here
    print("test:", decoded_line.rstrip())