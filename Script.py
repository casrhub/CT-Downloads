import requests
import subprocess

# Dictionary containing the URLs for each application
app_urls = {
    'Google Chrome': 'https://dl.google.com/chrome/install/latest/chrome_installer.exe',
    'AnyDesk': 'https://download.anydesk.com/AnyDesk.exe',
    'Skype': 'https://go.skype.com/windows.desktop.download',
    'WinRAR': 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-601.exe',
    'Adobe Reader': 'https://get.adobe.com/reader/otherversions/'
}

# Download and install each application
for app_name, app_url in app_urls.items():
    print(f"Downloading {app_name}...")
    response = requests.get(app_url)
    file_name = app_url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)

    print(f"Installing {app_name}...")
    subprocess.run([file_name], check=True)

    print(f"{app_name} installed successfully.")

    # Delete the installer file
    subprocess.run(['del', file_name], shell=True)

print("All applications installed.")