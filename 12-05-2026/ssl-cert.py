import ssl
import socket
from datetime import datetime

def check_ssl_expiry(domain):
    """Check SSL certificate expiry date for a domain"""
    
    try:
        # Create SSL context
        context = ssl.create_default_context()
        
        # Connect to the domain on port 443
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Get certificate information
                cert = ssock.getpeercert()
                
                # Extract expiry date
                expiry_date_str = cert['notAfter']
                expiry_date = datetime.strptime(
                    expiry_date_str, "%b %d %H:%M:%S %Y %Z"
                )
                
                # Calculate days remaining
                days_remaining = (expiry_date - datetime.now()).days
                
                return expiry_date, days_remaining
                
    except socket.error as e:
        print(f"Connection error: {e}")
        return None, None
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None


def main():
    domain = input("Enter domain (e.g., google.com): ").strip()
    
    # Remove https:// or www. if user added them
    domain = domain.replace("https://", "").replace("http://", "")
    domain = domain.replace("www.", "").split("/")[0]
    
    expiry_date, days_remaining = check_ssl_expiry(domain)
    
    if expiry_date:
        print(f"\n✓ SSL Certificate for {domain}:")
        print(f"  Expiry Date: {expiry_date}")
        print(f"  Days Remaining: {days_remaining}")
        
        # Alert based on days remaining
        if days_remaining < 0:
            print("  ⚠️  STATUS: EXPIRED!")
        elif days_remaining < 30:
            print("  ⚠️  STATUS: Expiring soon (less than 30 days)")
        elif days_remaining < 90:
            print("  ⚡ STATUS: Warning (less than 90 days)")
        else:
            print("  ✓ STATUS: Valid")
    else:
        print(f"\n✗ Could not retrieve SSL certificate for {domain}")


if __name__ == "__main__":
    main()
