#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# Create a file and write content
file = open('newFile.txt', 'w')
content = "Hello PLP Team!!!\n My name is Sodeeq Opeyemi Bello from Nigeria. I am using this opportunity to say " \
"a big THANK YOU to Power Learning Project for this exciting opportunity. I am excited to be a part of this community and " \
"I look forward to learning from all of you and sharing my knowledge with you as well.\n"
file.write(content)
file.close()

# Read file content
file = open('newFile.txt', 'r')
data = file.read()
print(data)
file.close()

# Append (modify) the file
file = open('newFile.txt', 'a')
file.write("About Me.\n I'm an aspiring software developer and data analyst with a solid " \
"background in Physics and Electronics, aiming to apply this knowledge in the healthcare sector, " \
"specifically in medical physics, such as medical imaging, diagnostics, and AI in medicine. " \
"Currently participating in the Power Learn Project's Software Development Scholarship, where I am gaining " \
"practical experience in Python, HTML, CSS, JavaScript, and Database Management. I am enthusiastic about " \
"leveraging digital tools to address real-world challenges and foster innovation in underprivileged communities. " \
"I look forward to applying my technical and analytical skills in a dynamic internship setting.\n")
file.close()

# To confirm the updated version by using read file format only
file = open('newFile.txt', 'r')
data = file.read()
print(data)
file.close()


#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
finally:
    print("Execution completed.")