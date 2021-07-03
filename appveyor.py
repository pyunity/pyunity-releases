import requests
import wget, urllib, os, glob

if os.path.exists("0.7.0"):
    for file in glob.glob(os.path.join("0.7.0", "pyunity*.whl")):
        os.remove(file)
else:
    os.mkdir("0.7.0")

apiUrl = "https://ci.appveyor.com/api"

project = requests.get(f"{apiUrl}/projects/rayzchen/pyunity")
jobId = project.json()["build"]["jobs"][0]["jobId"]
artifacts = requests.get(f"{apiUrl}/buildjobs/{jobId}/artifacts")

for artifact in artifacts.json():
    file = artifact["fileName"]
    try:
        wget.download(f"{apiUrl}/buildjobs/{jobId}/artifacts/{file}",
            "0.7.0/" + os.path.basename(file))
    except urllib.error.HTTPError:
        print(f"Couldnt download {os.path.basename(file)}", end="")
    print()