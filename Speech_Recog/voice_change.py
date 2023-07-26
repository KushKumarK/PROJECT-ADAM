import sys
import textwrap
import sounddevice as sd
sys.path.append("Speech_Recog/Real_Time_Voice_Cloning")
from IPython.utils import io
from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
from pathlib import Path
import numpy as np
import librosa

class Voice_Change:
    def __init__(self, path):
        self.path = path
        encoder_weights = Path("Speech_Recog/Real_Time_Voice_Cloning/encoder/saved_models/pretrained.pt")
        vocoder_weights = Path("Speech_Recog/Real_Time_Voice_Cloning/vocoder/saved_models/pretrained/pretrained.pt")
        syn_dir = Path("Speech_Recog/Real_Time_Voice_Cloning/synthesizer/saved_models/pretrained/pretrained.pt")
        encoder.load_model(encoder_weights)
        self.synthesizer = Synthesizer(syn_dir)
        vocoder.load_model(vocoder_weights)
        in_fpath = Path(self.path)
        reprocessed_wav = encoder.preprocess_wav(in_fpath)
        original_wav, sampling_rate = librosa.load(in_fpath)
        preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
        self.embed = encoder.embed_utterance(preprocessed_wav)

    def voice_speak(self, text):
        with io.capture_output() as captured:
            specs = self.synthesizer.synthesize_spectrograms([text], [self.embed])
        generated_wav = vocoder.infer_waveform(specs[0])
        generated_wav = np.pad(generated_wav, (0, self.synthesizer.sample_rate), mode="constant")
        voice_generated = [generated_wav, self.synthesizer.sample_rate]
        print(voice_generated)
        return voice_generated