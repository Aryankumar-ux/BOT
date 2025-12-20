#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    print("\n" + "="*50)
    print("🤖 TELEGRAM BOT SETUP SCRIPT")
    print("="*50)
    
    # Get user inputs
    bot_token = input("\nEnter BOT_TOKEN: ").strip()
    if not bot_token:
        print("❌ Error: BOT_TOKEN is required!")
        return
    
    chat_id = input("Enter Chat ID: ").strip()
    if not chat_id:
        print("❌ Error: Chat ID is required!")
        return
    
    username = input("Enter Username(Without @): ").strip()
    if not username:
        print("❌ Error: Username is required!")
        return
    
    print("\n" + "-"*50)
    print("🛠️  Setting up your bot...")
    
    # Check if setup.txt exists
    if not os.path.exists("setup.txt"):
        print("❌ ERROR: setup.txt not found in current directory!")
        print(f"Current directory: {os.getcwd()}")
        print("Please make sure setup.txt exists with your bot code.")
        return
    
    # Read ALL content from setup.txt
    with open("setup.txt", "r", encoding="utf-8") as f:
        setup_content = f.read()
    
    print(f"✅ Read {len(setup_content)} characters from setup.txt")
    
    # Create main.py with bot config + ALL setup.txt content
    with open("main.py", "w", encoding="utf-8") as f:
        # Write bot configuration at the top
        f.write(f'BOT_TOKEN = "{bot_token}"\n')
        f.write(f'ADMIN_USER_ID = {chat_id}\n')
        f.write(f'ADMIN_USERNAME = "{username}"\n\n')
        
        # Write ENTIRE content from setup.txt
        f.write(setup_content)
    
    print("✅ main.py created successfully!")
    
    # Install requirements if requirements.txt exists
    if os.path.exists("requirements.txt"):
        print("\n📦 Installing requirements from requirements.txt...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("✅ Requirements installed successfully!")
            else:
                print("⚠️  Some requirements failed to install")
                if result.stderr:
                    print(result.stderr[:200])
        except Exception as e:
            print(f"⚠️  Error installing requirements: {e}")
    else:
        print("\n⚠️  requirements.txt not found - skipping dependency installation")
    
    # Final success message
    print("\n" + "✨"*50)
    print("✨"*50)
    print("\n🎉 BOT SETUP COMPLETED SUCCESSFULLY!")
    print("\n" + "═"*50)
    print("🤖 BOT SCRIPT IS READY!")
    print("═"*50)
    print("\n📋 To run your bot, use this command:")
    print("\n" + ">"*30)
    print("    python main.py")
    print("<"*30)
    print("\n📍 Your bot file is ready at:")
    print(f"    {os.path.abspath('main.py')}")
    print("\n" + "✨"*50)
    print("✨"*50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")