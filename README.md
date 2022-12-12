# silence

Generation audio frames and saving **silent** mp3 files

Could be used alone but was designed to use with [gtts](https://pypi.org/project/gTTS/)
to make a pause between sounds

The class constructor has only one argument - the silence time in seconds 
(a float is available)   

### Usage Example

#### create a 10-second silent file

    >>> from silence import *
    >>> Silence(10).save('silence.mp3')

#### making 3-second mp3 

    >>> from silence import *
    >>> with open('silence.mp3', 'wb') as f:
    >>>     f.write(Silence(3).get_frames())

#### usage with gtts

    >>> from gtts import gTTS
    >>> from silence import *

    >>> with open('hello.mp3', 'wb') as f:
    >>>     gTTS('hello', lang='en').write_to_fp(f)
    >>>     Silence(5).write_to_fp(f)
    >>>     gTTS('bonjour', lang='fr').write_to_fp(f)

