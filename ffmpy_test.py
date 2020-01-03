import ffmpy

ff = ffmpy.FFmpeg(
     inputs={'download/v_5c80f6ac3e28a_7BumyNgu/video.m3u8': ['-protocol_whitelist', 'crypto,file,http,https,tcp,tls']},
     outputs={'download/ffmpy_test.mp4': None}
)
print(ff.cmd)
ff.run()
