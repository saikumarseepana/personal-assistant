class EmailProcessor:
    def extract_email_data(self, msg_detail):
        headers = msg_detail['payload']['headers']

        print(headers)

        subject = next(
            (h['value'] for h in headers if h['name'] == 'Subject'),
            None
        )

        return {
            'id': msg_detail['id'],
            'subject': subject
        }