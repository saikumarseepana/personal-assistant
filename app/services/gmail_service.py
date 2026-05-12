from googleapiclient.discovery import build
from app.processors.email_processor import EmailProcessor


class GmailService:
    def __init__(self, creds):
        self.service = build('gmail', 'v1', credentials=creds)
        self.processor = EmailProcessor()

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

            processed_email = self.processor.extract_email_data(msg_detail)


            email_data.append(processed_email)

        return email_data