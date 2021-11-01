from IPython.core.display import display
from IPython.display import Audio
from IPython.utils import io
from Real_Time_Voice_Cloning.synthesizer.inference import Synthesizer
from Real_Time_Voice_Cloning.encoder import inference as encoder
from Real_Time_Voice_Cloning.vocoder import inference as vocoder
from pathlib import Path
import numpy as np
import librosa

encoder_weights = Path("Real_Time_Voice_Cloning/encoder/saved_models/pretrained.pt")
vocoder_weights = Path("Real_Time_Voice_Cloning/vocoder/saved_models/pretrained/pretrained.pt")
syn_dir = Path("synthesizer/saved_models/logs-pretrained/taco_pretrained")
encoder.load_model(encoder_weights)
synthesizer = Synthesizer(syn_dir)
vocoder.load_model(vocoder_weights)
text = "Subscribe to the channel"
in_fpath = Path("Resources/audio_files_harvard.wav")
reprocessed_wav = encoder.preprocess_wav(in_fpath)
original_wav, sampling_rate = librosa.load(in_fpath)
preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
embed = encoder.embed_utterance(preprocessed_wav)
with io.capture_output() as captured:
    specs = synthesizer.synthesize_spectrograms([text], [embed])
generated_wav = vocoder.infer_waveform(specs[0])
generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")
display(Audio(generated_wav, rate=synthesizer.sample_rate))
