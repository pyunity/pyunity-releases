import requests
import wget, urllib, os, glob

if os.path.exists("post-0.4/0.8.4"):
    for file in glob.glob(os.path.join("post-0.4/0.8.4", "pyunity*.whl")):
        os.remove(file)
else:
    os.mkdir("post-0.4/0.8.4")

apiUrl = "https://ci.appveyor.com/api"

project = requests.get(f"{apiUrl}/projects/pyunity/pyunity")
for job in project.json()["build"]["jobs"]:
    jobId = job["jobId"]
    artifacts = requests.get(f"{apiUrl}/buildjobs/{jobId}/artifacts")

    for artifact in artifacts.json():
        file = artifact["fileName"]
        try:
            wget.download(f"{apiUrl}/buildjobs/{jobId}/artifacts/{file}",
                "post-0.4/0.8.4/" + os.path.basename(file))
        except urllib.error.HTTPError:
            print(f"Couldn't download {os.path.basename(file)}", end="")
        print()

for file in glob.glob("post-0.4/0.8.4/*linux*"):
    os.rename(file, file.replace("linux", "manylinux1"))
