from app.auth.gmail_auth import get_gmail_credentials
from app.services.gmail_service import GmailService
from app.storage.json_store import JSONStore


if __name__ == "__main__":
    creds = get_gmail_credentials()
    
    gmail_service = GmailService(creds)
    emails = gmail_service.fetch_emails()

    store = JSONStore()
    store.save(emails)

    print(emails)
    