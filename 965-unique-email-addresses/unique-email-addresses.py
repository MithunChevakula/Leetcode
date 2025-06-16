class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # To store unique email addresses

        for email in emails:
            local_name, domain_name = email.split('@')
            
            # Process local name: remove periods and ignore part after plus sign
            local_name = local_name.split('+')[0]  # Get part before '+'
            local_name = local_name.replace('.', '')  # Remove all '.'

            # Combine processed local name with domain name
            unique_email = f"{local_name}@{domain_name}"
            unique_emails.add(unique_email)  # Add to the set

        return len(unique_emails)  # The size of the set is the number of unique emails


