from cryptography.fernet import Fernet
import os
import getpass
import re

#1. Add check if a new password file wants to be created, telling user that a password file 
# already exists if they want to delete old password file and create a new one or ovewrite existing one
# 2. Add a condition if user wants to create a new key while a key already exists, that the old key will be deleted
# 3. There can only be one key at a time



class PasswordManager:
    # Menu options as constants
    MENU = """ What do you want to do?
          (1) Create a new key
          (2) Load an exisiting key
          (3) Create new password file
          (4) Load exisiting password file
          (5) Add a new password
          (6) Get a password
          (7) List all passwords
          (8) Delete a password
          (9) Quit (q)
 """
    OVERWRITE_MENU = """
Password file already exists and contains data!
(1) Overwrite existing file
(2) Delete old file and create new one
(3) Cancel
"""
    
    def __init__(self):
        self.key = None
        self.cipher = None  # Cipher object to avoid creating it multiple times
        self.password_file = None
        self.password_dic = {}

    @staticmethod
    def check_password_strength(password):
        """Check password strength and return score + feedback"""
        score = 0
        feedback = []
        
        # Check length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("- At least 8 characters")
        
        # Check for uppercase
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("- Include uppercase letters (A-Z)")
        
        # Check for lowercase
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("- Include lowercase letters (a-z)")
        
        # Check for numbers
        if re.search(r'[0-9]', password):
            score += 1
        else:
            feedback.append("- Include numbers (0-9)")
        
        # Check for special characters
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("- Include special characters (!@#$%^&*)")
        
        # Rate strength
        if score == 5:
            strength = "STRONG"
        elif score >= 3:
            strength = "MODERATE"
        else:
            strength = "WEAK"
        
        return strength, feedback

    def create_key(self, path):
        """Generate a new encryption key and save it to file"""
        try:
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)  # Create cipher object once
            with open(path,'wb') as f:
                f.write(self.key)
            print(f"Key created and saved to '{path}'")
        except Exception as e:
            print(f"Error creating key: {e}")
    
    def load_key(self,path):
        """Load encryption key from file"""
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
            self.cipher = Fernet(self.key)  # Create cipher object once
            print(f"Key loaded from '{path}'")
        except FileNotFoundError:
            print(f"Error: Key file '{path}' not found")
        except Exception as e:
            print(f"Error loading key: {e}")
    
    def create_password_file(self, path, initial_values=None):
        """Create a new password file with optional initial values"""
        # Check if a key has been loaded/created
        if self.key is None:
            print("\nError: No key loaded or created!")
            print("Please create or load a key first (options 1 or 2).")
            return
        
        # Check if password file already exists
        if os.path.exists(path):
            # Check if file is empty
            if os.path.getsize(path) == 0:
                print(f"Password file '{path}' is empty. Starting fresh...")
            else:
                # File is not empty, ask user what to do
                print(f"\nPassword file '{path}' already exists and contains data!")
                print(self.OVERWRITE_MENU)
                action = input("Enter your choice (1-3): ")
                
                if action == '1':
                    # Count existing passwords to warn user
                    existing_count = len(self.password_dic)
                    if existing_count > 0:
                        print(f"\nWARNING: You will delete {existing_count} existing passwords!")
                        confirm = input("Are you sure you want to overwrite? (yes/no): ")
                        if confirm.lower() != 'yes':
                            print("Operation cancelled.")
                            return
                    
                    print("Overwriting existing file...")
                    # Clear the file by opening it in write mode
                    open(path, 'w').close()
                    # Clear the password dictionary to start fresh
                    self.password_dic.clear()
                elif action == '2':
                    existing_count = len(self.password_dic)
                    if existing_count > 0:
                        print(f"\nWARNING: You will delete {existing_count} existing passwords!")
                        confirm = input("Are you sure you want to delete? (yes/no): ")
                        if confirm.lower() != 'yes':
                            print("Operation cancelled.")
                            return
                    
                    os.remove(path)
                    print("Old file deleted. Creating new password file...")
                    # Clear the password dictionary to start fresh
                    self.password_dic.clear()
                elif action == '3':
                    print("Operation cancelled.")
                    return
                else:
                    print("Invalid choice. Operation cancelled.")
                    return
        
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
        
        print(f"Password file created at '{path}'")

    def load_password_file(self, path):
        """Load existing password file and decrypt passwords"""
        if self.cipher is None:
            print("Error: No key loaded. Load or create a key first.")
            return
        
        try:
            self.password_file = path
            self.password_dic.clear()  # Clear old passwords to start fresh
            
            with open(path, 'r') as f:
                for line in f.readlines():
                    line = line.strip()  # Remove trailing newline
                    if line:  # Skip empty lines
                        site, encrypted_password = line.split(":")
                        self.password_dic[site] = self.cipher.decrypt(encrypted_password.encode()).decode()
            
            print(f"Password file loaded from '{path}'. {len(self.password_dic)} passwords loaded.")
        except FileNotFoundError:
            print(f"Error: Password file '{path}' not found")
        except ValueError as e:
            print(f"Error: Invalid password file format - {e}")
        except Exception as e:
            print(f"Error loading password file: {e}")
    
    def add_password(self,site, password):
        """Add a new password to dictionary and save to file"""
        if self.cipher is None:
            print("Error: No key loaded. Load or create a key first.")
            return
        
        if self.password_file is None:
            print("Error: No password file opened. Please load or create a password file first.")
            return
        
        try:
            self.password_dic[site]=password
            if self.password_file is not None:
                with open(self.password_file,'a+') as f:
                    encrypted = self.cipher.encrypt(password.encode())
                    f.write(f"{site}:{encrypted.decode()}\n")
            print(f"Password for '{site}' added.")
        except Exception as e:
            print(f"Error adding password: {e}")
    
    def get_password(self, site):
        """Retrieve password for a site"""
        if self.password_file is None:
            print("Error: No password file opened. Please load or create a password file first.")
            return None
        
        try:
            return self.password_dic[site]
        except KeyError:
            print(f"Error: No password found for '{site}'")
            return None
    
    def list_passwords(self):
        """Display all stored password sites"""
        if self.password_file is None:
            print("Error: No password file opened. Please load or create a password file first.")
            return
        
        if not self.password_dic:
            print("No passwords stored.")
            return
        
        print("\n" + "="*50)
        print(f"Stored Passwords ({len(self.password_dic)} total):")
        print("="*50)
        for i, site in enumerate(self.password_dic.keys(), 1):
            print(f"{i}. {site}")
        print("="*50 + "\n")
    
    def delete_password(self, site):
        """Delete a password for a specific site"""
        if self.password_file is None:
            print("Error: No password file opened. Please load or create a password file first.")
            return False
        
        if site not in self.password_dic:
            print(f"Error: No password found for '{site}'")
            return False
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete password for '{site}'? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return False
        
        try:
            del self.password_dic[site]
            
            if self.password_file is not None:
                # Rewrite the entire file without the deleted password
                with open(self.password_file, 'w') as f:
                    for stored_site, password in self.password_dic.items():
                        encrypted = self.cipher.encrypt(password.encode())
                        f.write(f"{stored_site}:{encrypted.decode()}\n")
                print(f"Password for '{site}' deleted successfully.")
            else:
                print(f"Password for '{site}' deleted from memory (not saved to file).")
            
            return True
        except Exception as e:
            print(f"Error deleting password: {e}")
            return False


