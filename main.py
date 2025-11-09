import subprocess
import re

def cl():

    profiles_output = subprocess.run(
        ["netsh", "wlan", "show", "profiles"], 
        capture_output=True, 
        text=True, 
        encoding='cp866'
    ).stdout
    
    profiles = re.findall(r"All User Profile\s+:\s(.*)", profiles_output)
    
    print("Сохраненные Wi-Fi пароли:")
    
    for profile in profiles:
        profile = profile.strip()
        if not profile:
            continue
            
        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", f'name="{profile}"', "key=clear"], 
            capture_output=True, 
            text=True,
            encoding='cp866'
        ).stdout
        
        # Извлекаем пароль
        key_match = re.search(r"Key Content\s+:\s(.*)", profile_info)
        password = key_match.group(1).strip() if key_match else "Открытая сеть"
        
        print(f"{profile}: {password}")

if __name__ == "__main__":
    cl()