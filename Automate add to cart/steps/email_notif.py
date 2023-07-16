@then('send email notification')
def step_impl(context):
    print("Task completed")
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        sender="hellojaned123@gmail.com"
        sender_password="rzlzacazmtdkoqoj"
        receiver="hellojaned123@gmail.com"
        smtp.login(sender,sender_password)
        subject="The program was executed successfully"
        body="Task successful"
        message=f'Subject: {subject}\n\n{body}'
        smtp.sendmail(sender,receiver,message)
        print("Email sent!")
