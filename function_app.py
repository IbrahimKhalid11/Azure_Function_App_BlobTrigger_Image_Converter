import os
import azure.functions as func
import logging
import io
from azure.storage.blob import BlobServiceClient
from PIL import Image

TARGET_SIZE = (800, 800) 

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="raw/{name}",
                  connection="AzureWebJobsStorage")
@app.blob_output(arg_name="outputblob", path="processed/{name}.png",
                 connection="AzureWebJobsStorage")
def convert_image_to_png(myblob: func.InputStream, outputblob: func.Out[bytes]):
    try:
        logging.info(f"Processing file: {myblob.name} (Size: {myblob.length} bytes)")

        filename = os.path.basename(myblob.name).rsplit('.', 1)[0]
        new_filename = f"{filename}.png"
        
        image = Image.open(io.BytesIO(myblob.read()))

        image.thumbnail(TARGET_SIZE)

        png_buffer = io.BytesIO()
        image.save(png_buffer, format="PNG")
        png_buffer.seek(0)
        
        outputblob.set(png_buffer.getvalue())

        logging.info(f"File successfully converted and resized to PNG as '{new_filename}' in 'processed/' container.")
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
