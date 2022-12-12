class Silence:
    audio_frame = b'\xff\xf3D\xc4\x00\x00\x00\x03H\x01@\x00\x00\xffE6&/\xfb\x17\xff~\xe9]\xfaO\xf8n_\x03\\\xe2\x0e' \
                  b'\xeaa\xfc\xe8\xcc(X0\x7f\xcf\x9c\x860/\xdf\xfa\x9e\x9f\xdf\xf3Vp\x7f\x0f\x8d\xeb8#\x06\xff\xd3' \
                  b'\x972\x1fC\x0f\x04\x7f\xc3\xe7:1cBc\x04\xc3D\x95\x05\xc1X\x80\xd2X\xf2\xc8\xc4\x02\xd0\xeeQ\xc4'

    def __init__(self, seconds: float):
        self.seconds = seconds

    def get_frames(self):
        return self.audio_frame * int(self.seconds / .024)

    def save(self, filename: str):
        with open(filename, 'wb') as fp:
            self.write_to_fp(fp)

    def write_to_fp(self, fp):
        times = int(self.seconds / .024)
        for _ in range(times):
            fp.write(self.audio_frame)
