from googleapiclient.discovery import build


class GmailService:
    def __init__(self, creds):
        self.service = build('gmail', 'v1', credentials=creds)

    def fetch_emails(self, max_results=20):
        results = self.service.users().messages().list(
            userId='me',
            maxResults = max_results
        ).execute()

        messages = results.get('messages', [])
        email_data = []

        for msg in messages:
            msg_detail = self.service.users().messages().get(
                userId='me',
                id=msg['id']
            ).execute()

            headers = msg_detail['payload']['headers']

            subject = next(
                (h['value'] for h in headers if h['name'] == 'Subject'),
                None
            )

            email_data.append({
                'id': msg['id'],
                'subject': subject
            })

        return email_data