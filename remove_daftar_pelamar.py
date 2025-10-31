import os
import re

# Directory to process
base_dir = "d:\\Project-an\\carier-pro"

# Files to update (non-admin)
files_to_update = [
    "index.html",
    "lowongan.html",
    "detail-lowongan.html",
    "daftar.html",
    "faq.html",
    "user-pelamar.html"
]

# Pattern to remove Daftar Pelamar link from navbar
navbar_pattern = r'<a href="user-pelamar\.html" class="text-gray-600 hover:text-green-600">Daftar Pelamar</a>\s*'

# Footer pattern - also remove references if any
footer_pattern = r'<li><a href="user-pelamar\.html"[^>]*>Daftar Pelamar</a></li>\s*'

def remove_daftar_pelamar(file_path):
    """Remove all Daftar Pelamar links from navbar and footer"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove from navbar
        content = re.sub(navbar_pattern, '', content)
        
        # Remove from footer if exists
        content = re.sub(footer_pattern, '', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {os.path.basename(file_path)}: Removed Daftar Pelamar link")
            return True
        else:
            print(f"  {os.path.basename(file_path)}: No Daftar Pelamar link found")
            return False
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {str(e)}")
        return False

print("=" * 60)
print("REMOVING 'DAFTAR PELAMAR' LINKS")
print("=" * 60)

removed_count = 0
for file in files_to_update:
    file_path = os.path.join(base_dir, file)
    if os.path.exists(file_path):
        if remove_daftar_pelamar(file_path):
            removed_count += 1
    else:
        print(f"  ⚠ {file}: File not found")

print("\n" + "=" * 60)
print(f"✅ Done! Updated {removed_count} files")
print("=" * 60)
