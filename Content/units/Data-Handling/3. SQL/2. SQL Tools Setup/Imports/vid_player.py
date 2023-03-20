from IPython import display
from base64 import b64encode

def play_vid(filepath):
    mp4 = open("filepath",'rb').read()
    mp4 = f"data:video/mp4;base64,{b64encode(mp4).decode()}"
    display.HTML(f"""<video width="60%" height="60%" controls
        src={mp4} >
    </video>""")