# This is generator great for when you need sample data
#
# You need to use pip3 to install both "pillow" and "reportlab"
#
# You also need to have a folder called "files" in the same directory as this file
#
# View readme for full instructions
#
# This implementation currently uses a process each for generating text, images, and pdf
# Future improvements could include better multiprocessing by using a Pool for example
# Another addition could be more filetypes
#
# For tweaking of the files you may edit the important variables below the imports
# There are a few more things you can edit manually in the code marked with ADJUSTABLE

import random
import string
from PIL import Image
from reportlab.pdfgen import canvas
import multiprocessing
import os

# Settings for text file generation

# Min size for the .txt filenames
text_filename_minsize = 10
# Max size for the .txt filenames
text_filename_maxsize = 30

# Min amount of characters generated in .txt files
text_min_characters = 500000
# Max amount of characters generated in .txt files
text_max_characters = 1000000


# Settings for image file generation

# Min size for the .jpg filenames
jpg_filename_minsize = 10
# Max size for the .jpg filenames
jpg_filename_maxsize = 30

# Amount of horizontal pixels (X)
jpg_horizontal_pixels = 1750
# Amount of vertical pixels (Y)
jpg_vertical_pixels = 1750


# Settings for pdf file generation

# Min size for the .txt filenames
pdf_filename_minsize = 10
# Max size for the .txt filenames
pdf_filename_maxsize = 30

# Min amount of lines in .pdf files
pdf_min_lines = 250
# Max amount of lines in .pdf files
pdf_max_lines = 500

# Min amount of characters per line in .pdf files
pdf_min_characters = 20000
# Max amount of characters per line in .pdf files
pdf_max_characters = 40000


# Function to generate .txt files, "amount" being desired amount of files
def generateTXT(amount):
    # Lets you know the function is working, unless you aren't generating any .txt files
    if not (amount < 1):
        print()
        print("Beginning .txt Generation")
        print()

    # Generation occurs in this for loop, "amount" being desired amount of .txt files
    for i in range(amount):

        # Random filename will be stored in this variable
        name = ""

        # Generates the filename
        for j in range(random.randint(text_filename_minsize, text_filename_maxsize)):
            name += random.choice(string.ascii_letters + string.digits)

        # Creates the file
        file = open(("files/" + name + ".txt"), "w+")

        # Writes the random text to the file
        for j in range(text_min_characters, text_max_characters):
            file.write(random.choice(string.ascii_letters + string.digits + ' '))

            # ADJUSTABLE - Uses random probability to add newlines
            if random.randint(0, 100) < 1:
                file.write("\n")

        # Prints message to let you know of the progress in realtime
        print("Created txt file " + str(i + 1) + "/" + str(amount))


# Function to generate .img files, "amount" being desired amount of files
def generateIMG(amount):
    # Lets you know the function is working, unless you aren't generating any .jpg files
    if not (amount < 1):
        print()
        print("Beginning .jpg Generation")
        print()

    # Generation occurs in this for loop, "amount" being desired amount of .jpg files
    for i in range(amount):

        # Random filename will be stored in this variable
        name = ""

        # Generates the filename
        for j in range(random.randint(jpg_filename_minsize, jpg_filename_maxsize)):
            name += random.choice(string.ascii_letters + string.digits)

        # Creates Image object
        image = Image.new("RGB", (jpg_horizontal_pixels, jpg_vertical_pixels), (255, 255, 255))
        pixel = image.load()

        # This for loop adds the randomized pixels to the image
        for j in range(jpg_horizontal_pixels):
            for k in range(jpg_vertical_pixels):
                red = random.randrange(0, 255)
                blue = random.randrange(0, 255)
                green = random.randrange(0, 255)
                pixel[j, k] = (red, blue, green)

        # Saves image file
        image.save("files/" + name + ".jpg")

        # Prints message to let you know of the progress in realtime
        print("Created .jpg file " + str(i + 1) + "/" + str(amount))


# Function to generate .pdf files, "amount" being desired amount of files
def generatePDF(amount):
    # Lets you know the function is working, unless you aren't generating any .pdf files
    if not (amount < 1):
        print()
        print("Beginning .pdf Generation")
        print()

    # Generation occurs in this for loop, "amount" being desired amount of .pdf files
    for i in range(amount):

        # Random filename will be stored in this variable
        name = ""

        # Generates the filename
        for j in range(random.randint(pdf_filename_minsize, pdf_filename_maxsize)):
            name += random.choice(string.ascii_letters + string.digits)

        # Creates Canvas object/file used for the pdf generation
        pdf = canvas.Canvas("files/" + name + ".pdf")

        # ADJUSTABLE - Can change this to get a specific color if you'd like
        pdf.setFillColorRGB(random.random(), random.random(), random.random())

        # ADJUSTABLE - Can change font and font size
        pdf.setFont("Helvetica", 10)

        # Generates the text line by line
        for j in range(random.randint(pdf_min_lines, pdf_max_lines)):
            temp = ""
            for k in range(random.randint(pdf_min_characters, pdf_max_characters)):
                temp += random.choice(string.ascii_letters + string.digits + " ")
            pdf.drawString(0, random.randint(0, 1500), temp)

        # Saves the pdf
        pdf.save()

        # Prints message to let you know of the progress in realtime
        print("Created pdf file " + str(i + 1) + "/" + str(amount))


if __name__ == "__main__":
    # Check for files output directory
    if not os.path.exists("files"):
        os.makedirs("files")

    # User input for desired amount of files
    amount_txt = int(input("Enter amount of txt files: "))
    amount_jpg = int(input("Enter amount of jpg files: "))
    amount_pdf = int(input("Enter amount of pdf files: "))

    # Creates a separate process for each function to help speed up generation and bypass the GIL
    text_process = multiprocessing.Process(target=generateTXT, args=(amount_txt, ))
    images_process = multiprocessing.Process(target=generateIMG, args=(amount_jpg, ))
    pdf_process = multiprocessing.Process(target=generatePDF, args=(amount_pdf, ))

    # Starts the processes
    text_process.start()
    images_process.start()
    pdf_process.start()

    # Joins the processes
    text_process.join()
    images_process.join()
    pdf_process.join()

    # Success!
    print()
    print("Done")
