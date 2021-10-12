import requests
import wget, urllib, os, glob

if os.path.exists("0.8.2"):
    for file in glob.glob(os.path.join("0.8.2", "pyunity*.whl")):
        os.remove(file)
else:
    os.mkdir("0.8.2")

apiUrl = "https://ci.appveyor.com/api"

project = requests.get(f"{apiUrl}/projects/pyunity/pyunity")
for job in project.json()["build"]["jobs"]:
    jobId = job["jobId"]
    artifacts = requests.get(f"{apiUrl}/buildjobs/{jobId}/artifacts")

    for artifact in artifacts.json():
        file = artifact["fileName"]
        try:
            wget.download(f"{apiUrl}/buildjobs/{jobId}/artifacts/{file}",
                "0.8.2/" + os.path.basename(file))
        except urllib.error.HTTPError:
            print(f"Couldnt download {os.path.basename(file)}", end="")
        print()

for file in glob.glob("0.8.2/*linux*"):
    os.rename(file, file.replace("linux", "manylinux1"))
