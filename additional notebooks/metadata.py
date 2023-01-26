##------------------------------------------------
# Function get_metadata( imagefile )
# Receives a name of a file (as string) containing an image
# and opens it with PIL
# Reads the exif metadata and returns a dictionary containing
# the tags as key and the corresponding metadata as value
# Uses a block try-except to avoid errors in cases when the metadata
# cannot be converted to string directly.
##------------------------------------------------
# To do: Implement a decoding function for metadata that cannot be 
# converted to string, i.e. GPS coordinates.
##------------------------------------------------
# Online resources:
# https://www.thepythoncode.com/article/extracting-image-metadata-in-python
# https://www.codedrome.com/reading-exif-data-with-python-and-pillow/

##------------------------------------------------
# get_metadata - receives a string parameter and returns a dictionary
def get_metadata( imagefile ):
    
    # Import needed modules
    from PIL import Image
    from PIL.ExifTags import TAGS 

    # Opens the file and extracts metadata
    with Image.open( imagefile ) as var_image:

        metadata = {} # Empty dictionary to store the metadata

        exifdata = var_image._getexif() # Get metadata from the image

        # Iterate over the data in the image to decode each value
        # from bytes into a human-readable string
        for tag_id in exifdata: 
            tag = TAGS.get(tag_id, tag_id) 
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                # try-except block: if a decoding error occurs, it
                # sets the metadata value to "ERROR AT DECODING"
                # Here further development is needed
                try:
                       data = data.decode('utf-8') 
                except:
                       data = "ERROR AT DECODING"

            # In each iteration, add the tag and data to the dictionary
            metadata[tag] = data

    # return dictionary and end the function
    return metadata


