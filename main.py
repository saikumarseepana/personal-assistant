from app.auth.gmail_auth import get_gmail_credentials
from app.services.gmail_service import GmailService
from app.storage.json_store import JSONStore


if __name__ == "__main__":
    creds = get_gmail_credentials()
    
    gmail_service = GmailService(creds)
    store = JSONStore()

    # Load previously stored emails
    old_emails = store.load()
    old_ids = set(email['id'] for email in old_emails)

    # Fetch new emails
    new_emails = gmail_service.fetch_emails()

    # Filter only unseen emails
    unseen_emails = [email for email in new_emails if email['id'] not in old_ids]

    print("New Emails:")
    for email in unseen_emails:
        print(email['subject'])

    # Merge old + new emails and save
    updated_emails = old_emails + unseen_emails
    store.save(updated_emails)

    