def display_menu():
    """Display the main menu"""
    print(PasswordManager.MENU)


def main():
    """Main program loop"""
    password={
        'email': "123456",
        "facebook": 'myfbpassword',
        "youtube": "hellowworld123",
        "something": 'myfavoritepassword_123'
    }

    pm=PasswordManager()
    
    display_menu()
    done = False
    while not done:
        choice=input("Enter your choice: ")
        
        try:
            if choice=='1':
                path = input("Enter path: ")
                pm.create_key(path)
            elif choice=='2':
                path = input('Enter path: ')
                pm.load_key(path)
            elif choice=="3":
                path = input('Enter path: ')
                pm.create_password_file(path, password)
            elif choice=='4':
                path = input('Enter path: ')
                pm.load_password_file(path)
            elif choice=='5':
                site=input('Enter the site: ')
                password_input = getpass.getpass('Enter the password (hidden): ')
                
                # Check password strength
                strength, feedback = PasswordManager.check_password_strength(password_input)
                print(f"\nPassword Strength: {strength}")
                
                if feedback:
                    print("Suggestions to improve:")
                    for suggestion in feedback:
                        print(f"  {suggestion}")
                
                if strength == "WEAK":
                    use_weak = input("\nWARNING: Password is weak. Use it anyway? (yes/no): ")
                    if use_weak.lower() != 'yes':
                        print("Password not added.")
                        continue
                
                pm.add_password(site, password_input)
            elif choice=='6':
                site=input('What site do you want: ')
                pwd = pm.get_password(site)
                if pwd:
                    print(f"Password for '{site}' is: {pwd}")
            elif choice=='7':
                pm.list_passwords()
            elif choice=='8':
                pm.list_passwords()
                site = input('Enter the site to delete: ')
                pm.delete_password(site)
            elif choice=="9" or choice=="q":
                done=True
                print('Bye')
            else:
                print('Invalid choice')
            
            # Show menu again
            if not done:
                print()
                display_menu()
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            done = True
        except Exception as e:
            print(f"Unexpected error: {e}")
        
if __name__ == "__main__":
    main()



