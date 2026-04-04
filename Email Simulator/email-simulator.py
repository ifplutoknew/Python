#Email Simulator - A simple program to simulate sending, receiving, and managing emails.
#Provides Email, Inbox, and User classes to create a basic email system.
#Created by: C.K Baloyi
#Date: 2026-03-24

import datetime



#Represents a single email message with sender, receiver, subject, body, and status.
class Email:    
    def __init__(self, sender, receiver, subject, body):
        # sender: User object sending the email
        # receiver: User object receiving the email
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()  # Record time when email sent
        self.read = False            #Track whether email has been read

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        #Display the complete email content and mark it as read.
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'  
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Inbox:
    def __init__(self):
        self.emails = []  # List to store Email objects

    def receive_email(self, email):
        #Add a new email to the inbox.
        self.emails.append(email)

    def list_emails(self):
        #Display a summary of all emails in the inbox."""
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
    
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        # Convert 1-based user input to 0-based list index
        actual_index = index - 1

        # Validate that the index is within bounds
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        # Convert 1-based user input to 0-based list index
        actual_index = index - 1

        # Validate that the index is within bounds
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
class User:
    #Represents a user who can send and receive emails."""
    
    def __init__(self, name):
        #Initialize a user with a name and their own inbox.
        
        self.name = name
        self.inbox = Inbox()  # Each user has their own inbox

    def send_email(self, receiver, subject, body):
        #Send an email to another user.
        # Create the email and add it directly to the receiver's inbox
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        """Display a summary of emails in the user's inbox."""
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)

def main():
    # Create two test users
    tory = User('Tory')
    ramy = User('Ramy')        
    
    # Simulate email exchanges
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    # Demonstrate inbox operations for Ramy
    ramy.check_inbox()
    ramy.read_email(1)  # Read the first email
    ramy.delete_email(1)  # Delete the first email
    ramy.check_inbox()  # Show updated inbox

    # Demonstrate inbox operations for Tory
    tory.check_inbox()
    tory.read_email(1)  # Read the first email


# Run the email simulator 
if __name__ == '__main__':
    main()