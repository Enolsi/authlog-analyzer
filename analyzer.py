failed_attempts = {}

targeted_users = {}

successful_logins = {}

successful_users = {}


with open("sample_auth.log","r") as file:

    for line in file:
 
        if "Accepted password" in line:

            parts = line.split()

            ip = parts [10]

            user = parts [8]

            if ip not in successful_users:
                
                successful_users[ip] = set()

            successful_users[ip].add(user)

            if ip in successful_logins: 
               
                successful_logins[ip] += 1
                
            else: 
              
               successful_logins[ip] = 1

        if "Failed password" in line:

            parts = line.split()

            user = parts [8] 

            ip = parts[10]

            if ip not in targeted_users:

                targeted_users[ip] = set()
            
            targeted_users[ip].add(user)
            
            if ip in failed_attempts:

                failed_attempts[ip] += 1
            
            
            
            else:

                failed_attempts[ip] = 1

print("=== AuthLog Analyzer ===")

for ip, count in failed_attempts.items():

  print(f"IP: {ip}")

  print(f"Failed attempts: {count}")

  print(f"Users targeted: {','.join(targeted_users[ip])}")

  if count >= 3:

      print("[!] Possible brute-force activity detected")

print("\n=== Successful logins ===")

for ip, count in successful_logins.items():
     print(f"IP: {ip}")
     print(f"Successful logins: {count}")
     print(f"Users: {','.join(successful_users[ip])}")

for ip, count in successful_logins.items():

     print("[!] Warning: this IP has failed attemps before a successful login")
