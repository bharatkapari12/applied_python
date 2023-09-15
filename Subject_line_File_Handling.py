def subject_count(file_name):
    subject_line_count = 0
    with open('/home/bharat/MEGA/SunwayMega/BCS 5th Sem/Applied Programming/Assignments/Final_Exam/short_Qns/emails.txt', 'r') as file:
        for line in file:
            if line.startswith("Subject line:"):
                print(line)
                # print(line.strip())  # displays the line
                subject_line_count += 1  # increases the munber count

    print(f"Total number of lines starting with 'Subject line:': {subject_line_count}")

file_name = input("Enter the file name: ")
subject_count(file_name)




# def count_subject_lines(file_name):
#     subject_line_count = 0
#     with open(file_name, "a") as file:
#         file.write("Subject: Welcome to IUKL!\n")
#         file.write("Subject: Important update on your application\n")
#         file.write("Subject: Reminder about upcoming deadline\n")

#     with open(file_name) as file:
#         for line in file:
#             if line.startswith("Subject:"):
#                 print(line)
#                 subject_line_count += 1

#     print(f"Total number of lines starting with 'Subject:': {subject_line_count}")

# file_name = "emails.txt"
# count_subject_lines(file_name)





# def count_subject_lines(file_name):
#     subject_line_count = 0
#     with open(file_name, "w") as file:  # Use "w" to overwrite the file each time
#         while True:
#             subject_line = input("Enter a subject line (or leave blank to exit): ")
#             if not subject_line:
#                 break
#             file.write(subject_line + "\n")
#             subject_line_count += 1

#     with open(file_name) as file:
#         for line in file:
#             if line.startswith("Subject:"):
#                 print(line)

#     print(f"Total number of lines starting with 'Subject:': {subject_line_count}")

# file_name = "emails.txt"
# count_subject_lines(file_name)






# def read_and_display_subject_lines():
#     file_name = input("Enter the name of the file: ")

#     with open('/home/bharat/MEGA/SunwayMega/BCS 5th Sem/Applied Programming/Assignments/Final_Exam/short_Qns/emails.txt', 'r') as file:
#         subject_lines_count = 0  # Initialize a counter for matching lines
#         for line in file:
#             if line.startswith("Subject line:"):
#                 print(line.strip())  # Display the line
#                 subject_lines_count += 1  # Increment the counter

#         if subject_lines_count > 0:
#             print(f"Found {subject_lines_count} lines starting with 'Subject line:'.")
#         else:
#             print("No lines starting with 'Subject line:' found in the file.")

# # Call the method to execute it
# read_and_display_subject_lines()
