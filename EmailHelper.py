from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 
from email import encoders

# NOTE CHROME MUST BE INSTALLED
# https://github.com/b1tst0rm/pygsuite/blob/master/send.py
def gmail_sendemail(logger, email_from, email_to, email_subiect, logfile_path, computername):
    # body = (
    #     """{}""".format(log)
    # )

    msg = MIMEMultipart()
    msg['Subject'] = ("{} - Log Explorer.exe".format(computername))
    msg['From'] = email_from
    msg['To'] = email_to
    # msg.set_content(body)

    # Setup the attachment
    filename = os.path.basename(logfile_path)
    attachment = open(logfile_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)

    # CHROME MUST BE INSTALLED
    context = ssl.create_default_context()

    try:
        # Do NOT use STMP_SSL, it fails negotiating SSL versions.
        # Instead use the starttls command to force encryption.
        # server = None
        server = smtplib.SMTP('smtp-relay.gmail.com', 587)
        server.set_debuglevel(1)
        server.starttls(context=context)
        server.send_message(msg)
        server.quit()
        logger.info("EMAIL SENT!")

    except socket.error as e:
        logger.error("Could not connect server")
    except:
        logger.error("Unknown error:", sys.exc_info()[0])
        logger.error(traceback.print_exc())