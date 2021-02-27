import requests
import pytube as pt
import sys

args = sys.argv
print("""
\t\tCOMMANDLINE SCRIPT TO DOWNLOAD YOUTUBE VIDEOS.
\t\tby www.github.com/nemo-xhan """)

if (len(args) > 1):
    url = args[0]
    print(args)
else:
    url = input("\tYOUTUBE VIDEO URL: ")

yt = pt.YouTube(url)
streams = yt.streams.all()
print(f"\tTITLE: {yt.title}")
print(f"\tAUTHOR: {yt.author}")
print(f"\tVIEWS: {yt.views}")

for i, stream in enumerate(streams):
    print(f"\t{i}. {stream.title} ({stream.resolution})")

get_choice = True

while get_choice:
    choice = int(input("\tSelect [ 0 - 1]: "))
    if choice < len(streams):
        print("\tDownloading Video...")
    
        try:
            with requests.get(streams[choice].url, stream=True) as r:
                with open(streams[choice].default_filename, "wb") as f:
                    for chunk in r.iter_content(512):
                        f.write(chunk)
            print("\tDownloading Completed")
            get_choice = False
        except Exception as e:
            print(str(e))
            exit(1)
    else:
        print("\tInvalid Choice")

