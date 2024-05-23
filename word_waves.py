from PIL import Image
import pytesseract
import pyttsx3
import wave

# Function to extract text from image
def extract_text_from_image(image_path):
    # Open the image with Pillow
    image = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    
    return text

# Function to convert text to speech and save as a wave file
def text_to_speech(text, output_file):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties for the speech output (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    
    # Convert text to speech and save to file
    engine.save_to_file(text, output_file)
    
    # Run the speech synthesis
    engine.runAndWait()

# Function to get audio file information
def get_audio_info(output_file):
    # Get the audio data in the form of a wave file object
    with wave.open(output_file, 'rb') as wav_file:
        frames = wav_file.getnframes()
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        duration = frames / float(frame_rate)
        
        print("Audio information:")
        print(f"Number of frames: {frames}")
        print(f"Number of channels: {channels}")
        print(f"Sample width: {sample_width}")
        print(f"Frame rate: {frame_rate}")
        print(f"Duration: {duration} seconds")

# Main workflow
if __name__ == "__main__":
    # Define the path to your image
    image_path = 'C:/Users/nicol/OneDrive/Billeder/TheIrishman.jpg'
    
    # Define the output audio file name
    output_file = 'output.wav'
    
    # Extract text from image
    extracted_text = extract_text_from_image(image_path)
    
    # Print extracted text (optional)
    print("Extracted Text:")
    print(extracted_text)
    
    # Convert extracted text to speech
    text_to_speech(extracted_text, output_file)
    
    # Get and print audio file information
    get_audio_info(output_file)




#text to waves

# Initialize the pyttsx3 engine
#engine = pyttsx3.init()

# Set properties for the speech output (optional)
#engine.setProperty('rate', 150)  # Speed of speech
#engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Set the output file name
#output_file = 'output.wav'

# Convert text to speech
#text = "Test for text to waves"
#engine.save_to_file(text, output_file)

# Run the speech synthesis
#engine.runAndWait()

# Optional: Get the audio data in the form of a wave file object
#with wave.open(output_file, 'rb') as wav_file:
    # You can now manipulate the wave file object as needed
    # For example, you can get information about the audio file:
    #frames = wav_file.getnframes()
    #channels = wav_file.getnchannels()
    #sample_width = wav_file.getsampwidth()
    #frame_rate = wav_file.getframerate()
    #duration = frames / float(frame_rate)

    #print("Audio information:")
    #print(f"Number of frames: {frames}")
    #print(f"Number of channels: {channels}")
    #print(f"Sample width: {sample_width}")
    #print(f"Frame rate: {frame_rate}")
    #print(f"Duration: {duration} seconds")